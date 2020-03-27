#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:08:47 2020

@author: patrickdemars
"""

import numpy as np
import time

s=time.time()
limit = 20000
ans = []
ls = np.array([])
for a in range(1, int(limit/2)):
    b_arr = np.arange(a, limit-a)
    a_arr = a*np.ones(b_arr.size)
    c_sq_arr = np.square(a_arr) + np.square(b_arr)
    c_arr = np.sqrt(c_sq_arr)
    idx = np.where(c_arr % 1 == 0)[0]
    if idx.size != 0:
        l = a_arr[idx] + b_arr[idx] + c_arr[idx]
        ls = np.append(ls, l)
#        print(a_arr[idx], b_arr[idx], c_arr[idx])

_, counts = np.unique(ls, return_counts=True)
idx = np.where(counts == 1)
unique_ls = ls[idx]

print("Time taken: {:.2f}s".format(time.time()-s))
print("Number of unique l: {}".format(unique_ls.size))


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



for a in range(1, limit):
    for b in range(a, limit-a):
        c_sq = np.square(a) + np.square(b)
        c = np.sqrt(c_sq)
        is_square = c % 1 == 0
        if is_square:
            ans.append([a,b,int(c)])

ans_np = np.array(ans)
np.unique(ans_np)