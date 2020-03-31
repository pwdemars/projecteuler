#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 18:55:08 2020

@author: joshuajacob
"""

import numpy 

def primes_list_a(n):
    x = numpy.ones(n, dtype = numpy.bool)
    i = 2
    x[0] = x[1] = False
    while i<int((n**0.5)+1):
        if x[i]:
            x[2*i::i] = False
        i += 1
    return([j for j in x*[k for k in range(n)] if j])
    


n = 100

x = numpy.zeros((100,100))

a = 0


primes = primes_list_a(n)

while a < n:
    b = 0
    if a in primes:
        x[a][0] = 1
    while primes[b] < a:
        if a-primes[b] <= primes[b]:
            x[a][a-primes[b]] = sum(x[a-primes[b]])
        else:
            x[a][a-primes[b]] = sum(x[a-primes[b]][a-primes[b]-primes[b]:a-primes[b]+2])
        b += 1    
    if sum(x[a]) > 5000:
                print(a, sum(x[a]))
                a = n 
                b = n
                
    a += 1