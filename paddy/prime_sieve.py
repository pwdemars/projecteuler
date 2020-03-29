#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:29:17 2020

@author: patrickdemars
"""

def prime_sieve(limit):
    """
    Generator for primes up to value limit.
    
    Adapted from algorithm found on stack overflow 
    """
    x = [True] * limit 
    x[0] = False
    x[1] = False
    
    for i, isprime in enumerate(x):
        if isprime:
            yield i
            n = i
            while n < limit:
                x[n] = False
                n += i
