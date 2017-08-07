# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 21:10:29 2017

@author: hannamj
"""

import numpy as np
import matplotlib.pyplot as plt

N = np.random.randn(10000)

plt.hist(N, bins=10)

