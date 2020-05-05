#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Test cases for the openxr module."""

from openxr import *

if __name__ == '__main__':
    import pytest, sys

    sys.exit(pytest.main(__file__))
