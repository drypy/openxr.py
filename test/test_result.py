#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Test cases for the openxr.result module."""

from openxr import Result

def test_result():
    assert(Result(42).code == 42)

if __name__ == '__main__':
    import pytest, sys

    sys.exit(pytest.main(__file__))
