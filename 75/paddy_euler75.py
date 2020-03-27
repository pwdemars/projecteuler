#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:08:47 2020

@author: patrickdemars
"""

import numpy as np
import time
    
limit = 20000
s = time.time()

a_arr = np.ones((int(limit/2)-1, int(limit/2)-1))    
a_arr = a_arr * np.arange(1, int(limit/2))

print("Init a array: {:.2f}s".format(time.time()-s))
s = time.time()

b_arr = np.copy(a_arr).T

print("Init b array: {:.2f}s".format(time.time()-s))
s = time.time()

w = a_arr.shape[1]
a_arr = a_arr[:,:int(w/2) - w%2]
b_arr = b_arr[:,:int(w/2) - w%2]

print("Truncate arrays: {:.2f}s".format(time.time()-s))
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
a = ans[0]
b = ans[1]

print("Get answer: {:.2f}s".format(time.time()-s))

ls = a + b + c 
np.max(ls)
