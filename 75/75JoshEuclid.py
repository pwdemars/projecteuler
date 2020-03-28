#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 10:23:04 2020

@author: joshuajacob

Singular integer right triangles.
"""
import numpy
import math 
import time

s = time.time()

l = 1500000
lengths = numpy.zeros(l+1, dtype=numpy.int8)

m = 2

while m <= l/4:
    n = m%2 + 1
    while m*n <= l/4 and n < m:
        if math.gcd(m,n) == 1:
            i = 2*(m**2)+2*m*n
            lengths[i::i] += 1 
        n += 2
    m += 1
        
answer = numpy.count_nonzero(lengths == 1)
print("Answer: {}".format(answer))
print("Time taken: {:.2f}s".format(time.time()-s))