---
title: "Low Level Libraries"
slug: libs
date: 2020-01-03T19:32:47-08:00
draft: false
---

Frequently use lower level libraries: numerical, multi processing.

<!--more-->

* [Blas](https://en.wikipedia.org/wiki/Basic_Linear_Algebra_Subprograms) - Basic Linear Algebra Subprograms
  - Intel [Math Kernel Library](https://software.intel.com/en-us/mkl-developer-reference-c-blas-and-sparse-blas-routines)

* [Eigen](https://eigen.tuxfamily.org)
  - Inside Eigen: https://eigen.tuxfamily.org/dox/TopicInsideEigenExample.html

* OpenMP: 
  - [wikipedia](https://en.wikipedia.org/wiki/OpenMP): application programming interface (API) that supports multi-platform shared memory multiprocessing programming in C, C++, and Fortran, on many platforms
  - [intel's guide](https://software.intel.com/en-us/articles/getting-started-with-openmp)


* [NCCL](https://github.com/NVIDIA/nccl):  Optimized primitives for collective multi-GPU communication
  * [documentation](https://docs.nvidia.com/deeplearning/sdk/nccl-developer-guide/index.html)
  * operations (ring algorithms):

      * all-reduce
      * all-gather
      * reduce-scatter
      * reduce
      * broadcast
