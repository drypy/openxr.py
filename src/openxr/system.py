# This is free and unencumbered software released into the public domain.

##
# @see https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#system
class System:
    def __init__(self, instance, id):
        self.instance = instance
        self.id = id
