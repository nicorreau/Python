letra = input("Ingrese una letra: ").lower()

if len(letra)>1:
    print("No se puede procesar ")

if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
    print("Es una vocal ")
else:
    print ("No es una vocal ")
    
    
