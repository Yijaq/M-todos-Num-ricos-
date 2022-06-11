#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:45:01 2021

@author: Yilber Quinto
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def newton(f, df, x0, tol, M):
    '''
    

    Parameters
    ----------
    f : Función
         Función de números reales 
         
    df : Función
         Derivada de la función f
         
    x0 : float
         Punto inicial x0
         
    tol : float
          Tolerancia 
          
    M : int 
        Número máximo de interaciones     


    Returns
    -------
    Exito "El cero de la funcion es x = p"
    
    Fracaso " El método fracasó después de M interaciones "

    '''
    
    
    valores = [x0]
    error   = [np.nan]
    
    i = 0
    while i < M: 
        x = x0 - f(x0)/df(x0)
        e = np.abs((x - x0)/x)
        
        valores.append(float(f'{x:.9f}'))
        error.append(float(f'{e:.9f}'))
        
        if e < tol:
            df = pd.DataFrame({'x_n':valores,'e_n':error})
            df.to_excel('Tabla_método_Newton.xlsx') 
            print(pd.read_excel("Tabla_método_Newton.xlsx",index_col=0))
            print('')
            print(f'El cero de la función es: {x:.9f}')
            return x 
        else:
            x0 = x
        i = i + 1    
    if i == M:
        df = pd.DataFrame({'x_n':valores,'e_n':error})
        df.to_excel('Tabla_método_Newton.xlsx') 
        print(pd.read_excel("Tabla_método_Newton.xlsx",index_col=0))
        print(f'No se logró una aproximacón despues de {M} iteraciónes')

        
#%%


#_______________Taller 1 ______Ejercicio 6___________________________________
def f1(w):
    g = 32.17
    t = 1
    return 1.7 + g/(2.0*w**2) * ((np.exp(w*t)-np.exp(-w*t))/2.0 - np.sin(w*t))

#-----------------------------------------------------------------------------    
def f(x):            # f(x) =x^2 -1
   return x**2 -1

def df(x):            # Derivada de f
   return 2*x 



#%%

#_______________Taller 1 ______Ejercicio 11___________________________________ 

def fun11(t):
    s0 = 300 
    m  = 0.25
    k  = 0.1 
    g  = 32.17
    return s0 - (m*g/k)*t + (m**2)*g/(k**2) * (1 - np.exp(-k*t/m))

def dfun11(t):          # Derivada de fun11
    m  = 0.25
    k  = 0.1 
    g  = 32.17
    return   m*g/k *( -1 + np.exp(-k*t/m))




#%%
#_______________Taller 1 ______Ejercicio 13___________________________________ 

def fun13(t):
    A = np.exp(1)/3
    return -0.25 + A*t*np.exp(-t/3)

def dfun13(t):
    A = np.exp(1)/3
    return  A*np.exp(-t/3)*(1 - t/3)

x =  newton(fun13, dfun13, 4.0, 1e-5, 50)

#%%

#-----------------------------------------------------------------------------
#_______________Taller 1 ______Ejercicio 18___________________________________ 

def fun18a1(x):
    return x**3 - np.sinh(x) + 4*(x**2) + 6*x + 9

def dfun18a1(x):
    return x**2 - np.cosh(x) + 8*x + 6 
#---------------------------------------------------------

def fun18a2(x):
    return np.exp(x) - np.tan(x)


def dfun18a2(x):
    return np.exp(x) - 1/(np.cos(x))**2 




#-----------------------------------------------------------------------------
        
x =  newton(fun13, dfun13, 4, 1e-5, 50)


#%%

fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('f1(x)')    
plt.grid() # visualiza la cuadricula en la figura    
plt.ylim(-10, 10)    
    
z = np.linspace(0,2, 100)
y = fun13(z)

y2 = np.sin(z)*f(z)

plt.plot(z, y, label='f1')
plt.plot(z,y2, label='f2')

plt.legend(loc='upper left')

plt.show()

