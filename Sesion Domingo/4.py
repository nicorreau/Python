""" 4.	Sistema de calificación:
El objetivo del ejercicio es crear un sistema de calificaciones, como sigue:
El usuario Digite una clasificación entre 0 y 10.
•	Si esta entre 8 y 10: imprimir una Excelente
•	Si esta entre 7 y menor a 8: imprimir una Muy bien 
•	Si esta entre 6 y menor a 7: imprimir una Bien
•	Si esta entre 0 y menor a 6: imprimir una Reprobado
•	cualquier otro valor debe imprimir: Valor incorrecto
Por ejemplo:
•	Proporciona un valor entre 0 y 10: 7
•	Bien """

calificacion = float(input("Ingrese una calificacion"))

if 8<calificacion<10:
    print("Excelente")
elif 7<calificacion<8:
    print("Bien")
elif 0<calificacion<6:
    print("Reprobado")
else:
    print("Valor incorrecto")