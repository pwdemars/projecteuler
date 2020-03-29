#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Solution to Project Euler problem 1:

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

import numpy as np 

# Initialise x, a boolean array of length 1000
limit = 1000 
x = np.zeros(limit, dtype=bool)

# Set all multiples of 3 in x to true
i = 3
while i < limit:
    x[i] = True
    i+=3
    
# Set all multiples of 5 in x to true
i = 5
while i < limit:
    x[i] = True
    i+=5

# Get indices set to true 
t = np.where(x)

# Sum up the indices 
ans = np.sum(t)

print("Answer: {}".format(ans))
