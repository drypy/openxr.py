# This is free and unencumbered software released into the public domain.

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#handles
class Handle:
    """An OpenXR handle."""

    def __init__(self) -> None:
        pass

    def destroy(self) -> None:
        pass # subclasses MUST implement this
