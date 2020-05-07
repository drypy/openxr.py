# This is free and unencumbered software released into the public domain.

from typing import Dict, Optional

from .instance import Instance

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#system
class System:
    """An OpenXR system."""

    instance: Instance
    id: int
    name: Optional[str]
    vendor_id: Optional[int]
    graphics_properties: Optional[Dict[str, int]]
    tracking_properties: Optional[Dict[str, bool]]

    def __init__(self, instance: Instance, id: int) -> None:
        self.instance = instance
        self.id = id
