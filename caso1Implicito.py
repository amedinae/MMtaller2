# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 22:36:03 2020

@author: Andres Medina
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

D = 1.8 #m**2/s
L = 0.9 #m
U = 0.2 #m/s
c_ref = 0.1 #kg/m**3
k = 5 #k**-1
dt = 0.01
tf = 10
it = int(tf/dt)
dx = 0.02
n = int(L/dx)+1
nodos = n

mat_futura = np.zeros((nodos,nodos))
C = np.zeros(nodos)
vec_F = np.zeros(nodos)

mat_C = np.zeros((nodos,it+1))

eq = 0 

for i in range(n):
    nc = eq
    nl = nc - 1
    nr = nc + 1
    if (i == 0):
        mat_futura[eq,nc] = 2*D*dt/dx**2+2*U*dt/dx + U**2*dt/D+ k*dt + 1
        mat_futura[eq,nr] = -2*D*dt/dx**2

        vec_F[eq] = (2*U*dt/dx + U**2*dt/D)*c_ref
        #print("Nodos a la izquierda")
    elif (i<n-1):
        mat_futura[eq,nc] = 2*D*dt/dx**2+k*dt + 1
        mat_futura[eq,nl] = -D*dt/dx**2 - U*dt/(2*dx)
        mat_futura[eq,nr] = -D*dt/dx**2 + U*dt/(2*dx)
        
        #print("Nodos internos")
    else:
        mat_futura[eq,nc] = 2*D*dt/dx**2+k*dt + 1
        mat_futura[eq,nl] = -2*D*dt/dx**2
        
        #print("Nodo a la derecha")
    eq += 1

minv = np.linalg.inv(mat_futura)

for j in range(1,it+1):
    #print("iteracion: ",j)
    C = minv@(C + vec_F)
    mat_C[:,j] = C

x = np.zeros(n)
for i in range(n):
    x[i] = dx*(i)

#plt.plot(x,mat_C[:,int(0.01*it)],label="t=0.1 s")  
#plt.plot(x,mat_C[:,int(0.02*it)],label="t=0.2 s")  
#plt.plot(x,mat_C[:,int(0.03*it)],label="t=0.3 s")  
#plt.plot(x,mat_C[:,int(0.04*it)],label="t=0.4 s")  
plt.plot(x,mat_C[:,int(0.05*it)],label="t=0.5 s")  
#plt.plot(x,mat_C[:,int(0.06*it)],label="t=0.6 s")  
#plt.plot(x,mat_C[:,int(0.07*it)],label="t=0.7 s")  
#plt.plot(x,mat_C[:,int(0.08*it)],label="t=0.8 s")  
#plt.plot(x,mat_C[:,int(0.09*it)],label="t=0.9 s")  
plt.plot(x,mat_C[:,int(0.1*it)],label="t=1 s") 
#plt.plot(x,mat_C[:,int(0.12*it)],label="t=1.2 s") 
#plt.plot(x,mat_C[:,int(0.13*it)],label="t=1.3 s")    
plt.legend(loc="upper right")
plt.xlabel('Distancia (m)')
plt.ylabel('Concentración (C)')
plt.grid()
plt.show()    