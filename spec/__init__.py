"""
This is module is used to generate wrapper source code and documentation for the public 
Geosoft GX APIs. At its heart the GX API is exposed as a low level C/C++ API that is 
version stable. The API specification files are used to define and document the signature 
of the API calls.

See the [Geosoft GX API Specification Repository](https://github.com/GeosoftInc/gxapi#geosoft-gx-api-specification-repository) 
for more information.

# Anatomy of a GX API specification file

The folders **core** and **desk** contains single Python modules for each class in the GX API. 
**core** includes the classes considered to be part of the Geosoft Core internal APIs implemented
by Geosoft, while **desk** contains classes that might depend on implementations in the 
Geosoft Desktop internal APIs. 

A specification module should have at the very least an attribute called **gx_class** of type
#spec.gxclass.Class that defines the class properties and documentation.

It can optionally also have a **gx_defines** attribute that should be a list of #spec.gxdefs.Define
and/or a **gx_methods** dict of lists containing #spec.gxmethods.Method . The key of the dict
is used to group related methods together in the documentation.

# Example

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

# License
Any source code found here are released under the [BSD 2-clause license](https://github.com/GeosoftInc/gxpy/blob/master/LICENSE). Core functionality exposed by the GX API may have additional license implications. For more information consult the [License page in the GX Developer Wiki](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License)

"""

from .gxdefs import Type, Availability, Constant, Define
from .gxclass import Class
from .gxmethod import Parameter, Method
