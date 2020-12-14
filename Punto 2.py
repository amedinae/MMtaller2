# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 09:25:54 2020

@author: Sebastian
"""

import numpy as np
import matplotlib.pyplot as plt

L=5 #m
c=1 #m/s
Gamma= 1 #1/s
dx= 0.125 #m
dt= 1e-4 #s
F=2*dx/(c*dt)
tf=30
nodos=int(L/dx) + 1
it = int(tf/dt)

U = np.zeros((nodos,it+1))
V = np.zeros((nodos,it+1))

# Condiciones iniciales
for j in range(nodos):
    U[j,0]=np.exp(np.cos(2*np.pi*(j*dx)/L))
    
for k in range(1,it+1):
    for i in range(nodos):
        if (i==0):
            U[i,k] = -U[i+1,k-1]/F + U[i,k-1] +U[nodos-2,k-1]/F 
        elif (i==nodos-1):
            U[i,k] = -U[1,k-1]/F + U[i,k-1] +U[i-1,k-1]/F 
        else:
            U[i,k] = -U[i+1,k-1]/F + U[i,k-1] +U[i-1,k-1]/F 
        V[i,k] = Gamma*dt*U[i,k-1]+(1-Gamma*dt)*V[i,k-1]    
        
x = np.zeros(nodos)
for h in range(nodos):
    x[h] = dx*h
    
#plt.plot(x,U[:,0],"-k",label="U(x,0)") 
#plt.plot(x,V[:,0],"-r",label="V(x,0)")  
   
plt.plot(x,U[:,it],"-g",label="U(x,30)")    
plt.plot(x,V[:,it],"-b",label="V(x,30)")      


plt.legend(loc="upper center|")
plt.xlabel('Distancia (m)')
plt.ylabel('U,V')
plt.grid()