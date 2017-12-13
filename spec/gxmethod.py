from .gxdefs import Type, Availability, SpecBase
from distutils.version import StrictVersion

class Parameter(SpecBase):
    def __init__(self, name, type, is_ref=False, is_val=False,
                 size_of_param=None, default_length=None, doc=None):
        super().__init__(name)

        self.name = name
        self.type = type
        self.doc = doc
        self.is_ref = is_ref
        self.is_val = is_val
        self.size_of_param = size_of_param
        self.default_length = default_length

    def validate(self):
        pass


_min_undocumented_obsolete_or_deprecated = StrictVersion("9.3")

class Method(SpecBase):
    _parameters = None
    _ext_method_name = None

    def __init__(self, name, version=None, availability=Availability.UNKNOWN, module=None, doc=None, notes=None, see_also=None, cpp_post=None, external_name=None, 
                 is_app=False, is_gui=False, no_gxh=False, no_csharp=False, no_cpp=False,
                 return_type=Type.UNKNOWN, return_doc=None, parameters=[],
                 is_deprecated=False, deprecation_version=None, deprecation_doc=None, 
                 is_obsolete=False, obsoletion_version=None, obsoletion_doc=None):
        super().__init__(name)

        self.name = name
        self.version = StrictVersion(version) if isinstance(version, str) else None
        self.availability = availability
        self.module = module
        self.doc = doc
        self.notes = notes
        self.see_also = see_also
        self.cpp_post = cpp_post
        self.external_name = external_name if external_name else self.name
        
        self.is_app = is_app
        self.is_gui = is_gui
        self.no_gxh = no_gxh
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        
        self.return_type = return_type
        self.return_doc = return_doc
        self.parameters = parameters
        
        self.is_deprecated = is_deprecated
        self.deprecation_version = StrictVersion(deprecation_version) if isinstance(deprecation_version, str) else None
        self.deprecation_doc = deprecation_doc
        
        self.is_obsolete = is_obsolete
        self.obsoletion_version = StrictVersion(obsoletion_version) if isinstance(obsoletion_version, str) else None
        self.obsoletion_doc = obsoletion_doc
        
        self.is_static = True
        self.is_destroy_method = False
        self.exposed_name = external_name if external_name else 'App_{}'.format(self.name) if self.is_app else self.name


    def validate(self):
        if not self.version:
            raise RuntimeError('Undocumented method {}'.format(self))
        if not self.doc:
            raise RuntimeError('Undocumented method {}'.format(self))
        if self.is_deprecated and self.version > _min_undocumented_obsolete_or_deprecated:
            if not self.deprecation_doc:
                raise RuntimeError('{} was deprecated without specifying an deprecation_doc'.format(self))
            if not self.deprecation_version:
                raise RuntimeError('{} was deprecated without specifying an deprecation_version'.format(self))
        if self.is_obsolete and self.version > _min_undocumented_obsolete_or_deprecated:
            if not self.obsoletion_doc:
                raise RuntimeError('{} was obsoleted without specifying an obsoletion_doc'.format(self))
            if not self.obsoletion_version:
                raise RuntimeError('{} was obsoleted without specifying an obsoletion_version'.format(self))
        for parameter in self.parameters:
            parameter.validate()

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
    def availability_info_html(self):
        if self.availability == Availability.PUBLIC:
            return '<a href="https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftOpenLicense">Geosoft Open License</a>'
        elif self.availability == Availability.EXTENSION:
            return '<a href="https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense">Geosoft Extended End-User License</a>'
        else:
            return '<a href="https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense">Geosoft End-User License</a>'

    @property
    def availability_info_rst(self):
        if self.availability == Availability.PUBLIC:
            return '`Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#open-lic>`_'
        elif self.availability == Availability.EXTENSION:
            return '`Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#ext-end-user-lic>`_'
        else:
            return '`Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#end-user-lic>`_'
        
    @property
    def limitations_info(self):
        return 'May not be available while executing a command line program.' if self.is_app else None
    

    @property
    def ext_method_name(self):
        if not self._ext_method_name:
            if not self.parent:
                #parent is assigned in code_generator.py
                raise 'ext_method_name property is not available until parent class is assigned ({})'.format(self.name)
            self._ext_method_name = self.parent._ext_method_name(self)
        return self._ext_method_name
