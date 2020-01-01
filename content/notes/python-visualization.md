---
title: "Python Visualization"
date: 2020-01-01T06:31:59-08:00
draft: false
type: notes
categories:
  - General
tags:
  - visualization
series:
  -
---

Notes about 3D python visualization packages.

<!--more-->

## Mayavi

As of Jan 2020 the [mayavi repo](https://github.com/enthought/mayavi) has 2,961 commits from 50 contributs. The repo is at least 11 years old.

Mayavi relies on [VTK](https://www.vtk.org/) and a gui toolkit, for python 3 you can use [PySide2](https://wiki.qt.io/Qt_for_Python) or [PyQt5](https://pypi.org/project/PyQt5/).

## Vispy

As of Jan 2020 the [vispy repo](https://github.com/vispy/vispy) has 6,116
commits from 102 contributors. It is at least 2 years old.

Vispy relies on OpenGL. The setup.py file builds and embbeds js and css resources by leveraging npm.

## Glumpy

As of Jan 2020 the [glumpy repo](https://github.com/glumpy/glumpy) had 791
commits from 35 contributors over its 4 years of existence. Note that according to the vispy readme glumpy should have been integrated in vispy.

Relies on [pyopengl](http://pyopengl.sourceforge.net/).

Use [ctypes](https://docs.python.org/3/library/ctypes.html) and
[cython](https://cython.org/) to load:

* ffmpeg
* sdf
* input hooks
