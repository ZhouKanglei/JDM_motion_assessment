#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/fbx/2 上午10:18

from utils.visualize_frames import visualise_frames
import numpy as np

arr = np.load('data/npz/JDM_motion.npz')
print(arr['data'].shape)
print(arr['label'])

visualise_frames()
