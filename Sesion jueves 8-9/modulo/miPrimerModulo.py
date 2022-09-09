def mensaje(nombre):
    return f"Hola {nombre} estamos en COLTIS"

def calculadora(num1,num2,basico=False):
    suma = num1 + num2
    resta = num1 - num2
    multiplicar = num1 * num2
    division = num1 / num2
    
    cadena = ""
    
    if basico!=False:
        cadena+= f"suma {suma}"
        cadena+= f"\n"
        cadena+= f"resta {resta}"
        cadena+= f"\n"
        
    else:
        cadena+= f"multiplicar {multiplicar}"
        cadena+= f"\n"
        cadena+= f"division {division}"
        cadena+= f"\n"
    
    return cadena