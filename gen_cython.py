import os
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap

class CythonConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        if self.type == Type.STRING:
            return self.generator.get_template('#define {{ constant.name }} "{{ constant.value }}"').render(constant=self)
        else:
            return self.generator.get_template('#define {{ constant.name }} {{ constant.value }}').render(constant=self)

class CythonDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
//===========================================================================================================
//
// Define {{ define.name }}
//
// {% if define.doc %}{{ define.doc | doc_sanitize | comment }}{% endif %}
//
{%- for constant in define.constants %}
// {{ constant.name }}
// {% if constant.doc %}{{ constant.doc | doc_sanitize | comment }}{% endif %}
//
{%- endfor %}
//===========================================================================================================
{% for constant in define.constants %}
{{ constant.render() }}
{%- endfor %}

""").render(define=self)

def get_c_type(type):
    if type == Type.VOID:
        return "void"
    elif type == Type.DOUBLE:
        return "double"
    elif type == Type.INT32_T:
        return "int32_t"
    elif type == Type.INT16_T:
        return "int16_t"
    elif type == Type.STRING:
        return "char"
    else:
        return "int32_t"


class CythonParameter(Parameter):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def c_type(self):
        if self.is_ref:
            return '{}*'.format(get_c_type(self.type))
        elif self.is_val:
            return '{}'.format(get_c_type(self.type))
        else:
            return 'const {}*'.format(get_c_type(self.type))

    def render_c_doc(self, indent_spaces):
        if self.doc:
            return self.generator.get_template(
                '{% set type_len = param.c_type|length %}{{ param.doc | doc_sanitize | comment(comment_first_line=True) | indent(indent_spaces-type_len, True) | indent(indent_spaces+1) }}'
            ).render(param=self, indent_spaces=indent_spaces)
        else:
            return self.generator.get_template(
                '{% set type_len = param.c_type|length %}{{ "//" | indent(indent_spaces-type_len, True) }}').render(param=self, indent_spaces=indent_spaces)



class CythonMethod(Method):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        return self.generator.get_template("""
cdef extern {{ method.c_return_type }} {{ method.exposed_name }}{{ method.render_parameters() }}""").render(method=self)

    @property
    def exposed_name(self):
        if self.external_name:
            return self.external_name
        else:
            if self.is_app:
                return 'App_{}'.format(self.name)
            else:
                return self.name

    def render_parameters(self):
        return self.generator.get_template("""(void*{% for param in parameters %}, {{ param.c_type }}{% endfor %});""").render(parameters=self.parameters)

    @property
    def c_return_type(self):
        return get_c_type(self.return_type)


class CythonClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def cdef_declarations(self):
        return self.generator.get_template("""
{{- cl.header -}}
{{- cl.c_methods -}}
""").render(cl=self)

    @property
    def class_wrapper(self):
        return self.generator.get_template("""

cdef class Wrap{{ cl.name }}:
    
    {{ cl.init_dealloc }}

""").render(cl=self)

    @property
    def init_dealloc(self):
        if self.is_static:
            return """
    pass
"""
        else:
            return self.generator.get_template("""

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            {{ cl.default_destroy_method }}(get_p_geo(), &self.handle)

""").render(cl=self)


    @property
    def header(self):
        return self.generator.get_template("""
# Class {{ cl.name }}
""").render(cl=self)


    @property
    def c_methods(self):
        if len(self.method_groups) == 1:
            method_group = next(iter(self.method_groups.values()))
            return self.render_method_group(method_group)
        else:
            return self.generator.get_template("""
{% for key, method_group in cl.method_groups.items() %}
# {{ key }}

{{ cl.render_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_method_group(self, method_group):
        return self.generator.get_template("""
{% for method in methods %}
{{ method.render() }}
{% endfor %}
""").render(methods=method_group)


class CythonCodeGenerator(CodeGeneratorBase):
    def __init__(self):
        super().__init__(constant_type=CythonConstant, define_type=CythonDefine, parameter_type=CythonParameter,
                         method_type=CythonMethod, class_type=CythonClass)

    def render_pyx(self):
        return self.get_template('''
# cython: c_string_type=unicode, c_string_encoding=utf8

from libc.stdint cimport int32_t, int16_t
from libc.stdlib cimport malloc, free

import threading
from threading import current_thread

thread_local = threading.local()

from geosoft.gxapi import GXCancel, GXExit, GXAPIError, GXError

{% for key, cl in classes.items() %}
{{ cl.cdef_declarations }}
{% endfor %}

cdef extern void* pCreate_GEO(const char*, const char*, int32_t, void*, int32_t, char*, int32_t);
cdef extern void Destroy_GEO(void *);

cdef unicode tounicode(char* s):
    return s.decode('UTF-8', 'strict')

cdef unicode tounicode_with_length(
        char* s, size_t length):
    return s[:length].decode('UTF-8', 'strict')

cdef unicode tounicode_with_length_and_free(
        char* s, size_t length):
    try:
        return s[:length].decode('UTF-8', 'strict')
    finally:
        free(s)

cdef class WrapPGeo:
    cdef void* p_geo
    
    def __cinit__(self, const char* app, const char* ver, wind_id=0):
        cdef void* hParentWnd = <void *>wind_id
        cdef char* err = <char*>malloc(4096)
        try:
            tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
            if not tls_geo is None:
                raise GXAPIError("Only one gxapi_cy.WrapPGeo instance per thread allowed.");
            self.p_geo = pCreate_GEO(app, ver, 0, hParentWnd, 0, err, 4096)
            if self.p_geo == NULL:
                raise GXAPIError(tounicode(err))
            thread_local.gxapi_cy_geo = <size_t>self.p_geo
        finally:
            free(err)
        
    def __dealloc__(self):
        if self.p_geo != NULL:
            Destroy_GEO(self.p_geo)
        thread_local.gxapi_cy_geo = None

    cdef _raise_on_gx_errors(self, void* p_geo):
        cdef int32_t term
        cdef char* module
        cdef char* err
        cdef int32_t error_number
        if iCheckTerminate_SYS(p_geo, &term) > 0:
            if term == 0:
                raise GXExit()
            elif term == -1:
                raise GXCancel()
            else:
                module = <char*>malloc(1024)
                err = <char*>malloc(4096)
                try:
                    sGetError_GEO(p_geo, module, 1024, err, 4096, &error_number)
                    if (error_number == 21023 or error_number == 21031 or # These two due to GXX asserts, Abort_SYS etc
                        error_number == 31009 or error_number == 31011):  # wrapper bind errors
                        raise GXAPIError(tounicode(err));
                    else:
                        raise GXError(tounicode(err), tounicode(module), error_number)
                finally:
                    if module != NULL:
                        free(module)
                    if err != NULL:
                        free(err)
    
    def dot_product(self, p1, p2, p3, p4, p5, p6):
        cdef double dp1 = p1, dp2 = p2, dp3 = p3, dp4 = p4, dp5 = p5, dp6 = p6
        retval = rDotProduct3D_MATH(self.p_geo, &dp1, &dp2, &dp3, &dp4, &dp5, &dp6)
        self._raise_on_gx_errors(self.p_geo)
        return retval

cdef void* get_p_geo():
    tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
    if not tls_geo is None:
        raise GXAPIError("A gxapi_cy.WrapPGeo instance has not been instantiated on current thread yet.");
    return <void*>tls_geo

{% for key, cl in classes.items() %}
{{ cl.class_wrapper }}
{% endfor %}

''').render(classes=self.classes)


# running as stand-alone program
if __name__ == "__main__":
    gen = CythonCodeGenerator()
    print(gen.render_pyx())