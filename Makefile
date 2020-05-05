PACKAGE := openxr
VERSION := $(shell cat VERSION)

PANDOC  ?= pandoc
PYTHON  ?= python3
PYTEST  ?= pytest
TWINE   ?= twine

SOURCES := $(wildcard src/*/*.py src/*/*/*.py)

%.html: %.md
	$(PANDOC) -o $@ -f gfm -t html5 -s $<

all: dist

dist/$(PACKAGE)-$(VERSION).tar.gz: setup.py MANIFEST.in $(SOURCES)
	$(PYTHON) setup.py sdist --formats=gztar

dist/$(PACKAGE)-$(VERSION).tar.xz: setup.py MANIFEST.in $(SOURCES)
	$(PYTHON) setup.py sdist --formats=xztar

dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl: setup.py $(SOURCES)
	$(PYTHON) setup.py bdist_wheel

build: setup.py $(SOURCES)
	$(PYTHON) setup.py build

check: $(SOURCES) $(wildcard test/test*.py)
	PYTHONPATH=src $(PYTEST)

dist:  sdist bdist
sdist: dist/$(PACKAGE)-$(VERSION).tar.gz
bdist: dist/$(PACKAGE)-$(VERSION)-py3-none-any.whl

install: setup.py $(SOURCES)
	$(PYTHON) setup.py build

clean: setup.py
	@rm -Rf *~ build dist
	$(PYTHON) setup.py clean

distclean: clean

mostlyclean: clean

.PHONY: build check dist sdist bdist install clean distclean mostlyclean
.SECONDARY:
.SUFFIXES:
