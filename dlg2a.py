# -*- coding: utf-8 -*-
"""
Created on Sat Aug 05 21:21:23 2017

@author: hannamj
"""

def standardize(x, mean, stdev):
    return (x - mean) / stdev

print standardize(60, 90, 5)
