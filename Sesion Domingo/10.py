""" 10.	Los alumnos de un curso se dividen en dos grupos A y B según sexo y nombre. El grupo A está formado por mujeres que llevan el nombre de M y hombres que llevan el nombre de N, y el grupo B es el resto. Escriba un programa que le pregunte al usuario su nombre y género y muestre el grupo correspondiente en la pantalla.
 """
nombre = input("Nombre:")
genero = input("Genero:")

if (genero.upper() == 'M' and 'n' in nombre.lower()) or (genero.upper() == 'F' and 'm' in nombre.lower()):
    print("Grupo A" )
else:
   print("Grupo B" )