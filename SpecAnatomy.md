<h1 id="spec">spec</h1>


This is module is used to generate wrapper source code and documentation for the public 
Geosoft GX APIs. At its heart the GX API is exposed as a low level C/C++ API that is 
version stable. The API specification files are used to define and document the signature 
of the API calls.

See the [Geosoft GX API Specification Repository](https://github.com/GeosoftInc/gxapi`geosoft`-gx-api-specification-repository) 
for more information.

__Anatomy of a GX API specification file__


The folders **core** and **desk** contains single Python modules for each class in the GX API. 
**core** includes the classes considered to be part of the Geosoft Core internal APIs implemented
by Geosoft, while **desk** contains classes that might depend on implementations in the 
Geosoft Desktop internal APIs. 

A specification module should have at the very least an attribute called **gx_class** of type
`spec.gxclass.Class` that defines the class properties and documentation.

It can optionally also have a **gx_defines** attribute that should be a list of `spec.gxdefs.Define`
and/or a **gx_methods** dict of lists containing `spec.gxmethods.Method` . The key of the dict
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

__License__

Any source code found here are released under the [BSD 2-clause license](https://github.com/GeosoftInc/gxpy/blob/master/LICENSE). Core functionality exposed by the GX API may have additional license implications. For more information consult the [License page in the GX Developer Wiki](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License)


<h2 id="spec.gxclass">spec.gxclass</h2>


<h3 id="spec.gxclass.Class">Class</h3>

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

            cl.is_static = True
        cl.has_methods = False

- `is_static (bool)`: Class is static and cannot be instantiated by any method
- `has_methods (bool)`: Class has no methods (i.e. just contains definitions)
- `branch (str)`: Branch folder containing the class
- `method_groups (dict of str: list of `spec.gxmethods.Method`)`: Method group lists
- `defines (dict of str: list of `spec.gxmethods.Method`)`: Defines

__Example__

```python
from .. import Class

gx_methods = {
'Miscellaneous': [

    Method('...

```

<h2 id="spec.gxdefs">spec.gxdefs</h2>


API specification of types, availability and constant defines for a GX class. 

__Types__


`spec.gxdefs.Type` enumerations are used wherever a basic type needs to be specified. E.g.
for a `spec.gxmethods.Method` return value, `spec.gxmethods.Parameter` or a `spec.gxdefs.Constant`.

The actual specific types supported by each programming language could be different.

Supported basic types:

    Type.FLOAT: Single precision floating point value (32-bit)
    Type.DOUBLE: Double precision floating point value (64-bit)
    Type.INT8_T: 8-bit signed integer
    Type.UINT8_T: 8-bit unsigned integer
    Type.INT16_T: 16-bit signed integer
    Type.UINT16_T: 16-bit unsigned integer
    Type.INT32_T: 32-bit signed integer
    Type.UINT32_T: 32-bit unsigned integer
    Type.INT64_T: 64-bit signed integer
    Type.UINT64_T: 64-bit unsigned integer
    Type.STRING: String
    Type.VOID: Void (for method return type)
    Type.BOOL: Boolean
    Type.FLOAT_2D: Single precision floating point 2D vector
    Type.FLOAT_3D: Single precision floating point 3D vector
    Type.DOUBLE_2D: Double precision floating point 2D vector
    Type.DOUBLE_3D: Double precision floating point 3D vector
    Type.FLOAT_BBOX_2D: Single precision floating point 2D bounding box
    Type.FLOAT_BBOX_3D: Single precision floating point 3D bounding box
    Type.DOUBLE_BBOX_2D: Double precision floating point 2D bounding box
    Type.DOUBLE_BBOX_3D: Double precision floating point 3D bounding box


In some cases a Type will be defined using a string instead. In this case the type will either 
be the name of a `spec.gxclass.Class`, a `spec.gxdefs.Define`, or some other known type understood 
by the generation framework (e.g. "VV", "VV_ORDER" or "HDC").


__Availability__


`spec.gxdefs.Availability` is used to indicate under which license a specific `spec.gxmethods.Method`
is available.

Supported values:

    Availability.PUBLIC: Available under [Geosoft Open License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License`License`-GeosoftOpenLicense
    Availability.LICENSED: Available under [Geosoft End-User License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License`License`-GeosoftDesktopLicense)
    Availability.EXTENSION: Available under [Geosoft Extended End-User License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License`License`-GeosoftExtendedDesktopLicense)


<h3 id="spec.gxdefs.Define">Define</h3>

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
- __constants (list of `spec.gxdefs.Constant`)__: Constants

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- `parent (`spec.gxclass.Class`)`: Parent class

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

<h3 id="spec.gxdefs.Constant">Constant</h3>

```python
Constant(self, name, value, type, doc=None)
```

API specification for a GX constant

__Arguments__

- __name (str)__: Class name
- __value (str)__: Value
- __type (`spec.gxdefs.Type`)__: Type
- __doc (str)__: Doc string with definition summary (optional but recommended)

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- `parent (`spec.gxdefs.Define`)`: Parent define

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

<h2 id="spec.gxmethod">spec.gxmethod</h2>


<h3 id="spec.gxmethod.Method">Method</h3>

```python
Method(self, name, version=None, availability=<Availability.UNKNOWN: 0>, module=None, doc=None, notes=None, see_also=None, cpp_post=None, external_name=None, is_app=False, is_gui=False, no_gxh=False, no_csharp=False, no_cpp=False, return_type=<Type.UNKNOWN: 0>, return_doc=None, parameters=[], is_deprecated=False, deprecation_version=None, deprecation_doc=None, is_obsolete=False, obsoletion_version=None, obsoletion_doc=None)
```

API specification for a GX method. 

A specification module should have lists of these assigned as the values
for a dict attribute called **gx_methods**.

__Arguments__

- __name (str)__: Method name
- __version (str)__: Version the method was introduced
- __availability (`spec.gxdefs.Availability`)__: Availability
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

- __return_type (`spec.gxdefs.Type`)__: Return type
- __return_doc (str)__: Doc string for return value
- __parameters (list of `spec.gxmethods.Parameter`)__: Parameters

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

- `parent (`spec.gxclass.Class`)`: Parent class
- `is_static (bool)`: Is this a static method
- `is_destroy_method (bool)`: Is this method used to dispose of the instance
- `exposed_name (str)`: C and GXC APIs external name (influenced by is_app)

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

<h3 id="spec.gxmethod.Parameter">Parameter</h3>

```python
Parameter(self, name, type, is_ref=False, is_val=False, size_of_param=None, default_length=None, doc=None)
```

API specification for a parameter of a GX method. 

__Arguments__

- __name (str)__: Parameter name
- __type (`spec.gxdefs.Type`)__: Type
- __doc (str)__: Doc string with parameter summary
- __is_ref (bool)__: Should parameter be passed by reference
- __is_val (bool)__: By default references (and const references if not is_ref) are used for parameters in the C GX API wrappers. Set this to true if the parameter will be passed by value.
- __size_of_param (str)__: If the parameter is a string and is_ref is True, this indicates the parameter name that contains the available string length.
- __default_length (str)__: If the parameter is a string and is_ref is True, this indicates a good maximum buffer length. Used to eliminate need to expose string length parameter in some language and keeps API simpler.

__Attributes__

All the arguments passed to the constructor are available as attributes on the instance.
The following attributes are mixed in by the code generation framework startup code and 
is used by the code generation scripts and templates.

- `parent (`spec.gxmethod.Method`)`: Parent method

