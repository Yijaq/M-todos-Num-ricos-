import numpy as np
import matplotlib.pyplot as plt



def f(t, x_vec):
    # tratar x_vec como vector!
   
    xx, yy = x_vec[0], x_vec[1]
    return np.array([yy, -xx])	


def euler(t,x, h, f):
    return f(t,x)


# Datos iniciales
t_final = 10.

h = 0.01 # tamano de paso : da 1000 pasos

x0 = np.array( [1., 0. ] )


# Inicializacion de variables
lista_t  = []  # Lista de tiempos: escalar
lista_x = []   # Lista de los valores de la solucion x : vector

x = x0
t = 0.

while t < t_final+h:		# para incluir t_final
        lista_t.append(t)
        lista_x.append(x.copy())	
        
        #x.copy() hace una copia de x como una lista
        #lista_x.append(list(x))  otra manera

        x += h*euler(t,x, h , f)  #  x = x + h*euler(t,x,h,f )
        t += h  # t = t + h
        

# Resultados: las dos componentes juntas
plt.plot(lista_t, lista_x )        
plt.show()


#Componente 0: 
lista_x0 = [ lista_x[i][0] for i in range(len(lista_t))  ]
plt.plot(lista_t, lista_x0 )
plt.show()

#Componente 1:
lista_x1 = [ lista_x[i][1] for i in range(len(lista_t) )  ]
plt.plot(lista_t, lista_x1 )
plt.show()
