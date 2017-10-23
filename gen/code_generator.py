import importlib
import glob
import os
import re
import copy
import itertools
import inspect
from jinja2 import Environment, StrictUndefined, FileSystemLoader

from spec import Type, Availability, Constant, Parameter, Method, Define, Class

# Generate global dictionaries and sets of everything with their methods and definitions
# only once per process execution for efficiency

_core_files = [
    'E:\\ggit\\t\\gxapi\spec\\core\\GEOSOFT.py',
    'E:\\ggit\\t\\gxapi\\spec\\core\\3DN.py', 
    'E:\\ggit\\t\\gxapi\\spec\\core\\VV.py', 
    #'E:\\ggit\\t\\gxapi\spec\\core\\GEO.py',
    ]
_desk_files = []

_core_files = glob.glob(os.path.join(os.path.dirname(__file__), '../spec/core/*.py'))
_desk_files = glob.glob(os.path.join(os.path.dirname(__file__), '../spec/desk/*.py'))

_classes = {}
_class_method_groups = {}
_class_defines = {}

for file in itertools.chain(_core_files, _desk_files):
    parts = file.replace('/', '.').replace('\\', '.').split('.')
    parts.pop()
    gx_cl = parts.pop()
    branch = parts.pop()
    mod = importlib.import_module('spec.{}.{}'.format(branch, gx_cl), __package__)

    _classes[gx_cl] = mod.gx_class

    defines = mod.gx_defines if hasattr(mod, 'gx_defines') else []
    _class_defines[gx_cl] = defines

    groups = mod.gx_methods if hasattr(mod, 'gx_methods') else {}

    _class_method_groups[gx_cl] = groups

def do_comment(s, prefix='// ', comment_first_line=False, extra_spaces=0):
    if extra_spaces > 0:
        prefix += u' ' * extra_spaces
    rv = (u'\n' + prefix).join(s.splitlines())
    if comment_first_line:
        rv = prefix + rv
    return rv


def _opt_derive(instance, derive_type):
    return derive_type(instance) if derive_type else copy.deepcopy(instance)


class CodeGeneratorBase:
    # This class provide a set of dicts from an API spec that is perfectly suited for
    # code generation. The circular references from children to parents are intentional
    # and allows resolution of any pertinent information where only the child object is
    # available.
    def __init__(self, *, constant_type=None, define_type=None, parameter_type=None,
                 method_type=None, class_type=None, no_obsolete=True, template_dirs = []):
        self.classes = {}
        self.methods = {}
        self.constants = {}
        self.definitions = {}
        
        loader = FileSystemLoader(template_dirs) if len(template_dirs) else None
        self.j2env = Environment(loader=loader, line_statement_prefix='###')
        self.j2env.filters['comment'] = do_comment
        self.j2env.undefined = StrictUndefined

        # Some regular expressions to sanitize documentation
        self.re_class = re.compile(':class:`(.*?)`')
        self.re_def = re.compile(':def:`(.*?)`')
        self.re_func = re.compile(':func:`(.*?)`')
        self.re_def_val = re.compile(':def_val:`(.*?)`')

        for c_name, c in _classes.items():
            cl = _opt_derive(c, class_type)
            cl.generator = self
            cl.defines = {}
            cl.method_groups = {}

            # defintions
            for d in _class_defines[c_name]:
                define = _opt_derive(d, define_type)
                define.parent = cl
                define.generator = self

                # constants within definition
                gen_constants = []
                for const in define.constants:
                    gen_const = _opt_derive(const, constant_type)
                    gen_const.parent = define
                    gen_const.generator = self
                    gen_constants.append(gen_const)
                    self.constants[gen_const.name] = gen_const
                define.constants = gen_constants
                cl.defines[d.name] = define
                self.definitions[d.name] = define

            cl.is_static = True
            cl.has_methods = False
            default_destr_name = 'Destroy_{}'.format(cl.name)
            default_destrex_name = 'DestroyEx_{}'.format(cl.name)


            # method groups
            for g_k, g in _class_method_groups[c_name].items():
                # methods within each group
                methods = []
                for m in g:
                    if not no_obsolete or not m.is_obsolete:
                        method = _opt_derive(m, method_type)
                        method.parent = cl
                        method.generator = self


                        # parameters within method
                        parameters = []
                        for p in m.parameters:
                            parameter = _opt_derive(p, parameter_type)
                            parameter.parent = method
                            parameter.generator = self
                            parameters.append(parameter)
                        method.parameters = parameters
                        method.is_static = len(parameters) == 0 or not parameters[0].type == cl.name
                        if not method.is_static:
                            cl.is_static = False

                        method.is_destroy_method = method.name == default_destr_name or method.name == default_destrex_name

                        if cl.name == 'BF':
                            # We only use the DestroyEx in BF
                            if method.name == default_destrex_name:
                                cl.default_destroy_method = default_destrex_name
                        elif method.name == default_destr_name:
                            if method.is_app:
                                cl.default_destroy_method = 'App_{}'.format(default_destr_name)
                            else:
                                cl.default_destroy_method = default_destr_name

                        cl.has_methods = True
                        methods.append(method)
                        self.methods[method.name] = method
                if len(methods) > 0:
                    cl.method_groups[g_k] = methods
            self.classes[c_name] = cl

    def parse_template(self, source, globals=None, template_class=None):
        return self.j2env.from_string(source, globals=globals, template_class=template_class)

    def get_template(self, name, parent=None, globals=None):
        return self.j2env.get_template(name, parent=parent, globals=globals)

    def refresh_file_contents(self, file_name, contents):
        cur_contents = None
        if os.path.exists(file_name):
            with open(file_name, 'r') as f:
                cur_contents = f.read()
        if contents != cur_contents:
            with open(file_name, 'wb') as f:
                f.write(contents.encode('UTF-8'))

    

