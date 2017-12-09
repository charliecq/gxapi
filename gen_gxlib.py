import os
import inspect
from gen import CodeGeneratorBase
from spec import Type, Availability, Constant, Define, Parameter, Method, Class
import textwrap
from datetime import datetime 

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
}

class GXLIBConstant(Constant):
    def __init__(self, other):
        super().construct_copy(other)

    @property
    def def_value(self):
        if self.type == Type.STRING:
            return '"{}"'.format(self.value)
        else:
            return self.value

class GXLIBDefine(Define):
    def __init__(self, other):
        super().construct_copy(other)


class GXLIBParameter(Parameter):
    _parameter_template = None
    _parameter_template_doc = None

    def __init__(self, other):
        super().construct_copy(other)

    @property
    def c_type(self):
        return self.generator.get_c_type(self.type, is_ref=self.is_ref, is_val=self.is_val)

    @property
    def doxy_param(self):
        return '@param{} {}'.format('[out]' if self.is_ref else '[in] ', self.name)
            
    
class GXLIBMethod(Method):
    _parameters_template = None

    def __init__(self, other):
        super().construct_copy(other)
        param_name_lengths = [ 4 ] # p_geo
        param_name_lengths.extend(len(p.name) for p in self.parameters)
        self._param_doc_indent = max(param_name_lengths) + 16
    
    @property
    def param_doc_indent(self):
        return self._param_doc_indent 

    @property
    def c_return_type(self):
        return self.generator.get_c_type(self.return_type, is_val=True)


class GXLIBClass(Class):
    def __init__(self, other):
        super().construct_copy(other)

class GXLIBCodeGenerator(CodeGeneratorBase):
    def doc_sanitize(self, s):
        s = self.re_class.sub(r'\1', s)
        s = self.re_def.sub(r'\1', s)
        s = self.re_func.sub(r'\1', s)
        s = self.re_def_val.sub(r'\1', s)
        s = textwrap.dedent(s).strip()
        return s.replace('``', '')

    def __init__(self):
        cur_dir = os.path.dirname(os.path.join(os.getcwd(), inspect.getfile(self.__class__)))
        template_dirs = [ os.path.join(cur_dir, 'templates', 'gxcore') ]
        super().__init__(constant_type=GXLIBConstant, define_type=GXLIBDefine, parameter_type=GXLIBParameter,
                         method_type=GXLIBMethod, class_type=GXLIBClass, template_dirs=template_dirs,
                         line_statement_prefix=r'//***')
        self.gxcore_outdir = os.path.join(cur_dir, '..', 'gxcore')
        self.gxcore_includes = os.path.join(self.gxcore_outdir, 'include')
        self.j2env.filters['doc_sanitize'] = self.doc_sanitize

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
        elif type == Type.INT32_T or type == Type.BOOL:
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

    def _regen_all(self):
        # put GEOSOFT first it has defines needed in other headers
        classes = [ 'GEOSOFT' ]
        classes.extend([c for c in self.classes.keys() if not c == 'GEOSOFT'])
        self.regen_with_template(self.gxcore_includes, 'all.gxlib', classes=classes)

    def _regen_gxlib(self, cl):
        h_file = os.path.join(self.gxcore_includes, 'gxlib', '{}_gxlib.h'.format(cl.name.lower()))
        self.regen_with_editable_blocks('templates/gxcore', 'gxlib', 'h', h_file, h_file, 
                                        cl=cl, date=self.generation_time)

    def _regen_classes(self):
        for cl in self.classes.values():
            self._regen_gxlib(cl)

    def generate(self):
        #gen._regen_all()
        gen._regen_classes()

if __name__ == "__main__":
    gen = GXLIBCodeGenerator()
    gen.generate()
    
