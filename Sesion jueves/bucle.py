import math

#bucle while
x = 0
while x<=10:
    print(x, end=' ')
    x+=1
    
print ("\n")

numero = int(input("digite un numero positivo: "))
while numero < 0:
    print("error, no admite negativos\n")
    numero = int(input("digite un numero positivo "))
print(f"\n Su raiz cuadrara es: {(math.sqrt(numero)): .2f}")    

respuesta = int(input("Cuantas lunas tiene jupiter: "))
while respuesta != 79:
    respuesta = int(input("Respuesta incorrecta, responda nuevamente: "))

print (f"Adivinaste: son {respuesta} lunas")

# bucle for
coleccion = [1,2,3,4,5,"johan"]
for i in coleccion:
    print(f"la literal de informacion de cada elemento es {i}")
    
#bucle for
coleccion = "Colombian TI Software"
for i in coleccion:
    print(f"{i}", end="")
    
for i in range (0,11): # imprime posiciones ( por eso se aumenta 1)
    print(i, end=" ")

for i in ("johan"):
    print(i, end=" ")