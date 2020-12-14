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
tao = L/U
dt = 0.01/tao
tf = 10/tao
it = int(tf/dt)
dx = 0.02/L
n = int(1/dx)+1
nodos = n

mat_futura = np.zeros((nodos,nodos))
C = np.zeros(nodos)
vec_F = np.zeros(nodos)

mat_C = np.zeros((nodos,it+1))

eq = 0 

a0 = D/(L*U)
a1 = k*L/U
a2 = U*L/D

b = 2*a0*dt/dx**2
b5 = b + a1*dt + 1
b6 = -b/2 + dt/(2*dx)
b7 = -b/2 - dt/(2*dx)
b8 = 2*a2*a0*dt/dx + a2*dt


for i in range(n):
    nc = eq
    nl = nc - 1
    nr = nc + 1
    if (i == 0):
        mat_futura[eq,nc] = b5+b8
        mat_futura[eq,nr] = -b #b6+b7

        vec_F[eq] = -b8
        #print("Nodos a la izquierda")
    elif (i<n-1):
        mat_futura[eq,nc] = b5
        mat_futura[eq,nl] = b7
        mat_futura[eq,nr] = b6
        
        #print("Nodos internos")
    else:
        mat_futura[eq,nc] = b5
        mat_futura[eq,nl] = -b
        
        #print("Nodo a la derecha")
    eq += 1

minv = np.linalg.inv(mat_futura)

for j in range(1,it+1):
    #print("iteracion: ",j)
    C = minv@(C + vec_F)
    mat_C[:,j] = -C*c_ref

x = np.zeros(n)
for i in range(n):
    x[i] = dx*(i)*L

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