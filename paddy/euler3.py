#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 12:04:25 2020

@author: patrickdemars
"""

import time

def get_largest_prime_factor(n):
    d = 2 
    factors = []
    while n > 1: 
        while n % d == 0:
            n /= d
            factors.append(d)
        d += 1 
        
    return factors
            
a = 600851475143
s = time.time()
factors = get_largest_prime_factor(a)
answer = max(factors)
print("answer: {}".format(answer))
print("time taken: {}s".format(time.time()-s))