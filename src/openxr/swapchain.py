# This is free and unencumbered software released into the public domain.

from typing import Optional

from .handle import Handle

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#rendering
class Swapchain(Handle):
    """An OpenXR swapchain handle."""

    def __init__(self) -> None:
        super().__init__()

    def destroy(self) -> None:
        """Destroy the swapchain."""
        pass # TODO
