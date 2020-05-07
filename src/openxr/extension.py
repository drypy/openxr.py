# This is free and unencumbered software released into the public domain.

from typing import Dict, List

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#extensions
class Extension:
    """An OpenXR instance extension."""

    name: str
    version: int

    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    @staticmethod
    def count() -> int:
        return 0 # TODO

    @staticmethod
    def list() -> List['Extension']:
        return [] # TODO

    @staticmethod
    def query() -> Dict[str, 'Extension']:
        return {} # TODO
