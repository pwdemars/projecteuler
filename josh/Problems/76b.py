#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 17:26:30 2020

@author: joshuajacob
"""

import numpy 

n = 100

x = numpy.zeros((100,100))

a = 0

while a < n:
    b = 0
    x[a][b] = 1
    while b < a:
        if b < a/2:
            x[a][b+1] = sum(x[b])
        else:
            x[a][b+1] = sum(x[b][-a+b+b+1:b+2])
        b += 1
    a += 1

