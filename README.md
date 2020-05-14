OpenXR for Python
=================

[![Project license](https://img.shields.io/badge/license-Public%20Domain-blue.svg)](https://unlicense.org)
[![PyPI package](https://img.shields.io/pypi/v/openxr.svg)](https://pypi.org/project/openxr/)
[![Python compatibility](https://img.shields.io/pypi/pyversions/openxr.svg)](https://pypi.org/project/openxr/)

**OpenXR.py** implements Python bindings for [OpenXR](https://www.khronos.org/openxr/)
[1.0](https://www.khronos.org/registry/OpenXR/specs/1.0/html/xrspec.html),
the open standard and cross-platform API for virtual reality (VR) and
augmented reality (AR) hardware.

Installation
------------

    $ pip3 install openxr

Prerequisites
-------------

- [Python](https://www.python.org) 3.6+
  with [ctypes](https://docs.python.org/3/library/ctypes.html)

- [OpenXR SDK](https://github.com/KhronosGroup/OpenXR-SDK) 1.0.8+

Examples
--------

### Loading the library

    import openxr

Development
-----------

We recommend Debian 11 (aka [Bullseye](https://www.debian.org/releases/bullseye/))
as a development environment. If you're on a Mac, you can run Debian in a
virtual machine using [VMware Fusion](https://www.vmware.com/products/fusion.html)
or [VirtualBox](https://www.virtualbox.org).

Install the Debian packages for the OpenXR SDK's loader as follows:

    $ apt install libopenxr-loader1

That's the only required package, but find related packages of interest using:

    $ apt search openxr

In addition, you _will_ need an OpenXR runtime for your hardware. In the
absence of suitable vendor-supplied runtimes, have a look at the open-source
[Monado](https://monado.freedesktop.org) project which supports many common
devices.

See Also
--------

- [OpenXR.rb](https://github.com/dryruby/openxr.rb): OpenXR bindings Ruby.

- [Unofficial OpenXR Tests](https://github.com/artob/openxr-rspec):
  An unofficial OpenXR conformance test suite.
