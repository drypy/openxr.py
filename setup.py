#!/usr/bin/env python3
# This is free and unencumbered software released into the public domain.

"""Installation script for OpenXR.py."""

from codecs import open
from os import path
from setuptools import setup, find_packages
from shutil import copyfile


def readfile(*filepath):
    with open(path.join(*filepath), encoding='utf-8') as f:
        return f.read()


PWD = path.abspath(path.dirname(__file__))

VERSION = readfile(PWD, 'VERSION').rstrip()
LONG_DESCRIPTION = readfile(PWD, 'README.md')

setup(
    name='openxr',
    version=VERSION,
    description="OpenXR bindings for Python.",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/drypy/openxr.py',
    author='Arto Bendiken',
    author_email='arto@bendiken.net',
    license='Public Domain',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Multimedia :: Graphics :: 3D Rendering',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
        'Topic :: Software Development :: User Interfaces',
    ],
    keywords='',
    project_urls={'Source': 'https://github.com/drypy/openxr.py'},
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    python_requires='~=3.6',
    extras_require={'test': ['pytest'],},
)
