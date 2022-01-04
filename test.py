#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time: 2022/raw/2 上午10:18

from utils import *
import numpy as np

arr = np.load('./data/tmp/JDM_motion.npz')
print(arr['data'].shape)
print(arr['label'])