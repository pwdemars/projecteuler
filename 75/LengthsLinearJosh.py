#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 23 19:20:06 2020

@author: joshuajacob
"""

import numpy

import time
t0 = time.time()
A = 3

L = 100

Lengths = numpy.zeros(L, dtype = numpy.int8) 

while A < L/2: 
    B = int((2*A+1)**0.5)
    while B < A and A+B < 2*L/3:
        if ((A**2 + B**2)**0.5) % 1 == 0.0:
            C = (A**2 + B**2)**0.5
            if A + B + C <= L:
                Lengths[A + B + int(C)-1] += 1
        
        B+=1
    A+=1
   

print(numpy.count_nonzero(Lengths == 1))

print(Lengths)

t4 = time.time()
print(t4-t0)



