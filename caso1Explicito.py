# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:38:08 2020

@author: Andres Medina
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from skimage.io import imsave

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
"""
fig = plt.figure()
plt.style.use('classic')
ims = []

def imagen(c):
    w = 10
    im = np.ones((w,w*len(c)))
    for i in range(len(c)):
        im[:,w*i:w*i+w] *= c[i]
    return im #(im * 255 / np.max(im)).astype('uint8')
 
for i in range(1,it):
    im = plt.imshow(imagen(mat_C[:,i]), animated=True)
    #imsave('imagenes/test'+str(i)+'.png', imagen(mat_C[:,i]))


ani = animation.ArtistAnimation(fig, ims, interval=10, blit=True,
                                repeat_delay=100)

writergif = animation.PillowWriter(fps=1)
#ani.save('dynamic_images.gif',writer=writergif)
plt.colorbar()
plt.show()
"""
