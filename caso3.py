# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 18:11:53 2020

@author: Andres Medina
"""
import numpy as np
from scipy.optimize import minimize

def SetMoneda(num, simbolo="US$", n_decimales=2):
    """Convierte el numero en un string en formato moneda
    SetMoneda(45924.457, 'RD$', 2) --> 'RD$ 45,924.46'     
    """
    #con abs, nos aseguramos que los dec. sea un positivo.
    n_decimales = abs(n_decimales)
    
    #se redondea a los decimales idicados.
    num = round(num, n_decimales)

    #se divide el entero del decimal y obtenemos los string
    num, dec = str(num).split(".")

    #si el num tiene menos decimales que los que se quieren mostrar,
    #se completan los faltantes con ceros.
    dec += "0" * (n_decimales - len(dec))
    
    #se invierte el num, para facilitar la adicion de comas.
    num = num[::-1]
    
    #se crea una lista con las cifras de miles como elementos.
    l = [num[pos:pos+3][::-1] for pos in range(0,50,3) if (num[pos:pos+3])]
    l.reverse()
    
    #se pasa la lista a string, uniendo sus elementos con comas.
    num = str.join(",", l)
    
    #si el numero es negativo, se quita una coma sobrante.
    try:
        if num[0:2] == "-,":
            num = "-%s" % num[2:]
    except IndexError:
        pass
    
    #si no se especifican decimales, se retorna un numero entero.
    if not n_decimales:
        return "%s %s" % (simbolo, num)
        
    return "%s %s.%s" % (simbolo, num, dec)

Amax = 250
Riegomax = 1.2e6
Manomax = 3000

Riegos = [6e3,3.1e3,4.6e3]
Trabajos = [20,5,7.5]
Rendimientos = [4.5,2.5,3.7]

def Rendimiento(x):
    return -(Rendimientos[0]*x[0] + Rendimientos[1]*x[1] + Rendimientos[2]*x[2])

def conTrabajo(x):
    return Manomax - (Trabajos[0]*x[0] + Trabajos[1]*x[1] + Trabajos[2]*x[2] )

def conEspacio(x):
    return Amax - (x[0] + x[1] + x[2] )

def conRiego(x):
    return Riegomax - (Riegos[0]*x[0] + Riegos[1]*x[1] + Riegos[2]*x[2] )

def Trabajo(x):
    return (Trabajos[0]*x[0] + Trabajos[1]*x[1] + Trabajos[2]*x[2] )

def Espacio(x):
    return (x[0] + x[1] + x[2] )

def Riego(x):
    return (Riegos[0]*x[0] + Riegos[1]*x[1] + Riegos[2]*x[2] )

r1 = {'type':'ineq', 'fun': conEspacio}
r2 = {'type':'ineq', 'fun': conTrabajo}
r3 = {'type':'ineq', 'fun': conRiego}

rango = (0,Amax)
fronteras = (rango,rango,rango)
x0 = [0,0,0]

bnds = ((0, Amax), (0, Amax), (0,Amax))

res1 = [r1,r2,r3]

results1 = minimize(Rendimiento,x0,method='SLSQP',bounds=fronteras,constraints=res1)

print("Todas las restricciones")
R1 = -Rendimiento(results1.x)*1e6
riego1 = Riego(results1.x)
trabajo1 = Trabajo(results1.x)
print("Rendimineto: "+ SetMoneda(R1,"COP"))
print("Hectareas usadas: "+ str(Espacio(results1.x)))
print("Riego Mensual: "+ str(riego1))
print("Trabajo Necesario: "+ str(trabajo1))
#Crear seis variables

res2 = [r1,r2]

results2 = minimize(Rendimiento,x0,method='SLSQP',bounds=fronteras,constraints=res2)
print("----------------------------------")
print("Sin restricción de agua")
R2 = -Rendimiento(results2.x)*1e6
riego2 = Riego(results2.x)
print("Rendimineto: "+ SetMoneda(R2,"COP"))
print("Hectareas usadas: "+ str(Espacio(results2.x)))
print("Riego Mensual: "+ str(riego2))
print("Trabajo Necesario: "+ str(Trabajo(results2.x)))

ganancia = R2-R1
deltaRiego = riego2-riego1

print("Compren: "+ str(deltaRiego) +" Si les cuesta menos de: " + SetMoneda(ganancia,"COP"))

res3 = [r1]

results3 = minimize(Rendimiento,x0,method='SLSQP',bounds=fronteras,constraints=res3)

print("----------------------------------")
print("Sin restricción ni de agua ni de trabajo")
R3 = -Rendimiento(results3.x)*1e6
trabajo3 = Trabajo(results3.x)
print("Rendimineto: "+ SetMoneda(R3,"COP"))
print("Hectareas usadas: "+ str(Espacio(results3.x)))
print("Riego Mensual: "+ str(Riego(results3.x)))
print("Trabajo Necesario: "+ str(trabajo3))

ganancia = R3-R1
deltaTrabajo = trabajo3-trabajo1

print("Contrate: "+ str(deltaTrabajo) +" Si les cuesta menos de: " + SetMoneda(ganancia,"COP"))
print("-------------------------------")
print("Resultados Adversos")
resultadosAdversos = np.zeros(6)
cnt = 0
for i in range(3):
    for j in range(2):
        Rendimientos = [4.5,2.5,3.7]
        Rendimientos[i] *= 0.8
        Rendimientos[(i+j+1)%3] *= 1.3
        #resultadosAdversos.append( minimize(Rendimiento,x0,method='SLSQP',bounds=fronteras,constraints=res1) )
        resultadosAdversos[cnt]=-Rendimiento(results1.x)*1e6  
        print(Rendimientos,SetMoneda(resultadosAdversos[cnt],"COP"))
        cnt += 1
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
        