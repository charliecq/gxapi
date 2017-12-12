from aenum import IntEnum
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
    STD_STRING = 14
    VECT_2D = 15
    VECT_3D = 16
    


class Availability(IntEnum):
    UNKNOWN = 0
    PUBLIC = 1
    LICENSED = 2
    EXTENSION = 3


class SpecBase:
    # Base class used in code generator classes
    def __init__(self):
        self.name_space = None
        self.generator = None
        self.parent = None

    def construct_copy(self, other):
        for k, v in other.__dict__.items():
            setattr(self, k, copy.deepcopy(v))


class Constant(SpecBase):
    def __init__(self, name, value, type=Type.UNKNOWN, doc=None):
        super().__init__()

        self.name = name
        self.value = value
        self.type = type
        self.doc = doc
        self.parent = None

    def validate(self):
        if self.value.startswith('0x') and not (self.type == Type.STRING or self.type == Type.STD_STRING) and not (
            self.type == Type.UINT32_T or
            self.type == Type.INT32_T or
            self.type == Type.UINT64_T or
            self.type == Type.INT64_T):
            raise RuntimeError('Unsupported type for constant {} with hex value {}'.format(self.name, self.value))

        if self.parent:
            if not isinstance(self.type, Type) and not self.parent.is_null_handle:
                raise RuntimeError('Unsupported type {} for constant {}'.format(self.type, self.name))

            if self.parent.parent:
                if not isinstance(self.type, str) and not self.parent.parent.next_gen and self.type > Type.BOOL:
                    raise RuntimeError('Unsupported type {} for constant {} in legacy class {}.'.format(self.type, self.name, self.parent.parent.name))

            


class Define(SpecBase):
    def __init__(self, name, is_constant=False, is_single_constant=False,
                 is_null_handle=False, doc=None, constants=[]):
        super().__init__()

        self.name = name
        self.is_constant = is_constant
        self.is_single_constant = is_single_constant
        self.is_null_handle = is_null_handle
        self.doc = doc
        self.constants = constants
        self.parent = None

        self.validate()

    def validate(self):
        for constant in self.constants:
            constant.validate()
