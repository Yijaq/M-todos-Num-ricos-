#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:44:48 2021

@author: YilberQuinto
"""

import numpy as np

L = np.array([[2, 0, 0],[-1/2, 1/2 * np.sqrt(19), 0],[0, 6/np.sqrt(19), 2*np.sqrt(10/19)]])
A = L@L.T

print('')
print('L es igual a ')
print('')
print(L)
print('')
print('A es igual a ')
print('')
print(A)