# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:38:08 2020

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
dt = 0.0001
tf = 10
it = int(tf/dt)
dx = 0.02
n = int(L/dx)+1
nodos = n

mat_actual = np.zeros((nodos,nodos))
C = np.zeros(nodos)
vec_F = np.zeros(nodos)

mat_C = np.zeros((nodos,it+1))

eq = 0 

for i in range(n):
    nc = eq
    nl = nc - 1
    nr = nc + 1
    if (i == 0):
        mat_actual[eq,nc] = (-2*D*dt)/dx**2 - 2*U*dt/dx - U**2*dt/D - k*dt + 1
        mat_actual[eq,nr] = (2*D*dt)/dx**2
        vec_F[eq] = (2*U*dt/dx + U**2*dt/D)*c_ref
        #print("Nodos a la izquierda")
    elif (i<n-1):
        mat_actual[eq,nc]= (-2*D*dt)/dx**2 - k*dt + 1
        mat_actual[eq,nl]= D*dt/(dx**2) + U*dt/(2*dx)
        mat_actual[eq,nr]= D*dt/(dx**2) - U*dt/(2*dx)
        #print("Nodos internos")
    else:
        mat_actual[eq,nc] = (-2*D*dt)/dx**2-k*dt + 1
        mat_actual[eq,nl] = (2*D*dt)/dx**2
        #print("Nodo a la derecha")
    eq += 1

for j in range(1,it+1):
    #print("iteracion: ",j)
    C = (mat_actual@C) + vec_F
    mat_C[:,j] = C

x = np.zeros(n)
for i in range(n):
    x[i] = dx*(i)

plt.plot(x,mat_C[:,-1],"-k",label="t=10 s")    

plt.legend(loc="upper right")
plt.xlabel('Distancia (m)')
plt.ylabel('Concentración (C)')
plt.grid()
plt.show()       
"""
fig = plt.figure()
plt.style.use('classic')
ims = []

def imagen(c):
    im = np.ones((2,2*len(c)))
    w = 3
    for i in range(len(c)):
        im[:,w*i:w*i+w] *= c[i]
    return im
    
imagenes = []
for i in range(0,it,100):
    im = plt.imshow(imagen(mat_C[:,i]), animated=True)
    ims.append([im])

ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=100)

writergif = animation.PillowWriter(fps=30)
#ani.save('dynamic_images.gif',writer=writergif)
plt.colorbar()
plt.show()
"""
