#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 17:30:45 2020

@author: joshuajacob
"""

import time
t0 = time.time()
n = 50


count = 1

solutions = [[] for x in range(n)]

while count < n:
    if count <= n/2:
        solutions[-count] += [[count]]
    m = 1
    while m < n/2 and m < count:
        counter = 0
        for x in solutions[-count+m]:
            if min(x) >= m:
                if max(x) <= n - count:
                    solutions[-count] += [x + [m]]
                    counter += 1
        if m == 20 :
            print(counter,m,count)
        
        #solutions[-count] += [x + [m] for x in solutions[-count+m] if min(x) >= m and max(x) <= n-count]
        m += 1
        
    count += 1

solutions = [[[a]+y for y in solutions[a]] for a in range(n)]

print(1+sum(len(x) for x in solutions))
t1 = time.time()
print(t1-t0)