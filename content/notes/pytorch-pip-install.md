---
title: "Pytorch Install"
slug: pytorch-install
date: 2019-12-25T20:09:36-08:00
draft: false
type: notes
categories:
  - General
tags:
  - ai
series:
  -

---
Dependencies and steps through which Pytorch gets installed on your development machine. 

<!--more-->
## Intro

As of Dec 2019, the instructions to install Pytorch are here
[instructions](https://pytorch.org/get-started/locally/) and one options is to run:

```
$  pip install torch torchvision
```

To learn more about pip see the [pip note]({{< ref "/notes/python-packages.md">}}).

## Wheels for torch

For python 3.7 Pytorch is provided through 2 [files](https://pypi.org/project/torch/#files), one per operating system:

* torch-1.3.1-cp37-cp37m-manylinux1_x86_64.whl
* torch-1.3.1-cp37-none-macosx_10_7_x86_64.whl

As opposed to TF there is no support wheel for windows. Also TF uses the newer manylinux2010 platform tag.


### File summary

This is a summary of the files in the macos wheel.

{{< fileSummary "torch-wheel" >}}


### Outside dependencies

As opposed to [TF]({{< ref "/notes/tf-pip-install.md" >}}), Pytorch only has one external dependency. 

* numpy

Also CUDA support is provided in the base install.