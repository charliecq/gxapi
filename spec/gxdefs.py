'''
API specification of types, availability and constant defines for a GX class. 

# Types

#spec.gxdefs.Type enumerations are used wherever a basic type needs to be specified. E.g.
for a #spec.gxmethods.Method return value, #spec.gxmethods.Parameter or a #spec.gxdefs.Constant.

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
be the name of a #spec.gxclass.Class, a #spec.gxdefs.Define, or some other known type understood 
by the generation framework (e.g. "VV", "VV_ORDER" or "HDC").


# Availability

#spec.gxdefs.Availability is used to indicate under which license a specific #spec.gxmethods.Method
is available.

Supported values:

    Availability.PUBLIC: Available under [Geosoft Open License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftOpenLicense
    Availability.LICENSED: Available under [Geosoft End-User License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftDesktopLicense)
    Availability.EXTENSION: Available under [Geosoft Extended End-User License](https://geosoftgxdev.atlassian.net/wiki/spaces/GD/pages/2359406/License#License-GeosoftExtendedDesktopLicense)
    
'''

from enum import IntEnum
import copy

class Type(IntEnum):
    UNKNOWN = 0 
    FLOAT = 1
    DOUBLE = 2
    INT8_T = 3
    UINT8_T = 4
    INT16_T = 5
    UINT16_T = 6
    INT32_T = 7
    UINT32_T = 8
    INT64_T = 9
    UINT64_T = 10
    STRING = 11
    VOID = 12
    BOOL = 13
    FLOAT_2D = 14
    FLOAT_3D = 15
    DOUBLE_2D = 16
    DOUBLE_3D = 17
    FLOAT_BBOX_2D = 18
    FLOAT_BBOX_3D = 19
    DOUBLE_BBOX_2D = 20
    DOUBLE_BBOX_3D = 21


class Availability(IntEnum):
    UNKNOWN = 0
    PUBLIC = 1
    LICENSED = 2
    EXTENSION = 3


class SpecBase:
    # Base class used in code generator classes
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.generator = None

    def __str__(self):
        if self.parent:
            return '{}.{}'.format(self.parent, self.name)
        else:
            return self.name

    def construct_copy(self, other):
        for k, v in other.__dict__.items():
            setattr(self, k, copy.deepcopy(v))


class Constant(SpecBase):
    '''
    API specification for a GX constant
    
    # Arguments
    name (str): Class name
    value (str): Value
    type (#spec.gxdefs.Type): Type
    doc (str): Doc string with definition summary (optional but recommended)
    
    # Attributes
    All the arguments passed to the constructor are available as attributes on the instance.
    The following attributes are mixed in by the code generation framework startup code and 
    is used by the code generation scripts and templates.

    parent (#spec.gxdefs.Define): Parent define
    
    # Example
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
    '''

    def __init__(self, name, value, type, doc=None):
        super().__init__(name)

        self.name = name
        self.value = value
        self.type = type
        self.doc = doc

    def validate(self):
        if self.value.startswith('0x') and not self.type == Type.STRING and not (
            self.type == Type.UINT32_T or
            self.type == Type.INT32_T or
            self.type == Type.UINT64_T or
            self.type == Type.INT64_T):
            raise RuntimeError('Unsupported type for constant {} with hex value {}'.format(self, self.value))

        if self.parent:
            if not isinstance(self.type, Type) and not self.parent.is_null_handle:
                raise RuntimeError('Unsupported type {} for constant {}'.format(self.type, self))

            if self.parent.parent:
                if not isinstance(self.type, str) and not self.parent.parent.next_gen and self.type > Type.BOOL:
                    raise RuntimeError('Unsupported type {} for constant {} in legacy class {}.'.format(self.type, self, self.parent.parent.name))

            


class Define(SpecBase):
    '''
    API specification for a grouping GX constants in a definition. 
    
    A specification module could have a list of these assigned to 
    an attribute called **gx_defines**.

    # Arguments
    name (str): Class name
    doc (str): Doc string with definition summary
    is_null_handle (bool): Constant acts as null instance of a class
    constants (list of #spec.gxdefs.Constant): Constants
    
    # Attributes
    All the arguments passed to the constructor are available as attributes on the instance.
    The following attributes are mixed in by the code generation framework startup code and 
    is used by the code generation scripts and templates.

    parent (#spec.gxclass.Class): Parent class
    
    # Example
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
    '''
    def __init__(self, name, doc, is_null_handle=False, constants=[]):
        super().__init__(name)

        self.name = name
        self.doc = doc
        self.is_null_handle = is_null_handle
        self.constants = constants

    def validate(self):
        if not self.doc:
            raise RuntimeError('Undocumented define {}'.format(self))
        
        for constant in self.constants:
            constant.validate()
