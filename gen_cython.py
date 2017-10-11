import os, sys
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
import getopt

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

class CythonParameter(Parameter):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def c_type(self):
        return self.generator.get_c_type(self.type, is_ref=self.is_ref, is_val=self.is_val)
        
    def cy_assign(self, index):
        c_type = self.generator.get_c_type(self.type, is_val=True)
        return c_type

class CythonMethod(Method):
    def __init__(self, other):
        super().construct_copy(other)

    def render_c(self):
        return self.generator.get_template("""
cdef extern {{ method.c_return_type }} {{ method.exposed_name }}{{ method.render_c_parameters() }}""").render(method=self)

    def render_wrapper(self):
        if self.is_destroy_method:
            return ""
        else:
            return self.generator.get_template("""
    def {{ method.ext_method_name }}({{ method.wrap_first_parm }}{{ method.wrap_parameters }}):
        
        pass
""").render(method=self)
    
    def render_c_parameters(self):
        return self.generator.get_template("""(void*{% for param in parameters %}, {{ param.c_type }} {{ param.name }}{% endfor %});""").render(parameters=self.parameters)

    @property
    def wrap_parameters(self):
        return self.generator.get_template("{% for param in in_params %}, {{ param.name }}{% endfor %}").render(in_params=self.in_params)

    @property
    def wrap_first_parm(self):
        return "cls" if self.is_static else "self"

    @property
    def c_return_type(self):
        return self.generator.get_c_type(self.return_type, is_val=True)


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
        if not self.has_methods:
            return ""
        else:
            return self.generator.get_template("""

cdef class Wrap{{ cl.name }}:
    
{{ cl.init_dealloc }}

{{ cl.wrap_methods }}

""").render(cl=self)

    @property
    def init_dealloc(self):
        if self.is_static:
            return ""
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
            return self.render_c_method_group(method_group)
        else:
            return self.generator.get_template("""
{% for key, method_group in cl.method_groups.items() %}
# {{ key }}

{{ cl.render_c_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_c_method_group(self, method_group):
        return self.generator.get_template("""
{% for method in methods %}
{{ method.render_c() }}
{% endfor %}
""").render(methods=method_group)


    @property
    def wrap_methods(self):
        if len(self.method_groups) == 1:
            method_group = next(iter(self.method_groups.values()))
            return self.render_wrap_method_group(method_group)
        else:
            return self.generator.get_template("""
{% for key, method_group in cl.method_groups.items() %}
# {{ key }}

{{ cl.render_wrap_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_wrap_method_group(self, method_group):
        return self.generator.get_template("""
{% for method in methods %}
{{ method.render_wrapper() }}
{% endfor %}
""").render(methods=method_group)

class CythonCodeGenerator(CodeGeneratorBase):
    def __init__(self):
        super().__init__(constant_type=CythonConstant, define_type=CythonDefine, parameter_type=CythonParameter,
                         method_type=CythonMethod, class_type=CythonClass)

    def get_c_type(self, type, is_val=False, is_ref=False):
        if type is str:
            type = type.replace("_stdcall", "")
            is_val = is_val or not type.find('*') == -1
        c_type = type
        if type == Type.VOID:
            c_type = "void"
        elif type == Type.DOUBLE:
            c_type = "double"
        elif type == Type.INT32_T:
            c_type = "int32_t"
        elif type == Type.INT16_T:
            c_type = "int16_t"
        elif type == Type.STRING:
            c_type = "char"
        elif type in self.classes or type in self.definitions:
            c_type = "int32_t"
        
        if is_ref:
            return '{}*'.format(c_type)
        elif is_val:
            return c_type
        else:
            return 'const {}*'.format(c_type)


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

cdef extern from "Windows.h":

    ctypedef Py_UNICODE WCHAR
    ctypedef const WCHAR* LPCWSTR
    ctypedef void* HWND

    int_value MessageBoxW(HWND hWnd, LPCWSTR lpText, LPCWSTR lpCaption, int_value uType)

#title = u"Windows Interop Demo - Python %d.%d.%d" % sys.version_info[:3]
#MessageBoxW(NULL, u"Hello Cython \u263a", title, 0)


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
    
cdef void* get_p_geo():
    tls_geo = getattr(thread_local, 'gxapi_cy_geo', None)
    if not tls_geo is None:
        raise GXAPIError("A gxapi_cy.WrapPGeo instance has not been instantiated on current thread yet.");
    return <void*>tls_geo

{% for key, cl in classes.items() %}
{{ cl.class_wrapper }}
{% endfor %}

''').render(classes=self.classes)

def usage():
    print('gen_cython.py -o <outputfile.pyx>')
    sys.exit(2)
def main(argv):
    outputfile = None
    try:
        opts, args = getopt.getopt(argv,"ho:",["ofile="])
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if opt == '-h':
            usage()
        elif opt in ("-o", "--ofile"):
            outputfile = arg
    if not outputfile:
        usage()

    with open(outputfile, 'wb') as f:
        gen = CythonCodeGenerator()
        #f.write(gen.classes['3DN'].method_groups['Miscellaneous'][0].parameters[0].c_type.encode('UTF-8'))
        f.write(gen.render_pyx().encode('UTF-8'))
    

if __name__ == "__main__":
   main(sys.argv[1:])