""" Escribir un programa para la empresa “MySpa” que tiene salas de relajación 
y limpieza fácil para todas las edades; MySpa quiere calcular de forma 
automática el precio que debe cobrar a sus clientes por disfrutar de sus 
servicios. El programa debe preguntar al usuario la edad del cliente y mostrar 
el precio de la entrada; si el cliente es menor de 4 años puede entrar gratis, 
si tiene entre 4 y 18 años debe pagar 5 pesos y si es mayor de 18 años, 10
pesos """

edad = int(input("Cual es su edad\n"))

if edad<4:
    precio = 0
elif 4<=edad<=18:
    precio = 5
elif edad>18:
    precio = 10
print (f"El precio a pagar es de {precio}")

