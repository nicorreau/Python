""" Requerir al usuario que ingrese un día de la semana e imprimir un mensaje 
si es lunes, otro mensaje diferente si es viernes, otro mensaje diferente si es 
sábado o domingo. Si el día ingresado no es ninguno de esos, imprimir otro 
mensaje. """

dia =input("Ingrese un dia de la semana ").lower()

if dia == "lunes":
    mensaje = "Hoy es lunes"
elif dia == "Viernes":
    mensaje = "Hoy es viernes"
elif dia == "domingo" or dia == "sabado":
    mensaje = "Hoy es fin de semana "
elif not (dia == "lunes" and dia == "viernes" and dia == "domingo" and dia == "sabado"):
    mensaje= ("Este no es un dia muy normal, lo mejor seria no pensar...")

    
    
print(mensaje)