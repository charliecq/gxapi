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


class Define(SpecBase):
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
