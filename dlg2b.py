# -*- coding: utf-8 -*-
"""
Created on Sun Aug 06 17:36:29 2017

@author: hannamj
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as ss

sals = [8.75, 8.75, 8.90, 9.00, 9.00, 9.00, 9.00, 10.15]

desc = ss.describe(sals)

names = ["length", "min", "max", "mean", "stdev"]
desc = [desc[0], desc[1][0],desc[1][1], desc[2],desc[3]]

for i in range(5):
    print "%s: %d" % (names[i], desc[i])
