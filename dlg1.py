# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 21:06:15 2017

@author: hannamj
"""

import numpy as np
import matplotlib.pyplot as plt

pi = np.pi

print np.sin(pi / 2)

x = np.linspace(0,2*pi, 100)
y = np.sin(x)

plt.plot(y)
