#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 16:24:01 2021

@author: YilberQuinto
"""


import numpy as np
import pandas as pd



def gauss_seidel(A, b, x0, M = 100, tol = 1e-5):
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

        list_xi = []   

        for i in np.arange(n):  
            
            suma1 = 0
            for j in np.arange(i):
                suma1 = suma1 + a[i][j] * list_xi[j]
                
            suma2 = 0
            for j in np.arange(i+1,n):
                suma2 = suma2 + a[i][j] * x0[j]
            
            xi = 1/a[i][i] * (b[i] - suma1 - suma2)
            list_xi.append(xi)    
                     
        x = np.array(list_xi)
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

x = gauss_seidel(A, b, x0, 15)
