---
title: "Mask R Cnn"
date: 2020-01-01T08:03:31-08:00
draft: true
type: notes
categories:
  - General
tags:
  - ai,image
series:
---

 Mask R-CNN, extends FasterR-CNN by adding a branch for predicting an object mask in parallel with the existing branch for bounding box recognition. 
 
<!--more-->



{{< figure src="/notes/mask-r-cnn/fig1.png" width="400" >}}

Here is the [Mask R-CNN arxiv](https://arxiv.org/pdf/1703.06870.pdf).

## Implementations

The Mask R-CNN implementation is part of [Detectron](https://github.com/facebookresearch/Detectron) which has been superseeded by [Detectron2](https://github.com/facebookresearch/Detectron2).

Nice implementation from [matterport](https://github.com/matterport/Mask_RCNN)

