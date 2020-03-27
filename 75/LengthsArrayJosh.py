#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 22:55:21 2020

@author: joshuajacob
"""

import numpy

import time 

t0 = time.time()

L = 1000

#limits = numpy.array([[1 if y<x and y+x+2 < 2*L/3 else 0 for y in numpy.arange(L)] for x in numpy.arange(L)])

Lengths = numpy.zeros(L+1, dtype = numpy.int8) 

side_squared = numpy.array([x for x in range(1,L+1)])**2

cees = numpy.array([[((side_squared[a] +  side_squared[b])**0.5) if b<a and a+b+2 < 2*L/3 else 0 for b in range(int(L))] for a in range(L)])

#side_sum = numpy.array([side_squared[y] +  side_squared[:] for y in numpy.arange(int(L))])

#side_sum *= limits

#cees = side_sum**0.5 

cees *= (cees % 1 == 0.0)



count = 0
for a in range(L):
    for b in range(L):
        if cees[a][b] != 0 and cees[a][b]+a+b+2 <= L:
            Lengths[a+b+2+int(cees[a][b])] += 1
            
print(numpy.count_nonzero(Lengths == 1))

t1 = time.time()
print(t1-t0)