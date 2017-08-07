# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 21:16:27 2017

@author: hannamj
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

def f(x):
    return ss.norm.cdf(x, loc = 18, scale=0.09)

print f(17.91)


