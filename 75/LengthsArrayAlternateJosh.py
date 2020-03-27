#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 11:38:46 2020

@author: joshuajacob
"""

import numpy

import time 
t0 = time.time()

L = 1000

Lengths = numpy.zeros(L+1, dtype = numpy.int8) 

side_squared = numpy.array([x for x in range(1,L+1)])**2

cees = numpy.array([[((side_squared[a] +  side_squared[b])**0.5)+a+b+2 if b<a and a+b+2 < 2*L/3 else 0 for b in range(L)] for a in range(L)])

cees *= (cees % 1 == 0.0)

cees = numpy.hstack(cees)

cees = numpy.minimum(cees, L+1)

print(numpy.count_nonzero(numpy.unique(cees,return_counts = True)[1] == 1))

t1 = time.time()
print(t1-t0)