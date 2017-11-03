import os, sys
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
import getopt
import inspect

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
    'HANDLE': 'int'
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
    @property
    def doc_name(self):
        name = self.name
        if name.startswith(self.parent.name):
            name = name.replace(self.parent.name + "_", "")
        parts = [w.lower() for w in name.split('_')]
        parts[0] = parts[0][0].upper() + parts[0][1:]
        return ' '.join(parts)

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


class PythonMethod(Method):
    _ref_string_params = None
    def __init__(self, other):
        super().construct_copy(other)
        max_param_name_len = max(len(p.name) for p in self.py_parameters) if len(self.py_parameters) else 0
        self._param_indent = max_param_name_len + 18
        self._return_indent_start = ' ' * max(0, self._param_indent - 21)
    
    def param_indent_start(self, param):
        return ' ' * max(0, self._param_indent - 18 - len(param.name))

    @property
    def return_indent_start(self):
        return self._return_indent_start

    @property
    def param_indent(self):
        return self._param_indent

    return_indent_start

    @property
    def call_wrapper(self):
        if self.is_static:
            return 'gxapi_cy.Wrap{}._{}'.format(self.parent.name, self.ext_method_name) 
        else:
            return 'self._{}'.format(self.ext_method_name)

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
            return "`{} <geosoft.gxapi.GX{}.{}>`".format(self.ext_method_name, self.parent.name, self.ext_method_name)
        else:
            return "`GX{}.{} <geosoft.gxapi.GX{}.{}>`".format(self.parent.name, self.ext_method_name, self.parent.name, self.ext_method_name)
    

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
        self.gxapi_docs_outdir = os.path.join(cur_dir, '..', 'gxpy', 'docs')
        template_dirs = [ os.path.join(cur_dir, 'templates', 'gxpy') ]
        super().__init__(constant_type=PythonConstant, define_type=PythonDefine, parameter_type=PythonParameter,
                         method_type=PythonMethod, class_type=PythonClass, template_dirs=template_dirs)
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize
        self._remove_no_cpp_methods()

    def doc_sanitize(self, s, ref_class):
        s = self.re_class.sub(r'`GX\1 <geosoft.gxapi.GX\1>`', s)
        s = self.re_def.sub(lambda m: self._doc_sanitize_def(m.group(1)), s)
        s = self.re_func.sub(lambda m: self.methods[m.group(1)].py_doc_ref(ref_class), s)
        s = self.re_def_val.sub(lambda m: self._doc_sanitize_def_val(m.group(1)), s)
        s = textwrap.dedent(s).strip()
        return s.replace('\\', '\\\\')

    def _doc_sanitize_def(self, match):
        return r':ref:`{}`'.format(match)

    def _doc_sanitize_def_val(self, match):
        if match == 'GS_TRUE':
            return '``True``'
        elif match == 'GS_FALSE':
            return '``False``'
        else:
            return r'`{} <geosoft.gxapi.{}>`'.format(match, match)

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
        elif type == Type.BOOL:
            py_type = "bool"
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

    def _regen_init(self):
        output_file = os.path.join(self.gxapi_outdir, '__init__.py')
        self.regen_with_editable_blocks('templates/gxpy', 'init', 'py', output_file, classes=self.classes)

    def _regen_python_code(self, cl):
        if not cl.no_cpp and not cl.name == 'GEO':
            py_file = os.path.join(self.gxapi_outdir, 'GX{}.py'.format(cl.name))
            self.regen_with_editable_blocks('templates/gxpy', 'class', 'py', py_file, cl=cl)

    def _regen_rst(self, cl):
        if (not cl.no_cpp and not cl.name == 'GEO') or cl.name == 'GEOSOFT':
            rst_file = os.path.join(self.gxapi_docs_outdir, 'GX{}.rst'.format(cl.name))
            rst_template = self.get_template("class_generated.rst")
            self.refresh_file_contents(rst_file, rst_template.render(cl=cl))
            
    def _regen_classes(self):
        for cl in self.classes.values():
            self._regen_python_code(cl)
            self._regen_rst(cl)
            
    def generate(self):
        gen._regen_init()
        gen._regen_classes()


if __name__ == "__main__":
    gen = PythonCodeGenerator()
    gen.generate()
    
