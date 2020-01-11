---
title: "Distributed Training"
date: 2020-01-11T06:35:00-08:00
draft: false
type: notes
categories:
  - General
tags:
  - training
series:
---

Frameworks and libraries for distributed training

<!--more-->

Overview from [lambdalabs](https://lambdalabs.com/blog/introduction-multi-gpu-multi-node-distributed-training-nccl-2-0/)

* multi gpu using parameter server: reduce and broadcast done on CPU
* multi gpu all-reduce in one one, using nccl
* asynchronous distributed SGD
* synchronous distributed SGD
* multiple parameter servers
* ring all reduce distributed training

## Low level

[gpudirect](https://developer.nvidia.com/gpudirect) from nvidia

  - 2019 Storage: from/to NVMe devices
  - 2013 RMDA: from/to network
  - 2011 GPU Peer to Peer: high speed DMA

## Frameworks

[Apache Spark](https://spark.apache.org/)

Tensorflow
* [distributed training](https://www.tensorflow.org/guide/distributed_training)

[Horovod](https://github.com/horovod/horovod)

* [paper](https://arxiv.org/pdf/1802.05799.pdf)
* part of [LF AI](https://lfai.foundation/)
* synchronous operation