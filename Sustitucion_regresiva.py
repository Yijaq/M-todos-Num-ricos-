#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  8 14:25:29 2021

@author: YilberQuinto
"""

import numpy as np


def sustitucion_regresiva(R, c):
    '''
    Algoritmo de sustitución regresiva. Determina el vector x, tal que Rx = c

    Parameters
    ----------
    R : Matriz diagonal suoerior de nxn 
        R := (r_ij)nxn .
        
    c : Matriz de 1xn
        c := (c_i)1xn.

    Returns
    -------
    x : Matriz de 1xn
        x := (x_i)1xn.

    '''
    n = R.shape[0]             # Dimensión de los vectores c y x: R^n
    r = n-1                    # Indexación Python 
    
    x = np.zeros((1,n))
    xr = (c[0][r])/(R[r][r])
    x[0][r] = xr
    
    for i in np.arange(r-1,-1,-1):
        suma = 0
        
        for j in np.arange(i+1,r+1):
            suma = suma + R[i][j] * x[0][j]
            
        x[0][i] = (c[0][i] - suma)/R[i][i]     
    return x         

#%%

R = np.array([[1,2,1,-1],[0,-1,3,0],[0,0,-2,-3],[0,0,0,2]])
c = np.array([[1,3,-1,-1]])

x = sustitucion_regresiva(R,c)
b = R @ x.T                      # x.T es la trasnpuesta de x

print('')
print(f'x = {x}')
print('')
print(f'Rx = {b.T}') 
print('')
print(f'c = {c}')
print('')

