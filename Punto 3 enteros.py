# -*- coding: utf-8 -*-
"""
Created on Sun Dec 13 20:48:27 2020

@author: Sebastian
"""

from pulp import LpMaximize, LpProblem, lpSum, LpVariable

model = LpProblem(name="Optimización_enteros", sense=LpMaximize)
# Variables de interés, 

L40z = LpVariable(name="L40z", lowBound=0, cat="Integer")
L40m = LpVariable(name="L40m", lowBound=0, cat="Integer")
L40p = LpVariable(name="L40p", lowBound=0, cat="Integer")

L25z = LpVariable(name="L25z", lowBound=0, cat="Integer")
L25m = LpVariable(name="L25m", lowBound=0, cat="Integer")
L25p = LpVariable(name="L25p", lowBound=0, cat="Integer")                  

model += (L40z + L40m + L40p <= 5, "Lotes_de_40")
model += (L25z + L25m + L25p <= 2, "Lotes_de_25")
model += (40*(6000*L40z+3100*L40m+4600*L40p)+25*(6000*L25z+3100*L25m+4600*L25p) <=1200000,"Riego_max")
model += (40*(20*L40z+5*L40m+7.5*L40p)+25*(20*L25z+5*L25m+7.5*L25p),"Horas_semanales")

model += lpSum([40*4.5*L40z,40*2.5*L40m,40*3.7*L40p,25*4.5*L25z,25*2.5*L25m,25*3.7*L25p])

status = model.solve()

for var in model.variables():
     print(f"{var.name}: {var.value()}")

print(f"Ganancia: {model.objective.value()}")