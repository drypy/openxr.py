# This is free and unencumbered software released into the public domain.

##
# @see https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html#instance
class Instance:
    def __init__(self, app_name, app_version=None, api_version=None):
        self.app_name = app_name
        self.app_version = app_version
        self.api_version = api_version
