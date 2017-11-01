import functools
import re
from collections import namedtuple, OrderedDict, Hashable

from .gxdefs import SpecBase

def convert_camel_case(name):
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


class memoized(object):
	'''Decorator. Caches a function's return value each time it is called.
	If called later with the same arguments, the cached value is returned
	(not reevaluated).
	'''
	def __init__(self, func):
	   self.func = func
	   self.cache = {}
	def __call__(self, *args):
		if not isinstance(args, Hashable): 
			# uncacheable.  a list, for instance.
			# better to not cache than blow up.
			return self.func(*args)
		if args in self.cache:
			return self.cache[args]
		else:
			value = self.func(*args)
			self.cache[args] = value
			return value
	def __repr__(self):
		'''Return the function's docstring.'''
		return self.func.__doc__
	def __get__(self, obj, objtype):
		'''Support instance methods.'''
		return functools.partial(self.__call__, obj)

class Class(SpecBase):
    def __init__(self, name, handle_name=None, no_gxh=False, no_csharp=False, no_cpp=False,
                 doc=None, notes=None):
        super().__init__()

        self.name = name
        self.handle_name = handle_name
        self.no_gxh = no_gxh
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        self.doc = doc
        self.notes = notes
        self.is_static = True
        self.default_destroy_method = "Destr_SYS"
        self.has_methods = False


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
        return convert_camel_case(self._ext_method_name_camel(method))

    def _ext_method_name_real_to_double(self, method):
        return self._ext_method_name_no_camel((method)).replace("_real", "_double")

    def _ext_method_name_no_polish(self, method):
        method_name = self._ext_method_name_real_to_double(method)
        if method_name.startswith("i_") or method_name.startswith("r_"):
        	return method_name[2:]
        else:
        	return method_name

    @memoized
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