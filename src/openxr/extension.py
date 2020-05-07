# This is free and unencumbered software released into the public domain.

from typing import List

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#extensions
class Extension:
    name: str
    version: int

    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version
