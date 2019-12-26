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

As per the (documentation)[https://pip.pypa.io/en/stable/] pip is taking the following steps:

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
These are [wheel](https://wheel.readthedocs.io/en/stable/) files, zip files with a custom extension and are defined in [PEP-0427](https://www.python.org/dev/peps/pep-0427/)

