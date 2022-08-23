""" 6.	Escriba un programa que almacene la cadena de contraseña en una variable, solicite la contraseña al usuario e imprima en la pantalla si la contraseña ingresada por el usuario coincide con la contraseña almacenada en la variable, independientemente de las letras mayúsculas y minúsculas.
 """

password = "hamburguesa"

ingreso = input (" Ingrese la contraseña ")

if password == ingreso.lower():
    print ("Coincide")
else:
    print("No hay coincidencia")

    
