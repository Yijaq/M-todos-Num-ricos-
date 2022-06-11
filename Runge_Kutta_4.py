#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 13:29:12 2021

@author: YilberQuinto
"""

import numpy as np
import matplotlib.pyplot as plt


def Runge_Kutta_4(a, b, h0, y0, fun):
    '''
    El método de Runge-Kutta de orden 4 se utiliza para aproximar la solución del problema 
    de valor inical 
    
              y' = f(t,y),  t en [a,b], y(a) = y0.
              
    Parameters
    ----------
    a : Float
        Condición inicial en t (a = t0). extremo izq del intervalo [a,b]
        
    b : Float
        Extremo derecho del intervalo [a,b].
        
    h : float
        Tamaño de paso en t.
        
    y0 : Float
        Condicion inicial en y.
        
    fun : funtion 
        Función de dos variables f(t,y).
        

    Returns
    -------
    Aproximación w para y. 

    '''
    
    t = a 
    h = h0
    y = y0
    list_t = []
    list_y = []
    
    while t < b + h: 
        list_t.append(t)
        list_y.append(y)
        
        K1 = fun(t,y)
        K2 = fun(t + h/2, y + h*K1/2)
        K3 = fun(t + h/2, y + h*K2/2)
        K4 = fun(t + h, y + h*K3)
        
        y = y + h*(K1 + 2*K2 + 2*K3 + K4)/6
        t = t + h 
            
    return [list_t, list_y]   
        
#%%

def f1(t,y):
    return y - t**2 + 1

w = Runge_Kutta_4(0.0, 5.0, 0.2, 0.5, f1)   

def f2(t):
    return (t +1 )**2 -0.5*np.exp(t)

# Resultados: las dos componentes juntas
plt.plot(w[0],w[1]) 
plt.plot(w[0],f2(np.array(w[0])))
plt.show() 