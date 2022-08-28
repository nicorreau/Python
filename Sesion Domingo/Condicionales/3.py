""" 3.	Etapas de la vida:
El usuario debe hacer un programa donde digite un rango de edad y le muestre:
a.	un valor de 0-10: "La infancia es fantástica"
b.	un valor de 10-20: "Muchos cambios y mucho estudio"
c.	un valor dd 20-30: "Amor y vida adulta" 
d. un varlos de 30 - arraiba "Sigue vivo-...?"""

edad = int(input("Digite su edad\n"))

if 0<edad<=10:
    print("La infancia es fantástica")
elif 10<edad<=20:
    print("Muchos cambios y mucho estudio")
elif 20<edad<=30:
    print("Amor y vida adulta")
elif edad>30:
    print("Sigue vivo ?")
else:
    print("digite una opcion valida")