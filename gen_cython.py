import os, sys
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
import getopt

type_map = {
    'CRC': 'int32_t',
    'WND': 'int32_t',
    'PTMP': 'int32_t',
    'FILTER': 'int32_t',
    'DGW_OBJ': 'int32_t',
    'TB_FIELD': 'int32_t',
    'DB_SELECT': 'int32_t',
    'DB_SYMB': 'int32_t',
    'META_TOKEN': 'int32_t',
    'HANDLE': 'int32_t',
    'GEO_BOOL': 'bool'
}



class CythonConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    def render(self):
        if self.type == Type.STRING:
            return self.generator.parse_template('#define {{ constant.name }} "{{ constant.value }}"').render(constant=self)
        else:
            return self.generator.parse_template('#define {{ constant.name }} {{ constant.value }}').render(constant=self)

class CythonDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

class CythonParameter(Parameter):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def c_type(self):
        return self.generator.get_c_type(self.type, is_ref=self.is_ref, is_val=self.is_val)
    
    @property
    def cy_alloc(self):
        return "c{} = <char*>malloc({})".format(self.name, self.size_of_default, self.name)

    @property
    def cy_free(self):
        return "if c{}: free(c{})".format(self.name, self.name)

    @property
    def cy_type(self):
        if self.type == "void*": return "unsigned char*"
        elif self.type == "const void*": return "const unsigned char*"
        elif self.type in self.generator.classes:
            return "Wrap{}".format(self.type)
        else: return self.generator.get_c_type(self.type, is_val=True)

    @property
    def cy_declare(self):
        if self.type == Type.STRING:
            if self.is_ref:
                return "cdef char* c{} = NULL".format(self.name)
            else:
                return ''
        else:
            return 'cdef int32_t {} = {}'.format(self.name, self.utf8_default_length)
            

    @property
    def cy_assign(self):
        return "strcpy(c{}, {})".format(self.name, self.name)

    @property
    def cy_pass(self):
        if self.type == Type.STRING:
            if self.is_ref:
                return "c{}".format(self.name)
            else:
                return '{}'.format(self.name)
        elif self.is_val or (isinstance(self.type, str) and not self.type.find('*') == -1):
            return '{}'.format(self.name)
        elif self.type in self.generator.classes:
            return "&{}._handle".format(self.name)
        else:
            return '&{}'.format(self.name)

    @property
    def utf8_default_length(self):
        if self.default_length in self.generator.constants.keys():
            return '{}'.format(self.generator.constants[self.default_length].value)
        else:
            return '{}'.format(self.default_length)

    @property
    def size_of_default(self):
        if self.size_of_param:
            return self.parent.param_dict[self.size_of_param].utf8_default_length
        else:
            return "len({})+1".format(self.name)

    @property
    def is_ref_string(self):
        return self.type == Type.STRING and self.is_ref


    @property
    def is_ptr_type(self):
        return (self.type != Type.VOID and self.type != Type.DOUBLE and self.type != Type.INT32_T and 
                self.type != Type.INT16_T and self.type != Type.STRING and 
                not (self.type in type_map or self.type in self.generator.classes or self.type in self.generator.definitions))

            

class CythonMethod(Method):
    _ref_string_params = None
    def __init__(self, other):
        super().construct_copy(other)
        

    def render_c(self):
        return self.generator.parse_template("""
cdef extern {{ method.c_return_type }} {{ method.exposed_name }}{{ method.render_c_parameters() }}""").render(method=self)

    def render_wrapper(self):
        if self.is_destroy_method:
            return ""
        else:
            return self.generator.parse_template("""{% if method.is_static %}    @classmethod{% endif %}
    def {{ method.ext_method_name }}({{ method.wrap_first_parm }}{{ method.wrap_parameters }}):
{{ method.wrap_declare_c }}
        try:
{{ method.wrap_alloc }}
{{ method.wrap_assign_c }}
            {% if not method.returns_void %}_return_val = {% endif %}{% if method.returns_class %}Wrap{{ method.return_type }}(_geo, {% endif %}{{ method.exposed_name }}({{ method.passed_parameters }}){% if method.returns_class %}){% endif %}
            _raise_on_gx_errors(_geo.p_geo)
            {{ method.wrap_return }}
        finally:
{{ method.wrap_free }}
""").render(method=self)
    
    def render_c_parameters(self):
        return self.generator.parse_template("""(void*{% for param in parameters %}, {{ param.c_type }} {{ param.name }}{% endfor %});""").render(parameters=self.parameters)

    @property
    def ref_string_params(self):
        if not self._ref_string_params:
            self._ref_string_params = [p for p in self.parameters if p.is_ref_string]
        return self._ref_string_params

    @property
    def wrap_parameters(self):
        params = self.in_params if self.is_static else self.in_params[1:]
        return self.generator.parse_template("{% for param in params %}, {{ param.cy_type }} {{ param.name }}{% endfor %}").render(params=params)

    @property
    def passed_parameters(self):
        params = []
        if not self.is_static:
            params.append('&self._handle')
        elif len(self.parameters):
            params.append(self.parameters[0].cy_pass)
        params.extend([p.cy_pass for p in self.parameters[1:]]) 
        return self.generator.parse_template("_geo.p_geo{% for param in params %}, {{ param }}{% endfor %}").render(params=params)

    @property
    def wrap_declare_c(self):
        params = [p for p in self.parameters if p.name in self.size_of_params.keys()]
        params.extend(self.ref_string_params)
        if len(params):
            declarations = self.generator.parse_template("""{% for param in params %}        {{ param.cy_declare }}
{% endfor %}""").render(params=params)
        else:
            declarations = ''
        if self.is_static:
            return declarations
        else:
            return '        _geo = self._geo\n{}'.format(declarations)

    @property
    def wrap_assign_c(self):
        if len(self.ref_string_params):
            return self.generator.parse_template("""{% for param in params %}            {{ param.cy_assign }}
{% endfor %}""").render(params=self.ref_string_params)
        else:
            return ''

    @property
    def wrap_alloc(self):
        if len(self.ref_string_params):
            return self.generator.parse_template("""{% for param in params %}            {{ param.cy_alloc }}
{% endfor %}""").render(params=self.ref_string_params)
        else:
            return ''

    @property
    def wrap_free(self):
        if len(self.ref_string_params):
            return self.generator.parse_template("""{% for param in params %}            {{ param.cy_free }}
{% endfor %}""").render(params=self.ref_string_params)
        else:
            return '            pass'


    @property
    def wrap_return(self):
        return_values = [] if self.returns_void else [ '_return_val' ]
        return_values.extend(['c{}'.format(p.name) if p.is_ref_string else '{}'.format(p.name) for p in self.ref_params]) 
        if len(return_values) == 1:
            return 'return {}'.format(return_values[0])
        elif len(return_values) > 1:
            return 'return ({})'.format(', '.join(return_values))
        else:
            return ''

    @property
    def wrap_first_parm(self):
        return "cls, WrapPGeo _geo" if self.is_static else "self"

    @property
    def c_return_type(self):
        return self.generator.get_c_type(self.return_type, is_val=True)

    @property
    def returns_class(self):
        return self.return_type in self.generator.classes.keys()

class CythonClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def cdef_declarations(self):
        return self.generator.parse_template("""
{{- cl.header -}}
{{- cl.c_methods -}}
""").render(cl=self)

    @property
    def class_wrapper(self):
        if not self.has_methods:
            return ""
        else:
            return self.generator.parse_template("""

cdef class Wrap{{ cl.name }}:
    
{{ cl.init_dealloc }}

{{ cl.wrap_methods }}
    pass
""").render(cl=self)

    @property
    def init_dealloc(self):
        if self.is_static:
            return ""
        else:
            return self.generator.parse_template("""

    cdef int32_t _handle
    cdef WrapPGeo _geo;
    
    def __cinit__(self, WrapPGeo geo, int32_t handle):
        self._geo = geo
        self._handle = handle
    
    def __dealloc__(self):
        if self._handle != 0:
            {{ cl.default_destroy_method }}(self._geo.p_geo, &self._handle)
        self._geo = None

    @property
    def handle(self):
        return self._handle

""").render(cl=self)


    @property
    def header(self):
        return self.generator.parse_template("""
# Class {{ cl.name }}
""").render(cl=self)


    @property
    def c_methods(self):
        if len(self.method_groups) == 1:
            method_group = next(iter(self.method_groups.values()))
            return self.render_c_method_group(method_group)
        else:
            return self.generator.parse_template("""
{% for key, method_group in cl.method_groups.items() %}
# {{ key }}

{{ cl.render_c_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_c_method_group(self, method_group):
        return self.generator.parse_template("""
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
            return self.generator.parse_template("""
{% for key, method_group in cl.method_groups.items() %}
# {{ key }}

{{ cl.render_wrap_method_group(method_group) }}
{% endfor %}
""").render(cl=self)

    def render_wrap_method_group(self, method_group):
        return self.generator.parse_template("""
{% for method in methods %}
{{ method.render_wrapper() }}
{% endfor %}
""").render(methods=method_group)

class CythonCodeGenerator(CodeGeneratorBase):
    def __init__(self):
        super().__init__(constant_type=CythonConstant, define_type=CythonDefine, parameter_type=CythonParameter,
                         method_type=CythonMethod, class_type=CythonClass)
        self._remove_no_cpp_methods()

    def _remove_no_cpp_methods(self):
        for _, cl in self.classes.items():
            for g_k, methods in cl.method_groups.items():
                cl.method_groups[g_k] = [m for m in methods if not m.no_cpp]

    def get_c_type(self, type, is_val=False, is_ref=False):
        if isinstance(type, str):
            is_val = is_val or not type.find('*') == -1
        c_type = type
        if type == Type.STRING:
            if is_ref:
                return 'char*'
            else:
                return 'const char*'
        elif type == Type.VOID:
            c_type = "void"
        elif type == Type.DOUBLE:
            c_type = "double"
        elif type == Type.INT32_T:
            c_type = "int32_t"
        elif type == Type.INT16_T:
            c_type = "int16_t"
        elif type in type_map:
            c_type = type_map[type]
        elif type in self.classes or type in self.definitions:
            c_type = "int32_t"
        
        if is_ref:
            return '{}*'.format(c_type)
        elif is_val:
            return c_type
        else:
            return 'const {}*'.format(c_type)


    def render_pyx(self):
        return self.parse_template('''
#cython: language_level=3, c_string_type=unicode, c_string_encoding=utf8

from libc.stdint cimport uintptr_t, int32_t, int16_t
from libc.stdlib cimport malloc, free
from libc.string cimport strcpy, strcat, strncat, memset, memchr, memcmp, memcpy, memmove

from geosoft.gxapi import GXCancel, GXExit, GXAPIError, GXError

ctypedef Py_UNICODE WCHAR
ctypedef const WCHAR* LPCWSTR
ctypedef uintptr_t HWND
ctypedef uintptr_t HDC
cdef extern void* pCreate_GEO(const char*, const char*, int32_t, void*, int32_t, char*, int32_t);
cdef extern void Destroy_GEO(void *);
cdef extern void Destr_SYS(void*, const int32_t* p1);
cdef extern int32_t iCheckError_SYS(void*)
cdef extern int32_t iCheckTerminate_SYS(void*, int32_t* p1);
cdef extern int16_t sGetError_GEO(void*, char*, int32_t, char*, int32_t, int32_t*);
cdef extern HWND hGetMainWnd_GEO();
cdef extern HWND hGetActiveMainWnd_GEO();
cdef extern EnableApplicationWindows_GEO(bool);

{% for key, cl in classes.items() %}
{{ cl.cdef_declarations }}
{% endfor %}

cdef _raise_on_gx_errors(void* p_geo):
    cdef int32_t term
    cdef char* module
    cdef char* err
    cdef int32_t error_number
    cdef int32_t check_err
    if iCheckTerminate_SYS(p_geo, &term) > 0:
        check_err = iCheckError_SYS(p_geo)
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
                    raise GXAPIError(err);
                else:
                    raise GXError(err, module, error_number)
            finally:
                if module != NULL:
                    free(module)
                if err != NULL:
                    free(err)

cdef class WrapPGeo:
    cdef void* p_geo
    cdef bint destroy_p_geo
    
    def __cinit__(self):
        self.destroy_p_geo = False

    def _create(self, application, version, wind_id, flags):
        app = (<unicode>application).encode()
        ver = (<unicode>version).encode()
        cdef uintptr_t wind_handle = wind_id
        cdef void* hParentWnd = <void *>wind_handle
        cdef char* err = <char*>malloc(4096)
        try:
            self.p_geo = pCreate_GEO(app, ver, 0, hParentWnd, flags, err, 4096)
            if self.p_geo == NULL:
                raise GXAPIError(err)
            self.destroy_p_geo = True
            #print("WrapPGeo alloc")
        finally:
            free(err)

    def _create_internal(self, p_geo):
        self.p_geo = <void*><uintptr_t>p_geo
        
    def __dealloc__(self):
        if self.p_geo != NULL and self.destroy_p_geo:
            Destroy_GEO(self.p_geo)
            #print("WrapPGeo dealloc")

    cpdef uintptr_t _internal_p(self):
        return <uintptr_t>self.p_geo

    cpdef uintptr_t get_main_wnd(self):
        return <uintptr_t>hGetMainWnd_GEO()

    cpdef uintptr_t get_active_wnd(self):
        return <uintptr_t>hGetActiveMainWnd_GEO()

    def enable_application_windows(self, enable):
        EnableApplicationWindows_GEO(enable);
        
    cdef void* get_p_geo(self):
        return self.p_geo

    
{% for key, cl in classes.items() %}
{{ cl.class_wrapper }}
{% endfor %}

''').render(classes=self.classes)

if __name__ == "__main__":
    outputfile = 'gxapi_cy.pyx'
    gen = CythonCodeGenerator()
    gen.refresh_file_contents('gxapi_cy.pyx', gen.render_pyx())
