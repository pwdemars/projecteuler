#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 13:38:14 2020

@author: patrickdemars
"""

import numpy as np 

limit = 100
x = np.zeros(limit, dtype=bool)

i = 3
while i < limit:
    x[i] = True
    i+=3
    
i = 5
while i < limit:
    x[i] = True
    i+=5
    