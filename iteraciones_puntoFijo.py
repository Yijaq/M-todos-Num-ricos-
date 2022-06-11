#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 22 19:06:52 2021

@author: YilberQuinto
"""

import numpy as np

x0 = 2.5
x1 = 5/np.sqrt(x0)
q  = 5/16
p  = 25**(1/3)
a  = (np.log(p*(1 - q)*1e-6/np.abs(x1 - x0)))/np.log(q)
print(a)