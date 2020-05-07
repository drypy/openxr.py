# This is free and unencumbered software released into the public domain.

"""OpenXR bindings for Python."""

import sys

assert sys.version_info >= (3, 6), "OpenXR.py requires Python 3.6+"

from .action import Action
from .action_set import ActionSet
from .extension import Extension
from .handle import Handle
from .instance import Instance
from .layer import Layer
from .result import Result
from .session import Session
from .space import Space
from .swapchain import Swapchain
from .system import System

__all__ = [
    'Action',
    'ActionSet',
    'Extension',
    'Handle',
    'Instance',
    'Layer',
    'Result',
    'Session',
    'Space',
    'Swapchain',
    'System',
]
