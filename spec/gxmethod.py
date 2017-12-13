from .gxdefs import Type, Availability, SpecBase
from distutils.version import StrictVersion

class Parameter(SpecBase):
    '''
    API specification for a parameter of a GX method. 
    
    # Arguments
    name (str): Parameter name
    type (#spec.gxdefs.Type): Type
    doc (str): Doc string with parameter summary
    is_ref (bool): Should parameter be passed by reference
    is_val (bool): By default references (and const references if not is_ref) are used for parameters in the C GX API wrappers. Set this to true if the parameter will be passed by value.
    size_of_param (str): If the parameter is a string and is_ref is True, this indicates the parameter name that contains the available string length.
    default_length (str): If the parameter is a string and is_ref is True, this indicates a good maximum buffer length. Used to eliminate need to expose string length parameter in some language and keeps API simpler.
    
    # Attributes
    All the arguments passed to the constructor are available as attributes on the instance.
    The following attributes are mixed in by the code generation framework startup code and 
    is used by the code generation scripts and templates.

    parent (#spec.gxmethod.Method): Parent method
    '''

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
    '''
    API specification for a GX method. 
    
    A specification module should have lists of these assigned as the values
    for a dict attribute called **gx_methods**.

    # Arguments
    name (str): Method name
    version (str): Version the method was introduced
    availability (#spec.gxdefs.Availability): Availability
    module (str): Name of binary module containing method (Not used if is_app==True)
    doc (str): Doc string with method summary
    notes (str): Doc string containing verbose notes (optional)
    see_also (str): Doc string containing see-also type references (optional)
    cpp_post (str): Postfix to add to name in C++ API generation
    external_name (str): Defined if exported internal name should be different than name in exposed API (optional)

    is_app (bool): "App" type method. I.e. dynamically loaded at runtime and might not be available to standalone programs
    is_gui (bool): GUI type method. Parent window parameter and handler code could be generated into API to ensure correct modality.
    no_gxh (bool): Not available in GXC API when 'True'
    no_csharp (bool): Not available in .Net API when 'True'
    no_cpp (bool): Not available in C++ API when 'True' (nor Python)
    
    return_type (#spec.gxdefs.Type): Return type
    return_doc (str): Doc string for return value
    parameters (list of #Parameter#): Parameters

    is_deprecated (bool): Method has been deprecated (still available but will be marked as such)
    deprecation_version (str): Version the method was deprecated
    deprecation_doc (str): Deprecation doc

    is_obsolete (bool): Method has been obsoleted (still available but will be marked as such)
    obsoletion_version (str): Version the method was obsoleted
    obsoletion_doc (str): Obsoletion doc

    # Attributes
    All the arguments passed to the constructor are available as attributes on the instance.
    The following attributes are mixed in by the code generation framework startup code and 
    is used by the code generation scripts and templates.

    parent (#spec.gxclass.Class): Parent class
    is_static (bool): Is this a static method
    is_destroy_method (bool): Is this method used to dispose of the instance
    exposed_name (str): C and GXC APIs external name (influenced by is_app)

    # Example
    ```python
    from .. import Class

    # This is a very simple example class with only a doc string
    gx_class = Class('GXSOMECLASS',
                 doc="""
                 This class' can be used to...
                 It is directly related to the :class:`GXSOMEOTHERCLASS` class.
                 """)
    ```
    '''

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
            return '`Geosoft Open License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftOpenLicense>`_'
        elif self.availability == Availability.EXTENSION:
            return '`Geosoft Extended End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense>`_'
        else:
            return '`Geosoft End-User License <https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense>`_'
        
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
