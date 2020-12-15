# -*- coding: utf-8 -*-
"""
Created on Sat Dec  5 08:38:08 2020

@author: Andres Medina
"""
import numpy as np
import matplotlib.pyplot as plt

D = 1.8 #m**2/s
L = 0.9 #m
U = 0.2 #m/s
c_ref = 0.1 #kg/m**3
k = 5 #k**-1
tao = L/U
dt = 0.0001/tao
tf = 10/tao
it = int(tf/dt)
dx = 0.02/L
n = int(1/dx)+1
nodos = n

mat_actual = np.zeros((nodos,nodos))
C = np.zeros(nodos)
vec_F = np.zeros(nodos)

mat_C = np.zeros((nodos,it+1))

a0 = D/(L*U)
a1 = k*L/U
a2 = U*L/D

b = 2*a0*dt/dx**2
b1 = -b - a1*dt + 1
b2 = b/2 - dt/(2*dx)
b3 = b/2 + dt/(2*dx)
b4 = 2*a2*a0*dt/dx + a2*dt

eq = 0 

for i in range(n):
    nc = eq
    nl = nc - 1
    nr = nc + 1
    if (i == 0):
        mat_actual[eq,nc] = b1-b4
        mat_actual[eq,nr] = b #b2+b3
        vec_F[eq] = b4
        #print("Nodos a la izquierda")
    elif (i<n-1):
        mat_actual[eq,nc]= b1
        mat_actual[eq,nr]= b2
        mat_actual[eq,nl]= b3
        #print("Nodos internos")
    else:
        mat_actual[eq,nc] = b1
        mat_actual[eq,nl] = b
        #print("Nodo a la derecha")
    eq += 1

for j in range(1,it+1):
    #print("iteracion: ",j)
    C = (mat_actual@C) + vec_F
    mat_C[:,j] = C*c_ref

x = np.zeros(n)
for i in range(n):
    x[i] = dx*(i)*L

plt.plot(x,mat_C[:,int(0.01*it)],label="t=0.1 s")  
plt.plot(x,mat_C[:,int(0.02*it)],label="t=0.2 s")  
plt.plot(x,mat_C[:,int(0.05*it)],label="t=0.5 s")   
plt.plot(x,mat_C[:,int(0.08*it)],label="t=0.8 s")  
plt.plot(x,mat_C[:,int(0.1*it)],label="t=1 s") 
plt.plot(x,mat_C[:,int(it)],label="t=10 s Explicito")    
plt.legend(loc="upper right")
plt.xlabel('Distancia (m)')
plt.ylabel('Concentración (kg/m**3)')
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
