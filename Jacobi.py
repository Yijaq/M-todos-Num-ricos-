#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 17:39:48 2021

@author: YilberQuinto
"""

import numpy as np
import pandas as pd



def jacobi(A, b, x0, tol, M):
    '''
    El método de Jacobi es un método iterativo utilizado para resolver sistemas
    lineales Ax = b.

    Parameters
    ----------
    A : Matriz 
        A es una matriz cuadrada nxn.
        
    b : Vector (array)
        b es vector nx1.
        
    x0 : Vector (array)
        x0 es un vector nx1.
        
    tol : float 
        Precisión deseada.
        
    M : inter
        Máximo número de iteraciones.


    Returns
    -------
    Éxito: Se obtuvo una aproximacón x := (xi)nx1.
    
    Fracaso: No se logro la precisión deseada despues de M iteracione  
    '''
    n = A.shape[0]
    a = A
    
    lista = [x0]
    lista_error = [np.nan]
    
    for k in np.arange(M + 1):
        
        list_x = [] 
        
        for i in np.arange(n):  
            
            suma = 0
            for j in np.arange(n):
                if j == i:
                    pass
                else:
                    suma = suma + a[i][j] * x0[j]
            
            xi = 1/a[i][i] * (b[i] - suma)
            list_x.append(xi)
            
        x = np.array(list_x)
        error = np.linalg.norm(x - x0)         # Norma euclideana de x - x0
        
        lista.append(x)
        lista_error.append(error)
        
        if error < tol:
            df = pd.DataFrame({'x_k':lista,'e_k':lista_error})
            df.to_excel('Tabla_Jacobi.xlsx') 
            print(pd.read_excel("Tabla_Jacobi.xlsx",index_col=0))
            print('')
            print(f' Éxito: Se obtuvo una aproximacón x := {x}.')
            return x 
        else:
            x0 = x
            
    if k == M:
        return print(f'Fracaso: No se logro la precisión deseada despues de {M} iteraciones')
    
#%%

A = np.array([[5, -1, 1], [2, 8, -1], [-1, 1, 4]])
b = np.array([10, 11, 3])
x0 = np.array([0, 0, 0])

x = jacobi(A, b, x0, 1e-5, 15)


    