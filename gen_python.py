import os, sys
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
import getopt
import inspect
from shutil import copyfile

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



class PythonConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def python_value(self):
        val = self.value
        if self.value in self.generator.constants.keys():
            val = self.generator.constants[val].python_value
        if self.type == Type.STRING:
            return '\"{}\"'.format(val)
        else:
            last_char = val[-1]
            if 'U' == last_char or 'f' == last_char or 'L' == last_char:
                return val[:-1]
            else:
                return val

class PythonDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

class PythonParameter(Parameter):
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
            return "&{}.handle".format(self.name)
        else:
            return '&{}'.format(self.name)

    @property
    def utf8_default_length(self):
        if self.default_length in self.generator.constants.keys():
            return '4*{}'.format(self.generator.constants[self.default_length].value)
        else:
            return '4*{}'.format(self.default_length)

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

            

class PythonMethod(Method):
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
            {% if not method.returns_void %}_return_val = {% endif %}{% if method.returns_class %}Wrap{{ method.return_type }}({% endif %}{{ method.exposed_name }}({{ method.passed_parameters }}){% if method.returns_class %}){% endif %}
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
            params.append('&self.handle')
        elif len(self.parameters):
            params.append(self.parameters[0].cy_pass)
        params.extend([p.cy_pass for p in self.parameters[1:]]) 
        return self.generator.parse_template("get_p_geo(){% for param in params %}, {{ param }}{% endfor %}").render(params=params)

    @property
    def wrap_declare_c(self):
        params = [p for p in self.parameters if p.name in self.size_of_params.keys()]
        params.extend(self.ref_string_params)
        if len(params):
            return self.generator.parse_template("""{% for param in params %}        {{ param.cy_declare }}
{% endfor %}""").render(params=params)
        else:
            return ''

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
        return "cls" if self.is_static else "self"

    @property
    def c_return_type(self):
        return self.generator.get_c_type(self.return_type, is_val=True)

    @property
    def returns_class(self):
        return self.return_type in self.generator.classes.keys()

class PythonClass(Class):
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

    cdef int32_t handle
    
    def __cinit__(self, handle):
        self.handle = handle
        
    def __dealloc__(self):
        if self.handle != 0:
            {{ cl.default_destroy_method }}(get_p_geo(), &self.handle)

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

class PythonCodeGenerator(CodeGeneratorBase):
    def __init__(self):
        cur_dir = os.path.dirname(os.path.join(os.getcwd(), inspect.getfile(self.__class__)))
        self.gxapi_outdir = os.path.join(cur_dir, '..', 'gxpy', 'geosoft', 'gxapi')
        template_dirs = [ os.path.join(cur_dir, 'templates') ]
        super().__init__(constant_type=PythonConstant, define_type=PythonDefine, parameter_type=PythonParameter,
                         method_type=PythonMethod, class_type=PythonClass, template_dirs=template_dirs)
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

    def _regen_py(self, template_prefix, output_file, **kwargs):
        empty_template = 'templates/{}_empty.py'.format(template_prefix)
        cur_gen_template = 'templates/{}_cur.gen.py'.format(template_prefix)
        generated_template_name = '{}_generated.py'.format(template_prefix)
        generated_gen_template = 'templates/{}_generated.gen.py'.format(template_prefix)

        if not os.path.exists(output_file):
            copyfile(empty_template, cur_gen_template)
        else:
            copyfile(output_file, cur_gen_template)
        
        gen_template = self.get_template(generated_template_name)
        with open(generated_gen_template, 'wb') as f:
            f.write(gen_template.render(**kwargs).encode('UTF-8'))

        final_template = self.get_template(os.path.split(generated_gen_template)[1])
        with open(output_file, 'wb') as f:
            f.write(final_template.render(**kwargs).encode('UTF-8'))

    def regen_init(self):
        output_file = os.path.join(self.gxapi_outdir, '__init__.py')
        self._regen_py('init', output_file, classes=self.classes)

    def regen_classes(self):
        for key, cl in self.classes.items():
            if not cl.no_cpp:
                output_file = os.path.join(self.gxapi_outdir, 'GX{}.py'.format(key))
                self._regen_py('class', output_file, cl=cl)

    def generate(self):
        gen.regen_init()
        gen.regen_classes()


if __name__ == "__main__":
    gen = PythonCodeGenerator()
    gen.generate()
    
