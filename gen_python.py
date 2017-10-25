import os, sys
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
import getopt
import inspect
from shutil import copyfile

type_map = {
    'HDC': 'int',
    'HWND': 'int',
    'CRC': 'int',
    'WND': 'int',
    'PTMP': 'int',
    'FILTER': 'int',
    'DGW_OBJ': 'int',
    'TB_FIELD': 'int',
    'DB_SELECT': 'int',
    'DB_SYMB': 'int',
    'META_TOKEN': 'int',
    'HANDLE': 'int',
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
    def py_type(self):
        return self.generator.get_py_type(self.type, is_val=self.is_val, is_ref=self.is_ref)

    @property
    def py_type_hint(self):
        if self.is_class:
            return "'{}'".format(self.py_type)
        else:
            return self.py_type

    @property
    def is_class(self):
        return self.type in self.generator.classes.keys()

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
        

    @property
    def call_wrapper(self):
        if self.is_static:
            return 'gxapi_cy.Wrap{}.{}'.format(self.parent.name, self.ext_method_name) 
        else:
            return 'self._wrapper.{}'.format(self.ext_method_name)

    @property
    def py_return(self):
        if self.returns_void:
            return ''
        elif self.returns_class:
            return "return {}(ret_val)".format(self.py_return_type)
        else:
            return "return ret_val"

    def py_doc_ref(self, ref_class):
        if ref_class == self.parent.name:
            return "`{}`".format(self.ext_method_name)
        else:
            return "`GX{}.{}`".format(self.parent.name, self.ext_method_name)
    

    @property
    def assign_return_values(self):
        return_values = []
        if not self.returns_void:
            return_values.append('ret_val')
        return_values.extend(['{}.value'.format(p.name) for p in self.ref_params])
        if not return_values:
            return ''
        else:
            return '{} = '.format(', '.join(return_values))

    @property
    def pass_py_parameters(self):
        parameters = []
        if self.is_static:
            parameters.append('GXContext._get_tls_geo()')
        passed_params = self.in_params if self.is_static else self.in_params[1:]
        for p in passed_params:
            if p.type == Type.STRING:
                if p.is_ref:
                    parameters.append("{}.value.encode()".format(p.name))
                else:
                    parameters.append("{}.encode()".format(p.name))
            else:
                if p.is_ref:
                    parameters.append("{}.value".format(p.name))
                elif p.type in self.generator.classes:
                    parameters.append("{}._wrapper".format(p.name))
                else:
                    parameters.append(p.name)
        if not parameters:
            return ''
        else:
            return '{}'.format(', '.join(parameters))

    @property
    def ref_string_params(self):
        if not self._ref_string_params:
            self._ref_string_params = [p for p in self.parameters if p.is_ref_string]
        return self._ref_string_params

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
    def return_hint(self):
        if self.returns_class:
            return "'{}'".format(self.py_return_type)
        else:
            return self.py_return_type

    @property
    def py_first_parm(self):
        return "cls" if self.is_static else "self"

    @property
    def py_parameters(self):
        return self.in_params if self.is_static else self.in_params[1:]

    @property
    def py_return_type(self):
        return self.generator.get_py_type(self.return_type, is_val=True)

    @property
    def returns_class(self):
        return self.return_type in self.generator.classes.keys()

class PythonClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def gxapi_imports(self):
        imports = set()
        for _, group_methods in self.method_groups.items():
            imports |= set([m.py_return_type for m in group_methods if m.returns_class and not m.return_type == self.name])
            #for m in group_methods:
            #    imports |= set([p.py_type for p in m.parameters if p.is_class and not p.type == self.name])
        imports = list(imports)
        imports.sort()
        return imports

    @property
    def gxapi_imports_typing(self):
        gxapi_imports = set(self.gxapi_imports)
        imports = set()
        for _, group_methods in self.method_groups.items():
            for m in group_methods:
                imports |= set([p.py_type for p in m.parameters if p.is_class and not p.type == self.name]) - gxapi_imports
        imports = list(imports)
        imports.sort()
        return imports
        #return "\r\n".join(["from .{} import {}".format(i, i) for i in imports])

class PythonCodeGenerator(CodeGeneratorBase):
    def __init__(self):
        cur_dir = os.path.dirname(os.path.join(os.getcwd(), inspect.getfile(self.__class__)))
        self.gxapi_outdir = os.path.join(cur_dir, '..', 'gxpy', 'geosoft', 'gxapi')
        template_dirs = [ os.path.join(cur_dir, 'templates') ]
        super().__init__(constant_type=PythonConstant, define_type=PythonDefine, parameter_type=PythonParameter,
                         method_type=PythonMethod, class_type=PythonClass, template_dirs=template_dirs)
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize
        self._remove_no_cpp_methods()

    def doc_sanitize(self, s, ref_class):
        s = self.re_class.sub(r'`GX\1`', s)
        s = self.re_def.sub(r'`\1`', s)
        s = self.re_func.sub(lambda m: self.methods[m.group(1)].py_doc_ref(ref_class), s)
        s = self.re_def_val.sub(r'`\1`', s)
        s = textwrap.dedent(s).strip()
        return s.replace('\\', '\\\\')

    def _remove_no_cpp_methods(self):
        for _, cl in self.classes.items():
            for g_k, methods in cl.method_groups.items():
                cl.method_groups[g_k] = [m for m in methods if not m.no_cpp]

    def get_py_type(self, type, is_val=False, is_ref=False):
        if isinstance(type, str):
            is_val = is_val or not type.find('*') == -1
        py_type = type

        if type == "void*" or type == "const void*":
            py_type = 'bytearray'
        elif type == Type.STRING:
            py_type = 'str'
        elif type == Type.VOID:
            py_type = "None"
        elif type == Type.DOUBLE:
            py_type = "float"
        elif type == Type.INT32_T:
            py_type = "int"
        elif type == Type.INT16_T:
            py_type = "int"
        elif type in type_map:
            py_type = type_map[type]
        elif type in self.definitions:
            py_type = "int"
        elif type in self.classes:
            py_type = "GX{}".format(py_type)
        
        if is_ref:
            return '{}_ref'.format(py_type)
        else:
            return py_type

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
        self.refresh_file_contents(generated_gen_template, gen_template.render(**kwargs))

        final_template = self.get_template(os.path.split(generated_gen_template)[1])
        self.refresh_file_contents(output_file, final_template.render(**kwargs))

    def regen_init(self):
        output_file = os.path.join(self.gxapi_outdir, '__init__.py')
        self._regen_py('init', output_file, classes=self.classes)

    def regen_classes(self):
        for key, cl in self.classes.items():
            if not cl.no_cpp and not key == 'GEO':
                output_file = os.path.join(self.gxapi_outdir, 'GX{}.py'.format(key))
                self._regen_py('class', output_file, cl=cl)

    def generate(self):
        gen.regen_init()
        gen.regen_classes()


if __name__ == "__main__":
    gen = PythonCodeGenerator()
    gen.generate()
    
