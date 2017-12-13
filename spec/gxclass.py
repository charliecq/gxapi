import functools
import re
from collections import namedtuple, OrderedDict, Hashable

from .gxdefs import SpecBase

def _convert_camel_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
    if s2.endswith("3_d"):
        s2 = s2[:-3] + "_3d"
    if s2.endswith("2_d"):
        s2 = s2[:-3] + "_2d"
    s2 = s2.replace("3_d_", "_3d_").replace("2_d_", "_2d_")
    if s2.endswith("3_dv"):
        s2 = s2[:-4] + "_3dv"
    s2 = s2.replace("_h3_dn", "_3dn")
    s2 = s2.replace("3_dgui", "_3d_gui")    
    return s2


class Class(SpecBase):
    def __init__(self, name, doc=None, notes=None, see_also=None, 
                 handle_name=None, no_gxh=False, no_csharp=False, no_cpp=False,
                 next_gen=False):
        super().__init__(name)
        self.name = name
        self.next_gen = next_gen
        self.handle_name = handle_name
        self.no_gxh = no_gxh or next_gen
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        self.doc = doc
        self.notes = notes
        self.is_static = True
        self.default_destroy_method = "Destr_SYS"
        self.has_methods = False
        self.see_also = see_also
        self.branch = ''
        self.method_groups = {}
        self.defines = {}

    def validate(self):
        if not self.doc:
            raise RuntimeError('Undocumented class {}'.format(self))
        for _, method_group in self.method_groups.items():
            for method in method_group:
                method.validate()


    def _ext_method_name_camel(self, method):
        if method.name == "iCheckError_SYS":
            return "iCheckError"
        method_postfix = "_" + self.name
        method_name = method.external_name
        if method.name.endswith(method_postfix):
            method_name = method_name[0 : len(method_name) - len(method_postfix)]
        if method_name.startswith("_") or (method_name.startswith("I") and len(method_name) > 2 and (method_name[1] == 'i' or (method_name[1] >= 'A' and method_name[1] <= 'Z'))):
            return method_name[1:]
        return method_name

    def _ext_method_name_no_camel(self, method):
        return _convert_camel_case(self._ext_method_name_camel(method))

    def _ext_method_name_real_to_double(self, method):
        return self._ext_method_name_no_camel((method)).replace("_real", "_double")

    def _ext_method_name_no_polish(self, method):
        method_name = self._ext_method_name_real_to_double(method)
        if method_name.startswith("i_") or method_name.startswith("r_"):
        	return method_name[2:]
        else:
        	return method_name

    def _ext_method_name(self, method):
        method_name = self._ext_method_name_no_polish(method)
        
        if method.cpp_post:
            method_name = method_name + method.cpp_post
        
        # Stops keyword and macro collisions
        if (self.name == "MATH" or method_name == 'char' or method_name == 'assert' or 
            method_name == 'exit' or method_name == 'cancel' or method_name == 'global' or 
            method_name == 'print' ):
            return '{}_'.format(method_name)
        else:
            return method_name