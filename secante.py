#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 13:50:08 2021

@author: Yilber Quinto
"""
import numpy as np
import matplotlib.pyplot as plt

def secante(f, x0, x1, tol, M):
    """
    

    Parameters
    ----------
    f :  Función 
         Función de números reales 
    x0 : float
         Punto inicial
    x1 : float
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
    i = 0
    print('    n   x_n           e_n')
    print('    -----------------------------')
    while i < M: 
        x = (x0*f(x1) - x1*f(x0))/(f(x1) - f(x0))
        e = np.abs((x - x1)/x)
        print(f'{i+3:>5d}   {x:>10.8f}   {e:>10.8f}')
        if e < tol:
            return x
        else:
            x0 = x1
            x1 = x
        i = i + 1
    if i == M:
        print(f'No se logró una aproximacón despues de {M} iteraciónes')

#----------------------------------------------------------------------------

#_______________Taller 1 ______Ejercicio 6____________________________________
def f1(w):
    g = 32.17
    t = 1
    return 1.7 + g/(2.0*w**2) * ((np.exp(w*t)-np.exp(-w*t))/2.0 - np.sin(w*t))

#-----------------------------------------------------------------------------
#_______________Taller 1 ______Ejercicio 11___________________________________ 

def fun11(t):
    s0 = 300 
    m  = 0.25
    k  = 0.1 
    g  = 32.17
    return s0 - (m*g/k)*t + (m**2)*g/(k**2) * (1 - np.exp(-k*t/m))

#-----------------------------------------------------------------------------
#_______________Taller 1 ______Ejercicio 18___________________________________ 

def fun18a1(x):
    return x**3 - np.sinh(x) + 4*(x**2) + 6*x + 9


def fun18a2(x):
    return np.exp(x) - np.tan(x)


#-----------------------------------------------------------------------------   
       
x =  secante(fun18a2, 1, 1.2, 1e-5, 50)


#%%
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('f1(x)')    
plt.grid() # visualiza la cuadricula en la figura    
plt.ylim(-10, 20)    
    
z = np.linspace(-5,11, 1000)
y = fun18a2(z)

#y2 = np.sin(z)*f(z)

plt.plot(z,y, label='f1')
#plt.plot(z,y2, label='f2')

plt.legend(loc='upper left')

plt.show()
        