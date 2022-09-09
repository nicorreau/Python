""" import miPrimerModulo

print(miPrimerModulo.mensaje("NESTOR"))


print(miPrimerModulo.calculadora(2,2,True))
print(miPrimerModulo.calculadora(2,2,False)) """

# Modulo de fechas

""" import datetime
print(datetime.date.today())
fechaCompleta= datetime.datetime.now()
print(fechaCompleta)
print(fechaCompleta.year)
print(fechaCompleta.month)
print(fechaCompleta.day)

fechaPersonalizada = fechaCompleta.strftime("%Y/%m/%d")
print(fechaPersonalizada) """

import math

print (f"la Raiz cuadrada de un numero es {math.sqrt(2):.2f}")

import random

print(f"Numero aleatorio entre 20 y 40: {random.randint(20,40)}")