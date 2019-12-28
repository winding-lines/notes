---
title: "Argoverse"
slug: argoverse
description: null
date: 2019-12-28T06:51:08-08:00
type: posts
draft: false
categories:
- General
tags:
- AV
series:
-
---

These are notes from the Argoverse competition with the goal of providing curated datasets and high-definition (HD) maps designed to support advancements in computer vision and machine learning.

<!--more-->
The main site is here [Argoverse](https://www.argoverse.org).

## Baseline

The [baseline repo](https://github.com/jagjeet-singh/argoverse-forecasting) is a good starting point.

## Evaluation metrics

The [eval_forecasting_helper](https://github.com/jagjeet-singh/argoverse-forecasting/blob/master/eval_forecasting_helper.py) generates the following metrics using [argoverse-api/.../eval_forecasting.py](https://github.com/argoai/argoverse-api/blob/87c5e3f2d2eb039052e142d5e30bb7d6caeb6252/argoverse/evaluation/eval_forecasting.py#L136)

* mean_min_ade: Mean of min average displacement error for all the trajectories.
* mean_min_fde: Mean of min final displacement error for all the trajectories.
* mean_dac: Mean drivable area compliance for all the trajectories.
* miss_rate: Miss rate.
