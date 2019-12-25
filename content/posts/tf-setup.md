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

The instructions to install Tensorflow (TF) are here (instructions)[https://www.tensorflow.org/install].

## The pip ecosystem

In order to install Tensorflow you need to have pip 19 or better, where pip is a part of the python ecosystem. you can see the changes in the [pip changelog](https://pip.pypa.io/en/stable/news/).

## pip 19

It is interesting that TF requires a specific version of pip. Some notable changes in pep 19 are below:

- support for [PEP-0517](https://www.python.org/dev/peps/pep-0517/)
- `manylinux2010` platform tag support which allows binary wheels to be installed on compatible linux libraries

It is unclear how these or additional changes are needed for TF setup, the requirement may simply force the usage of a newer verion of pip.

### wheels

Wheels are a zip file withe the extension `whl` and are defined in [PEP-0427](https://www.python.org/dev/peps/pep-0427/)

## running pip

According to the [TF install page](https://www.tensorflow.org/install) one should run:

```shell
pip install tensorflow
```

To keep your local dev environment clean you should setup and activate a [venv](https://docs.python.org/3/library/venv.html)

When running [pip install](https://pip.pypa.io/en/stable/reference/pip_install/) the following happens:

- TODO