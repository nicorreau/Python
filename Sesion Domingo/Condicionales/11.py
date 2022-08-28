""" Escriba un programa para la empresa de entretenimiento “Divertilife” que 
tiene un parque infantil inflable para todas las edades y desea calcular 
automáticamente el precio que cobrará a los clientes por ingresar. El 
programa preguntará al usuario sobre la edad del cliente y mostrará la tarifa. 
Si los clientes menores de 2 años pueden entrar gratis, si tienen de 3 a 18 
años, tienen que pagar 5 pesos, y si son mayores de 18 años son 10. """

edad = int(input("Cual es su edad: "))
if 0<edad<2:
    tarifa = 0
elif 3<edad<=18:
    tarifa = 5
elif edad>18:
    tarifa = 10

print (f"La tarifa a pagar es {tarifa}")