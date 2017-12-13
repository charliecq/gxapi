# Geosoft GX API Specification Repository

This is the repository used to generate wrapper source code and documentation for the public Geosoft GX APIs. 
At its heart the GX API is exposed as a low level C/C++ API that is version stable. 
The API specification files are used to define and document the signature of the API calls.

Refer to the documentation for more information on using the GX API.

[GX Developer documentation](https://geosoftgxdev.atlassian.net/wiki/display/GD/Python+in+GX+Developer)

Also see the [Geosoft Inc. organization on Github](https://github.com/GeosoftInc) for the programming language specific repos.

License
-------
Any source code found here are released under the [BSD 2-clause license](https://github.com/GeosoftInc/gxpy/blob/master/LICENSE). Core functionality exposed by the GX API may have additional license implications. For more information consult the [License page in the GX Developer Wiki](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License)

# Anatomy of a GX API specification file

The folders **spec/core** and **spec/desk** contains single Python modules for each class in the GX API. 
The **core** folder contains the classes considered to be part of the Geosoft Core internal APIs implemented
by Geosoft, while **desk** contains classes that might depend on implementations in the 
Geosoft Desktop internal APIs. 

A specification module should have at the very least an attribute called **gx_class** of type
[Class](#class) that defines the class properties and documentation.

It can optionally also have a **gx_defines** attribute that should be a list of [Define](#define)
and/or a **gx_methods** dict of lists containing `Method```. The key of the dict
is used to group related methods together in the documentation.

__Example__


```python
from .. import Availability, Class, Constant, Define, Method, Parameter, Type

gx_class = Class('...

...

gx_defines = [
    Define('...

...

gx_methods = {
    'Miscellaneous': [

        Method('...

...
```

__Cross-referencing in Doc strings__

Any doc string in the API specifications can contain cross-references to other API elements.

Here is an example of one with each of the supported references:

```python
...
    see_also="Class :class:`MVIEW`, method :func:`GetXYZChanSymb_DB`, definition :def:`BF_SEEK` and constant :const:`AGG_LAYER_ZONE_SHADE`"
...
```

Class
-----

```python
Class(self, name, doc=None, notes=None, see_also=None, handle_name=None, no_gxh=False, no_csharp=False, no_cpp=False, next_gen=False)
```

API specification for a GX class. 

A specification module should have one of these assigned to 
an attribute called **gx_class**.

__Arguments__

- __name (str)__: Class name
- __doc (str)__: Doc string with class summary
- __notes (str)__: Doc string containing verbose notes (optional)
- __see_also (str)__: Doc string containing see-also type references (optional)
- __handle_name (str)__: GXC API variable type override (does not affect other languages)
- __no_gxh (bool)__: Not available in GXC API when 'True'
- __no_csharp (bool)__: Not available in .Net API when 'True'
- __no_cpp (bool)__: Not available in C++ API when 'True' (nor Python)
- __next_gen (bool)__: Not a legacy class (support enhanced API types and callbacks). Implies __no_gxh__

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- __is_static (bool)__: Class is static and cannot be instantiated by any method
- __has_methods (bool)__: Class has no methods (i.e. just contains definitions)
- __branch (str)__: Branch folder containing the class
- __method_groups (dict of str: list of [Method](#method))__: Method group lists
- __defines (dict of str: list of [Method](#method))__: Defines

__Example__

```python
from .. import Class

gx_methods = {
'Miscellaneous': [

    Method('...

```

Type
----

The **Type** enumeration is used wherever a basic type needs to be specified. E.g.
for a [Method](#method) return value, [Parameter](#parameter) or a [Constant](#constant).

The actual specific types supported by each programming language could be different.

Supported basic types:

- __Type.FLOAT__: Single precision floating point value (32-bit)
- __Type.DOUBLE__: Double precision floating point value (64-bit)
- __Type.INT8_T__: 8-bit signed integer
- __Type.UINT8_T__: 8-bit unsigned integer
- __Type.INT16_T__: 16-bit signed integer
- __Type.UINT16_T__: 16-bit unsigned integer
- __Type.INT32_T__: 32-bit signed integer
- __Type.UINT32_T__: 32-bit unsigned integer
- __Type.INT64_T__: 64-bit signed integer
- __Type.UINT64_T__: 64-bit unsigned integer
- __Type.STRING__: String
- __Type.VOID__: Void (for method return type)
- __Type.BOOL__: Boolean

In some cases a Type will be defined using a string instead. In this case the type will either 
be the name of a [Class](#class), a [Define](#define), or some other known type understood 
by the generation framework (e.g. "VV", "VV_ORDER" or "HDC").


Availability
------------

The **Availability** enumeration is used to indicate under which license a specific [Method](#method)
is available.

Supported values:

- __Availability.PUBLIC__: Available under [Geosoft Open License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-open-lic)
- __Availability.LICENSED__: Available under [Geosoft End-User License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic)
- __Availability.EXTENSION__: Available under [Geosoft Extended End-User License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-end-user-lic)

Define
------

```python
Define(self, name, doc, is_null_handle=False, constants=[])
```

API specification for a grouping GX constants in a definition. 

A specification module could have a list of these assigned to 
an attribute called **gx_defines**.

__Arguments__

- __name (str)__: Class name
- __doc (str)__: Doc string with definition summary
- __is_null_handle (bool)__: Constant acts as null instance of a class
- __constants (list of [Constant](#constant))__: Constants

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- __parent ([Class](#class))__: Parent class

__Example__

```python
from .. import Define, Constant

gx_defines = [
    Define('SOME_DEF',
        doc="Def doc",
        constants=[
            Constant(...
        ]),
        ...
```

Constant
--------

```python
Constant(self, name, value, type, doc=None)
```

API specification for a GX constant

__Arguments__

- __name (str)__: Class name
- __value (str)__: Value
- __type ([Type](#type))__: Type
- __doc (str)__: Doc string with definition summary (optional but recommended)

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- __parent ([Define](#define))__: Parent define

__Example__

```python
from .. import Define, Constant

gx_defines = [
    Define('SOME_DEF',
        doc="Def doc",
        constants=[
            Constant('SOME_CONST', value='24', type=Type.INT32_T,
                    doc="This is 24"),
            ...
        ]),
        ...
```

Method
------

```python
Method(self, name, version=None, availability=<Availability.UNKNOWN: 0>, module=None, doc=None, notes=None, see_also=None, cpp_post=None, external_name=None, is_app=False, is_gui=False, no_gxh=False, no_csharp=False, no_cpp=False, return_type=<Type.UNKNOWN: 0>, return_doc=None, parameters=[], is_deprecated=False, deprecation_version=None, deprecation_doc=None, is_obsolete=False, obsoletion_version=None, obsoletion_doc=None)
```

API specification for a GX method. 

A specification module should have lists of these assigned as the values
for a dict attribute called **gx_methods**.

__Arguments__

- __name (str)__: Method name
- __version (str)__: Version the method was introduced
- __availability ([Availability](#availability))__: Availability
- __module (str)__: Name of binary module containing method (Not used if is_app==True)
- __doc (str)__: Doc string with method summary
- __notes (str)__: Doc string containing verbose notes (optional)
- __see_also (str)__: Doc string containing see-also type references (optional)
- __cpp_post (str)__: Postfix to add to name in C++ API generation
- __external_name (str)__: Defined if exported internal name should be different than name in exposed API (optional)

- __is_app (bool)__: "App" type method. I.e. dynamically loaded at runtime and might not be available to standalone programs
- __is_gui (bool)__: GUI type method. Parent window parameter and handler code could be generated into API to ensure correct modality.
- __no_gxh (bool)__: Not available in GXC API when 'True'
- __no_csharp (bool)__: Not available in .Net API when 'True'
- __no_cpp (bool)__: Not available in C++ API when 'True' (nor Python)

- __return_type ([Type](#type))__: Return type
- __return_doc (str)__: Doc string for return value
- __parameters (list of [Parameter](#parameter))__: Parameters

- __is_deprecated (bool)__: Method has been deprecated (still available but will be marked as such)
- __deprecation_version (str)__: Version the method was deprecated
- __deprecation_doc (str)__: Deprecation doc

- __is_obsolete (bool)__: Method has been obsoleted (still available but will be marked as such)
- __obsoletion_version (str)__: Version the method was obsoleted
- __obsoletion_doc (str)__: Obsoletion doc

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- __parent ([Class](#class))__: Parent class
- __is_static (bool)__: Is this a static method
- __is_destroy_method (bool)__: Is this method used to dispose of the instance
- __exposed_name (str)__: C and GXC APIs external name (influenced by is_app)

__Example__

```python
from .. import Class

# This is a very simple example class with only a doc string
gx_class = Class('GXSOMECLASS',
             doc="""
             This class' can be used to...
             It is directly related to the :class:`GXSOMEOTHERCLASS` class.
             """)
```

Parameter
---------

```python
Parameter(self, name, type, is_ref=False, is_val=False, size_of_param=None, default_length=None, doc=None)
```

API specification for a parameter of a GX method. 

__Arguments__

- __name (str)__: Parameter name
- __type ([Type](#type))__: Type
- __doc (str)__: Doc string with parameter summary
- __is_ref (bool)__: Should parameter be passed by reference
- __is_val (bool)__: By default references (and const references if not is_ref) are used for parameters in the C GX API wrappers. Set this to true if the parameter will be passed by value.
- __size_of_param (str)__: If the parameter is a string and is_ref is True, this indicates the parameter name that contains the available string length.
- __default_length (str)__: If the parameter is a string and is_ref is True, this indicates a good maximum buffer length. Used to eliminate need to expose string length parameter in some language and keeps API simpler.

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- __parent ([Method](#method))__: Parent method


