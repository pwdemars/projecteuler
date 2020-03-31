#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:05:56 2020

@author: joshuajacob
"""

import numpy 

n = 10000

x = numpy.zeros((10000,10000))

a = 0

while a < n:
    b = 0
    x[a][b] = 1
    while b < a:
        if b < a/2:
            x[a][b+1] = sum(x[b])
        else:
            x[a][b+1] = sum(x[b][-a+b+b+1:b+2])
        b += 1
    
    if sum(x[a]) % 100 == 0:
        if sum(x[a]) % 1000 == 0:
            if sum(x[a]) % 10000 == 0:
                if sum(x[a]) % 100000 == 0:
                    if sum(x[a]) % 1000000 == 0:
                        print('1000000',a, sum(x[a]))
                        a = n
                    else:
                        print('100000',a, sum(x[a])%1000000)
                else:
                    print('10000',a, sum(x[a])%100000)
            else:
                print('1000',a, sum(x[a])%10000)
        else:
            print('100',a, sum(x[a])%1000)
    a += 1
