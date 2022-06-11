#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 16:02:44 2021

@author: Yilber Quinto
"""

import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

def punto_fijo(g, x0, tol, M):
    """
    

    Parameters
    ----------
    f : Función
        Función de Números reales contracción 
    x0 : float
        Punto inicial
    tol : float
        Tolerancia
    M : int
        Número máximo de interaciones 

    Returns
    -------
    Exito "El cero de la funcion es x = p"
    
    Fracaso " El método fracasó después de M interaciones "

    """
    
    
    valores = [x0]
    error   = [np.nan]
    
    p = 25**(1/3)
    
    i = 0
    while i < M:
        x = g(x0)
        e = np.abs((x - p)/p)
        
        valores.append(float(f'{x:.10f}'))
        error.append(float(f'{e:.10f}'))
        
        if e < tol: 
            df = pd.DataFrame({'x_n':valores,'e_n':error})
            df.to_excel('Tabla_método_punto_fijo.xlsx') 
            print(pd.read_excel("Tabla_método_punto_fijo.xlsx",index_col=0))
            print('')
            print(f'El cero de la función es: {x:.9f}')
            return x
        else:
            x0 = x
        i = i + 1
        
    if i == M:
        df = pd.DataFrame({'x_n':valores,'e_n':error})
        df.to_excel('Tabla_método_PuntoFijo.xlsx') 
        print(pd.read_excel("Tabla_método_punto_fijo.xlsx",index_col=0))
        print(f'No se logró la aproximacón deseada despues de {M} iteraciónes')    


#%%

def f1(x):
    return 5/(x**(1/2))

x = punto_fijo(f1, 3.0, 1e-6, 40)

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('f1(x)')    
plt.grid() # visualiza la cuadricula en la figura    
plt.ylim(-1.5, 1.5)    
    
z = np.linspace(0.1,4, 100)
y = f1(z)

#y2 = np.sin(z)*f(z)

plt.plot(z,y, label='f1')
#plt.plot(z,y2, label='f2')

plt.legend(loc='upper left')

plt.show()
             