nombre1 = input("\n\nnombre1\n")
nombre2 = input("\nnombre2\n")

if nombre1[0] == nombre2[0] or nombre1[len(nombre1) - 1] == nombre2[len(nombre2) - 1]:
    print("Coincidencia")
else:
    print("No hay coincidencia")
    
    
    