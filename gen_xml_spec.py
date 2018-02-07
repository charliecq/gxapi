import os
import inspect
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
from datetime import datetime 
import pathlib
import argparse
from xml.sax.saxutils import escape

class XMLConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

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
        if self.is_null_handle:
            type = self.name.replace("_NULL", "")
            nullconst = Constant(name=self.name, type=type, value='(({})0)'.format(type))
            self.constants.append(XMLConstant(nullconst))
    

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
    def attributes(self):
        attrs = ' type="{}"'.format(self.xml_type)
        if self.size_of_param:
            parameters = enumerate(self.parent.parameters)
            index, size_param = next((i, p) for i, p in parameters if p.name == self.size_of_param)
            attrs = attrs + ' size_of_param="{}"'.format(index)
            if size_param.type == Type.INT32_T and size_param.is_val:
                attrs = attrs + ' size_of_param_intval="true"'
        if self.default_length:
            attrs = attrs + ' defaultlength="{}"'.format(self.default_length)
        return attrs

    @property
    def xml_type(self):
        if self.is_ref:
            return 'var {}'.format(get_xml_type(self.type))
        elif self.type == Type.INT32_T and self.is_val:
            return 'intval'
        else:
            return get_xml_type(self.type)

class XMLMethod(Method):
    _parameters_template = None

    def __init__(self, other):
        super().construct_copy(other)

    @property
    def xml_return_type(self):
        return get_xml_type(self.return_type)

    @property
    def attributes(self):
        attrs = ' name="{}"'.format(self.name)
        if not self.external_name == self.name:
            attrs = attrs + ' externalname="{}"'.format(self.external_name)
        if not self.is_app:
            attrs = attrs + ' module="{}"'.format(self.module)
        attrs = attrs + ' license="{}" available="{}"'.format(self.availability_prefix, self.version)
        if self.is_gui:
            attrs = attrs + ' guicall="true"'
        if self.no_gxh:
            attrs = attrs + ' nogxh="true"'
        if self.no_csharp:
            attrs = attrs + ' nocsharp="true"'
        if self.no_cpp:
            attrs = attrs + ' nocpp="true"'
        if self.cpp_post:
            attrs = attrs + ' cpp_post="{}"'.format(self.cpp_post)
        if self.is_obsolete:
            attrs = attrs + ' obsolete="true"'
        return attrs

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
        s = self.re_const.sub(lambda m: self._doc_sanitize_def(m.group(1)), s)
        s = textwrap.dedent(s).strip()
        return escape(s.replace('``', ''))

    def _doc_sanitize_def(self, match):
        return r'&lt;define&gt;{}&lt;/define&gt;'.format(match)

    def __init__(self, xml_outdir):
        cur_dir = os.path.dirname(os.path.join(os.getcwd(), inspect.getfile(self.__class__)))
        template_dirs = [ os.path.join(cur_dir, 'templates', 'xml') ]
        super().__init__(no_obsolete=False, constant_type=XMLConstant, define_type=XMLDefine, parameter_type=XMLParameter,
                         method_type=XMLMethod, class_type=XMLClass, template_dirs=template_dirs,
                         line_statement_prefix=r'//***')
        self.xml_outdir = os.path.join(cur_dir, '..', '..', 'api', 'gx')
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize
        for branch in self.branches:
            self.delete_gen_files_with_no_class(os.path.join(self.xml_outdir, branch), 'geosoft_gx_class')

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
    parser = argparse.ArgumentParser(description='Generate legacy GX API XML spec for legacy tools.')
    parser.add_argument('output_dir', type=str, 
                        help='Output directory')
    args = parser.parse_args()
    gen = XMLCodeGenerator(args.output_dir)
    gen.generate()
    
