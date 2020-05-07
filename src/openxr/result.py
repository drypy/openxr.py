# This is free and unencumbered software released into the public domain.

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#return-codes
class Result(Exception):
    """An OpenXR result code."""

    code: int

    def __init__(self, code: int) -> None:
        self.code = code
