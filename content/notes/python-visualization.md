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

## ipywidgets

Some of these are integrated with [ipywidgets](https://ipywidgets.readthedocs.io/en/latest/index.html).

Install and debub courtesy of [ipyvolume issue#102](https://github.com/maartenbreddels/ipyvolume/issues/102#issuecomment-358641450)

Install steps from fresh venv creation, less may be needed 
```
pip install jupyter
pip install jupyterlab
jupyter labextension install @jupyter-widgets/jupyterlab-manager
jupyter lab --no-browser
```

Debug from command line
```
jupyter labextension list
```

Debug in notebook
```
import ipywidgets
ipywidgets.FloatSlider()
```

## ipyvolume

* docs: https://ipyvolume.readthedocs.io/en/latest/index.html
* github: https://github.com/maartenbreddels/ipyvolume
* SciPy 2018 presentation: https://www.youtube.com/watch?v=hOKa8klJPyo

## Other



* [yt](http://yt-project.org/)

* [plotly](https://github.com/plotly/plotly.py) ()

* [itk-jupyter-widgets](https://github.com/banesullivan/itk-jupyter-widgets)

* [K3D-jupyter](https://github.com/K3D-tools/K3D-jupyter)

* [pytreejs](https://github.com/jupyter-widgets/pythreejs) (ipywidgets)
  - A Python / ThreeJS bridge utilizing the Jupyter widget infrastructure.
  - scene graph library
  
