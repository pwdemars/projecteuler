#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Project Euler 75 

TODO: ensure that a + b + c <= l 

Approach: 
    1. Create arrays a_arr and b_arr of dimension (limit/2, limit/4) with np.indices. 
    2. Fill the top right diagonals of a_arr and b_arr with nans. This assures
    that b > a 
    3. Square the two arrays and add them to give c_sq_arr
    4. Square root the result to produce c_arr
    5. Apply modulo 1 to c_arr (check if integer) to get c_mod
    6. The index of places where c_mod == 0 give a and b, and c_arr[a,b] gives 
    the values for c. 

"""

import numpy as np
import time
    
limit = 10000
s0 = time.time()
s = time.time()

a_arr, b_arr = np.add(np.indices((int(limit/2), int(limit/4)), dtype=float), 1)

for i in range(1, a_arr.shape[1]):
    np.fill_diagonal(a_arr[:,i:], np.nan)
    np.fill_diagonal(b_arr[:,i:], np.nan)

print("Fill diagonals: {:.2f}s".format(time.time()-s))
s = time.time()

c_sq_arr = np.square(a_arr) + np.square(b_arr)

print("Square arrays: {:.2f}s".format(time.time()-s))
s = time.time()

c_arr = np.sqrt(c_sq_arr)

print("Square root c arrays {:.2f}s".format(time.time()-s))
s = time.time()

c_mod = np.mod(c_arr, 1)

print("Modulo arrays: {:.2f}s".format(time.time()-s))
s = time.time()

ans = np.where(c_mod == 0)
c = c_arr[ans]
ans = np.add(ans, 1)
a = ans[1]
b = ans[0]

print("Get a's, b's and c's: {:.2f}s".format(time.time()-s))

ls = a + b + c 

print("TOTAL TIME: {:.2f}s".format(time.time()-s0))
# TODO: remove duplicates
# TODO: count ls 
