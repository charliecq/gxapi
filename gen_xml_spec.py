import os
import inspect
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
from datetime import datetime 
import pathlib


class XMLConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def def_value(self):
        if self.type == Type.STRING:
            return '"{}"'.format(self.value)
        else:
            return self.value

    @property
    def xml_type(self):
        if self.type == Type.DOUBLE:
            return "System.Double"
        elif self.type == Type.FLOAT:
            return "System.Single"
        elif self.type == Type.INT8_T:
            return "sbyte"
        elif self.type == Type.UINT8_T:
            return "byte"
        elif self.type == Type.INT16_T:
            return "System.Int16"
        elif self.type == Type.UINT16_T:
            return "System.UInt16"
        elif self.type == Type.INT32_T:
            return "System.Int32"
        elif self.type == Type.UINT32_T:
            return "System.UInt32"
        elif self.type == Type.INT64_T:
            return "System.Int64"
        elif self.type == Type.UINT64_T:
            return "System.UInt64"
        elif self.type == Type.STRING:
            return "System.String"
        else:
            return self.type


class XMLDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

    

def get_xml_type(type):
    if type == Type.VOID:
        return "void"
    elif type == Type.DOUBLE:
        return "real"
    elif type == Type.INT32_T or type == Type.BOOL:
        return "int"
    elif type == Type.STRING:
        return "string"
    else:
        return type


class XMLParameter(Parameter):
    _parameter_template = None
    _parameter_template_doc = None

    def __init__(self, other):
        super().construct_copy(other)

    @property
    def xml_type(self):
        if self.is_ref:
            return 'var {}'.format(get_xml_type(self.type))
        elif self.type == Type.INT32_T and self.is_val:
            return 'intval'
        else:
            return get_xml_type(self.type)

    def render_xml_doc(self, indent_spaces):
        if self.doc:
            if not XMLParameter._parameter_template_doc:
                XMLParameter._parameter_template_doc = self.generator.parse_template(
                    '{% set type_len = param.xml_type|length %}{{ param.doc | doc_sanitize | comment(comment_first_line=True) | indent(indent_spaces-type_len, True) | indent(indent_spaces+1) }}'
                    )
            return XMLParameter._parameter_template_doc.render(param=self, indent_spaces=indent_spaces)
        else:
            if not XMLParameter._parameter_template:
                XMLParameter._parameter_template = self.generator.parse_template(
                    '{% set type_len = param.xml_type|length %}{{ "//" | indent(indent_spaces-type_len, True) }}'
                    )
            return XMLParameter._parameter_template.render(param=self, indent_spaces=indent_spaces)


class XMLMethod(Method):
    _parameters_template = None

    def __init__(self, other):
        super().construct_copy(other)

    @property
    def string_macro(self):
        method_name = self.name
        param_replacements = {p.size_of_param: p.name for p in self.parameters if p.size_of_param}

        if len(param_replacements) > 0:
            if method_name.startswith('I') or method_name.startswith('_'):
                macro_name = method_name[1:]
            elif method_name.startswith('iI'):
                macro_name = 'i{}'.format(method_name[2:])
            elif method_name.startswith('Gt'):
                macro_name = 'Get{}'.format(method_name[2:])
            else:
                macro_name = '_{}'.format(method_name)
        
            macro_params = ''
            method_params = ''

            for param in self.parameters:
                if method_params:
                    method_params += ', '
                if param.name in param_replacements:
                    method_params += 'sizeof({})'.format(param_replacements[param.name])
                else:
                    if macro_params:
                        macro_params += ', '
                    macro_params += param.name
                    method_params += param.name
            return '#define {}({}) {}({})\n'.format(macro_name, macro_params, method_name, method_params)
        elif method_name.startswith('_'):
            return '#define {} {}\n'.format(method_name[1:], method_name)
        else:
            return ''

    def render_parameters(self):
        if not XMLMethod._parameters_template:
            XMLMethod._parameters_template = self.generator.parse_template("""{% for param in parameters %}{% if loop.first %}({% else %} {% endif %}{{ param.xml_type }}{% if not loop.last %}, {{ param.render_xml_doc(max_type_len + 2) }}
{% else %});{{ param.render_xml_doc(max_type_len + 2) }}{% endif %}{% else %}();{% endfor %}""")
        max_type_len = 0
        for param in self.parameters:
            max_type_len = max(max_type_len, len(param.xml_type))
        return XMLMethod._parameters_template.render(parameters=self.parameters, max_type_len=max_type_len)

    @property
    def xml_return_type(self):
        return get_xml_type(self.return_type)

    @property
    def availability_prefix(self):
        if self.availability == Availability.PUBLIC:
            prefix = 'public'
        elif self.availability == Availability.EXTENSION:
            prefix = 'extended'
        else:
            prefix = 'licensed'
        if self.is_app:
            prefix += '_app'
        return '_{}'.format(prefix)


class XMLClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

class XMLCodeGenerator(CodeGeneratorBase):
    def doc_sanitize(self, s):
        s = self.re_class.sub(r'\1', s)
        s = self.re_def.sub(lambda m: self._doc_sanitize_def(m.group(1)), s)
        s = self.re_func.sub(r'\1', s)
        s = self.re_def_val.sub(lambda m: self._doc_sanitize_def(m.group(1)), s)
        s = textwrap.dedent(s).strip()
        return s.replace('``', '')

    def _doc_sanitize_def(self, match):
        return r'&lt;define&gt;{}&lt;/define&gt;'.format(match)

    def __init__(self):
        cur_dir = os.path.dirname(os.path.join(os.getcwd(), inspect.getfile(self.__class__)))
        template_dirs = [ os.path.join(cur_dir, 'templates', 'xml') ]
        super().__init__(no_obsolete=False, constant_type=XMLConstant, define_type=XMLDefine, parameter_type=XMLParameter,
                         method_type=XMLMethod, class_type=XMLClass, template_dirs=template_dirs,
                         line_statement_prefix=r'//***')
        self.xml_outdir = os.path.join(cur_dir, '..', 'api', 'build', 'gx', 'spec')
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize

    def _regen_xml(self, cl):
        out_dir = os.path.join(self.xml_outdir, cl.branch)
        pathlib.Path(out_dir).mkdir(parents=True, exist_ok=True)
        xml_file = os.path.join(out_dir, '{}.geosoft_gx_class'.format(cl.name))
        template = self.get_template('class.geosoft_gx_class')       
        self.refresh_file_contents(xml_file, template.render(cl=cl))

    def _regen_classes(self):
        for cl in self.classes.values():
            self._regen_xml(cl)

    def generate(self):
        gen._regen_classes()

if __name__ == "__main__":
    gen = XMLCodeGenerator()
    gen.generate()
    
