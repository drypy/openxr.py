# This is free and unencumbered software released into the public domain.

"""OpenXR bindings for Python."""

import sys

assert sys.version_info >= (3, 6), "OpenXR.py requires Python 3.6+"

from .error import Error
from .extension import Extension
from .instance import Instance
from .layer import Layer
from .session import Session
from .system import System

__all__ = ['Error', 'Extension', 'Instance', 'Layer', 'Session', 'System']
