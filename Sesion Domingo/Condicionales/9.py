""" 9.	Para pagar un determinado impuesto es necesario ser mayor de 16 años y tener unos ingresos iguales o superiores a 1.000 mensuales. Escriba un programa que le pregunte al usuario su edad e ingresos mensuales y muestre en la pantalla si el usuario tiene que pagar impuestos. """

edad = int(input("Ingrese su edad: "))
ingresos = float(input("Cuales son los ingresos: "))

if edad >= 16 and ingresos>=1000:
    print("Paga impuesto")
else:
    print("No paga impuesto")
