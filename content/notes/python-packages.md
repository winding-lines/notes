---
title: "Python Packages"
slug: "pip"
date: 2019-12-26T05:54:33-08:00
draft: false
type: notes
categories:
  - General
tags:
  - python
series:

---

The package manager in the python ecosystem is pip.

<!--more-->


## Intro

For an overview of installing packages in python head over to the [tutorial](https://packaging.python.org/tutorials/installing-packages).

As per the [documentation](https://pip.pypa.io/en/stable/) pip is taking the following steps:

1. Identify the base requirements. The user supplied arguments are processed here.

2. Resolve dependencies. What will be installed is determined here.

3. Build wheels. All the dependencies that can be are built into wheels.

4. Install the packages (and uninstall anything being upgraded/replaced).

## Isolated installs

In order keep your environment clean you should setup and activate a [venv](https://docs.python.org/3/library/venv.html). By using a venv you do not change the globally installed versions of packages. Pip will still use the global pip cache so you minimize the amount of wasted disk space by having multiple installs.

## Alternatives

Complex packages like as ML frameworks have a lot of dependencies. In some cases it may be simpler to use a docker image, if provided by the developers, or [conda](https://docs.conda.io/en/latest/).


## Wheels

When searching for `tensorflow` on pypi you will see that the  have the extension `whl`. 
These are [wheel](https://wheel.readthedocs.io/en/stable/) files, zip files with a custom extension and are defined in [PEP-0427](https://www.python.org/dev/peps/pep-0427/).

When building wheels for multiple linux architectures it can be beneficial to use [manylinux](https://github.com/pypa/manylinux).

## Setuptools

From [Read the docs](https://setuptools.readthedocs.io/en/latest/setuptools.html): "Setuptools is a collection of enhancements to the Python distutils that allow developers to more easily build and distribute Python packages, especially ones that have dependencies on other packages." The documentation page mentions that setuptools is used to build Python egg distributable which seems to be deprecated in favor of wheels.


## Binary dependencies

Some of the python magic is achieved through binary dependencies. Some of the tools used to bring those in the interpreter are:

* [ctypes](https://docs.python.org/3/library/ctypes.html) - loads shared libraries using the Foreing Function Interface (FFI)
* [cython](https://cython.org/) -  optimising static compiler for both the Python programming language and the extended Cython programming language.
