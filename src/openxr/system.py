# This is free and unencumbered software released into the public domain.

from .instance import Instance

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#system
class System:
    instance: Instance
    id: int

    def __init__(self, instance: Instance, id: int) -> None:
        self.instance = instance
        self.id = id
