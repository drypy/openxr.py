#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Test cases for the openxr.abi module."""

from openxr.abi import *
import ctypes

def test_XrBaseStructure():
    assert(ctypes.sizeof(XrBaseStructure) == 16)

if __name__ == '__main__':
    import pytest, sys

    sys.exit(pytest.main(__file__))
