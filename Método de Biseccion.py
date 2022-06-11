import numpy as np

# numpy:  funciones numericas
# matplotlib : graficas
# scipy : computacion cientifica

import matplotlib.pyplot as plt


#from numpy import *   # carga toda la libreria numpy

# Considere una funcion f(x) definida en un intervalo [a,b]
# La funcion f debe tener un cambio de signo en [a,b]

# Buscamos un cero de f en el intervalo [a,b] es decir x tal que f(x) = 0
# a, b extremos del intervalo


def biseccion(f, a, b, tol):
    
    if a > b :
      raise ValueError('Intervalo mal definido')
    
    if f(a) * f(b) >= 0:
      raise ValueError('La funcion debe cambiar de signo en el intervalo')
    
       
    x = (a + b) / 2.0
    i = 0  
    print('    n   x_n           e_n')
    print('    -----------------------------')
    while True:
       e = b-a 
       print(f'{i+1:>5d}   {x:>10.9f}   {e:>10.9f}')
       if e < tol:
          return  x 
   # sale de la funcion biseccion()
       elif np.sign( f(a) ) * np.sign( f(x) ) > 0:     # sino si ....
          a = x  
       else:
          b = x 
       x = (a + b) / 2.0
       i = 1 + i
      # print(x)       
  
    
  
#_______________Taller 1 ______Ejercicio 6____________________________________
        
def f1(w):
    g = 32.17
    t = 1
    return 1.7 + g/(2.0*w**2) * ((np.exp(w*t)-np.exp(-w*t))/2.0 - np.sin(w*t))
    
def f(x):            # f(x) =x^2 -1
   return x**2 -1

#-----------------------------------------------------------------------------
#_______________Taller 1 ______Ejercicio 11___________________________________ 

def fun11(t):
    s0 = 300 
    m  = 0.25
    k  = 0.1 
    g  = 32.17
    return s0 - (m*g/k)*t + (m**2)*g/(k**2) * (1 - np.exp(-k*t/m))

#-----------------------------------------------------------------------------
#_______________Taller 1 ______Ejercicio 17___________________________________ 

def fun17(x):
    gamma = 1
    return x**2 * (1 - np.cos(x)*np.cosh(x)) - gamma*np.sin(x)*np.sinh(x)

#-----------------------------------------------------------------------------

def fun10(x):
    return x**2 - 3

#-----------------------------------------------------------------------------


x =  biseccion(fun10, 1, 2, 1e-4)


        
#%%
fig, ax = plt.subplots()
ax.set_xlabel('x')
ax.set_ylabel('f1(x)')    
plt.grid() # visualiza la cuadricula en la figura    
plt.ylim(-5, 5)    
    
z = np.linspace(1,3, 100)
y = fun10(z)

#y2 = np.sin(z)*f(z)

plt.plot(z,y, label='f1')
#plt.plot(z,y2, label='f2')

plt.legend(loc='upper left')

plt.show()

