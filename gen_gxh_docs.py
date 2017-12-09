import os
import inspect
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
from datetime import datetime 

class GXHConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def def_value(self):
        if self.type == Type.STRING:
            return '"{}"'.format(self.value)
        else:
            return self.value

class GXHDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)

    
def get_gxh_type(type):
    if type == Type.VOID:
        return "void"
    elif type == Type.DOUBLE:
        return "real"
    elif type == Type.INT32_T or type == Type.BOOL:
        return "int"
    elif type == Type.STRING:
        return "string"
    else:
        if '0' <= type[0] and type[0] <= '9':
            return "H" + type
        else:
            return type


class GXHParameter(Parameter):
    _parameter_template = None
    _parameter_template_doc = None

    def __init__(self, other):
        super().construct_copy(other)

    @property
    def gxh_type(self):
        if self.is_ref:
            return 'var {}'.format(get_gxh_type(self.type))
        else:
            return get_gxh_type(self.type)

    def render_gxh_doc(self, indent_spaces):
        if self.doc:
            if not GXHParameter._parameter_template_doc:
                GXHParameter._parameter_template_doc = self.generator.parse_template(
                    '{% set type_len = param.gxh_type|length %}{{ param.doc | doc_sanitize | comment(comment_first_line=True) | indent(indent_spaces-type_len, True) | indent(indent_spaces+1) }}'
                    )
            return GXHParameter._parameter_template_doc.render(param=self, indent_spaces=indent_spaces)
        else:
            if not GXHParameter._parameter_template:
                GXHParameter._parameter_template = self.generator.parse_template(
                    '{% set type_len = param.gxh_type|length %}{{ "//" | indent(indent_spaces-type_len, True) }}'
                    )
            return GXHParameter._parameter_template.render(param=self, indent_spaces=indent_spaces)


class GXHMethod(Method):
    _parameters_template = None

    def __init__(self, other):
        super().construct_copy(other)

    @property
    def string_macro(self):
        method_name = self.exposed_name
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
        else:
            return ''

    def render_parameters(self):
        if not GXHMethod._parameters_template:
            GXHMethod._parameters_template = self.generator.parse_template("""{% for param in parameters %}{% if loop.first %}({% else %} {% endif %}{{ param.gxh_type }}{% if not loop.last %}, {{ param.render_gxh_doc(max_type_len + 2) }}
{% else %});{{ param.render_gxh_doc(max_type_len + 2) }}{% endif %}{% else %}();{% endfor %}""")
        max_type_len = 0
        for param in self.parameters:
            max_type_len = max(max_type_len, len(param.gxh_type))
        return GXHMethod._parameters_template.render(parameters=self.parameters, max_type_len=max_type_len)

    @property
    def gxh_return_type(self):
        return get_gxh_type(self.return_type)

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
        return '[_{}]'.format(prefix)


class GXHClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

class GXHCodeGenerator(CodeGeneratorBase):
    def doc_sanitize(self, s):
        s = self.re_class.sub(r'\1', s)
        s = self.re_def.sub(r'\1', s)
        s = self.re_func.sub(r'\1', s)
        s = self.re_def_val.sub(r'\1', s)
        s = textwrap.dedent(s).strip()
        return s.replace('``', '')

    def __init__(self):
        cur_dir = os.path.dirname(os.path.join(os.getcwd(), inspect.getfile(self.__class__)))
        template_dirs = [ os.path.join(cur_dir, 'templates', 'gxc') ]
        super().__init__(constant_type=GXHConstant, define_type=GXHDefine, parameter_type=GXHParameter,
                         method_type=GXHMethod, class_type=GXHClass, template_dirs=template_dirs,
                         line_statement_prefix=r'<!--')
        self.gxc_outdir = os.path.join(cur_dir, '..', 'gxc')
        self.gxc_docs = os.path.join(self.gxc_outdir, 'docs')
        self._remove_no_gxh_classes_and_methods()
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize

    def _remove_no_gxh_classes_and_methods(self):
        classes_to_remove = [ key for key, cl in self.classes.items() if cl.no_gxh ]
        for key in classes_to_remove:
            self.classes.pop(key, None)
        for _, cl in self.classes.items():
            for g_k, methods in cl.method_groups.items():
                cl.method_groups[g_k] = [m for m in methods if not m.no_gxh]

    def _regen_all(self):
        # put GEOSOFT first it has defines needed in other headers
        classes = [ 'GEOSOFT' ]
        classes.extend([c for c in self.classes.keys() if not c == 'GEOSOFT'])
        self.regen_with_template(self.gxc_includes, 'all.gxh', classes=classes)

    def _regen_version(self):
        date = datetime.now().date()
        datestamp = '{}{}{}'.format(date.year, str(date.month).zfill(2), str(date.day).zfill(2))
        self.regen_with_template(self.gxc_includes, 'version.gxh', version=self.current_version, datestamp=datestamp)

    def _regen_md(self, cl):
        if not cl.name == 'GEO':
            md_file = os.path.join(self.gxc_docs, '{}.md'.format(cl.name))
            self.regen_with_editable_blocks('templates/gxc', 'class', 'md', md_file, md_file, cl=cl)
            
    def _regen_classes(self):
        for cl in self.classes.values():
            self._regen_md(cl)

    def generate(self):
        #gen._regen_version()
        #gen._regen_all()
        gen._regen_classes()

if __name__ == "__main__":
    gen = GXHCodeGenerator()
    gen.generate()
    
