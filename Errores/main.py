""" try:
    edad = int(input('¿Hola q tal me puedes decir tu edad '))
    print(edad)
except: 
    print("Valor no valido, por favor ingrese un entero")
else:
    print("Todo funciona normal")
finally:
    print("!Se acabo!") """
    
    

#Manejo de errores multiples

try:
    numero = int(input("Ingrese un numero para elevar al cubo: "))
    print("El numreo elevado al cubo es "+ str(numero**3))
except TypeError:
    print("Debes convertir tu cadena en un valor entero ")
#except ValueError:
    #print("Ingrese  un valor numerico entero ")
except Exception as e:
    print("Ha ocurrido un error: ", type(e).__name__)