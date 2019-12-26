---
title: "TensorFlow Install"
slug: tf-setup
description: "Unpack the TF installation steps"
summary: "How does TF install itself and its dependencies on your local dev system?"
date: 2019-12-25T05:59:28-08:00
type: posts
draft: false
categories:
  - General
tags:
  -
series:
  -
---




## Intro

This post describes the dependencies and the steps through which
Tensorflow (TF) gets installed on your development machine. We go in details of the underlying implementation. 

For an end user you may be better served to use the docker image or [conda](https://docs.conda.io/en/latest/).

This post will focus on installing for local dev. In order keep your environment clean you should setup and activate a [venv](https://docs.python.org/3/library/venv.html).

The instructions to install Tensorflow (TF) are here
[instructions](https://www.tensorflow.org/install) and one should run:

```

$  pip install tensorflow

```

## pip

The starting point to the Tensorflow installation is (pip)[https://pip.pypa.io/en/stable/], the package manager in the python ecosystem.

As per the documentation pip is taking the following steps:

1. Identify the base requirements. The user supplied arguments are processed here.

2. Resolve dependencies. What will be installed is determined here.

3. Build wheels. All the dependencies that can be are built into wheels.

4. Install the packages (and uninstall anything being upgraded/replaced).

## wheels

When searching for `tensorflow` on pypi you will see that the [download files](https://pypi.org/project/tensorflow/#files) have the extension `whl`. 
These are [wheel](https://wheel.readthedocs.io/en/stable/) files, zip files with a custom extension and are defined in [PEP-0427](https://www.python.org/dev/peps/pep-0427/)

For python 3.7 there are 3 files

* tensorflow-2.0.0-cp37-cp37m-macosx_10_11_x86_64.whl 
* tensorflow-2.0.0-cp37-cp37m-manylinux2010_x86_64.whl 
* tensorflow-2.0.0-cp37-cp37m-win_amd64.whl

The `manylinux2010`  is platform tag which allows binary wheels to be installed on compatible linux libraries. This is probably the reason why TF requires pip version 19, as per the [changelog](https://pip.pypa.io/en/stable/news/) this platform support first appeared in this version.

### Structure of the macos wheel

The macos wheel contains 4764 files out of which 1513 py files, 2239 header files + 121 C files that need to be compiled. Note that installing a python file from a wheel should not involve the build system at all so it's not clear what the C files are for.

 These files are split amongst the following top-level folders:

* tensorflow: just an \_\_init\_\_.py to load the actual code
* tensorflow_core: most of the python and pre-compiled libraries
* tensorflow-2.0.0.data: 
* tensorflow-2.0.0.dist-info: metadata required by the wheel

The wheel contains the following pre-compiled libraries:

* tensorflow_core/python/_pywrap_tensorflow_internal.so, biggest file at 32MB
* tensorflow_core/compiler/tf2tensorrt/_wrap_py_utils.so
* tensorflow_core/compiler/tf2xla/ops/_xla_ops.so
* tensorflow_core/lite/experimental/microfrontend/python/ops/_audio_microfrontend_op.so
* tensorflow_core/lite/python/interpreter_wrapper/_tensorflow_wrap_interpreter_wrapper.so
* tensorflow_core/lite/python/optimize/_tensorflow_lite_wrap_calibration_wrapper.so
* tensorflow_core/python/framework/fast_tensor_util.so

It has the following outside dependencies:

* absl-py (>=0.7.0)
* astor (>=0.6.0)
* gast (==0.2.2)
* google-pasta (>=0.1.6)
* keras-applications (>=1.0.8)
* keras-preprocessing (>=1.0.5)
* numpy (<2.0,>=1.16.0)
* opt-einsum (>=2.3.2)
* six (>=1.10.0)
* protobuf (>=3.6.1)
* tensorboard (<2.1.0,>=2.0.0)
* tensorflow-estimator (<2.1.0,>=2.0.0)
* termcolor (>=1.1.0)
* wrapt (>=1.11.1)
* grpcio (>=1.8.6)
* wheel (>=0.26)
* backports.weakref (>=1.0rc1); python_version < "3.4"
* enum34 (>=1.1.6); python_version < "3.4"
