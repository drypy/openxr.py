# This is free and unencumbered software released into the public domain.

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#return-codes
class Error(Exception):
    result: int

    def __init__(self, result: int) -> None:
        self.result = result
