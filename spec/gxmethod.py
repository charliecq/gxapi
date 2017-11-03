from .gxdefs import Type, Availability, SpecBase
from distutils.version import StrictVersion

class Parameter(SpecBase):
    def __init__(self, name, type=Type.UNKNOWN, is_ref=False, is_val=False,
                 size_of_param=None, default_length=None, doc=None):
        super().__init__()

        self.name = name
        self.type = type
        self.is_ref = is_ref
        self.is_val = is_val
        self.size_of_param = size_of_param
        self.default_length = default_length
        self.doc = doc


class Method(SpecBase):
    _parameters = None

    def __init__(self, name, module=None, version=None, cpp_post=None, external_name=None, availability=Availability.UNKNOWN,
                 is_obsolete=False, is_app=False, is_gui=False, no_gxh=False, no_csharp=False, no_cpp=False,
                 return_type=Type.UNKNOWN, return_doc=None,
                 doc=None, notes=None, see_also=None, parameters=[]):
        super().__init__()

        self.name = name
        self.module = module
        self.version = StrictVersion(version)
        self.cpp_post = cpp_post
        self.external_name = external_name if external_name else self.name
        self.availability = availability
        self.is_obsolete = is_obsolete
        self.is_app = is_app
        self.is_gui = is_gui
        self.no_gxh = no_gxh
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        self.return_type = return_type
        self.return_doc = return_doc
        self.doc = doc
        self.notes = notes
        self.see_also = see_also
        self.parameters = parameters
        self.is_static = True
        self.is_destroy_method = False
        
        self.exposed_name = external_name if external_name else 'App_{}'.format(self.name) if self.is_app else self.name
        

    @property
    def parameters(self):
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        self._parameters = value        
    
        self.param_dict = { p.name : p for p in self._parameters }
        self.size_of_params = { p.size_of_param: p.name for p in self._parameters if p.size_of_param }
        self.in_params = [ p for p in self._parameters if not p.name in self.size_of_params.keys() ]
        self.ref_params = [ p for p in self._parameters if p.is_ref ]

    @property
    def returns_void(self):
        return self.return_type == Type.VOID

    @property
    def returns_void(self):
        return self.return_type == Type.VOID

    @property
    def availability_info(self):
        if self.availability == Availability.PUBLIC:
            return '<a href="https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftOpenLicense">Geosoft Open License</a>'
        elif self.availability == Availability.EXTENSION:
            return '<a href="https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense">Geosoft Extended Desktop License</a>'
        else:
            return '<a href="https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense">Geosoft Desktop License</a>'

    @property
    def limitations_info(self):
        return 'May not be available if running outside of a Oasis Montaj or from a command line program.' if self.is_app else None
    

    @property
    def ext_method_name(self):
        #parent is assigned in code_generator.py
        return self.parent._ext_method_name(self)
