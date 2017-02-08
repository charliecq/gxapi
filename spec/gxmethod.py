import importlib
import glob
import os
import itertools
from enum import Enum

from .gxdefs import Type, Availability

class Parameter:
    def __init__(self, name, type=Type.UNKNOWN, is_ref=False, is_val=False,
                 size_of_param=None, default_length=None, doc=None):
        self.name = name
        self.type = type
        self.is_ref = is_ref
        self.is_val = is_val
        self.size_of_param = size_of_param
        self.default_length = default_length
        self.doc = doc

class Method:
    def __init__(self, name, module=None, version=None, external_name=None, availability=Availability.UNKNOWN,
                 is_obsolete=False, is_app=False, is_gui=False, no_gxh=False, no_csharp=False, no_cpp=False,
                 return_type=Type.UNKNOWN, return_doc=None,
                 doc=None, parameters=[]):
        self.name = name
        self.module = module
        self.version = version
        self.external_name = external_name
        self.availability = availability
        self.is_obsolete = is_obsolete
        self.is_app = is_app
        self.is_gui = is_gui
        self.no_gxh = no_gxh
        self.no_csharp = no_csharp
        self.no_cpp = no_cpp
        self.doc = doc
        self.return_type = return_type
        self.return_doc = return_doc
        self.parameters = parameters


