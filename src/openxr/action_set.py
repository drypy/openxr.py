# This is free and unencumbered software released into the public domain.

from typing import Optional

from .handle import Handle

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#input
class ActionSet(Handle):
    """An OpenXR action set handle."""

    def __init__(self) -> None:
        super().__init__()

    def destroy(self) -> None:
        """Destroy the action set."""
        pass # TODO
