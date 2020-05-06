# This is free and unencumbered software released into the public domain.

##
# @see https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#extensions
class Extension:
    def __init__(self, name, version):
        self.name = name
        self.version = version
