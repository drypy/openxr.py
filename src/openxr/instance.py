# This is free and unencumbered software released into the public domain.

from typing import Optional

##
# See: https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#instance
class Instance:
    app_name: str
    app_version: Optional[int]
    api_version: Optional[int]

    def __init__(self, app_name: str, app_version: Optional[int] = None, api_version: Optional[int] = None) -> None:
        self.app_name = app_name
        self.app_version = app_version
        self.api_version = api_version
