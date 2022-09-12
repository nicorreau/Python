import random
import string
from paquetes import diagramas
from paquetes import bd_palabras

def juegoAhorcado(palabra):
    print("============================")
    print("!Bienvenido al juego del Ahorcado¡")
    print("============================")


    letrasPorAdivinar = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letrasAdivinadas = set()
    
    intentos = 7
    
    while len(letrasPorAdivinar) > 0 and intentos>0:
        print(f"Te quedan {intentos} intentos y has usado estas letras: {''.join(letrasAdivinadas)}")
        
        palabraLista = [letra if letra in letrasAdivinadas else '-' for letra in palabra]
        
        print (diagramas.vidas[intentos])
        
        print (f"Palabra: {' '.join(palabraLista)}")
        
        letraUsuario = input("Digite una letra para la palabra ").upper()
        
        if letraUsuario in abecedario - letrasAdivinadas:
            letrasAdivinadas.add(letraUsuario)
            
            if letraUsuario in letrasPorAdivinar:
                letrasPorAdivinar.remove(letraUsuario)
                print("")
            else:
                intentos -= 1
                print (f"\n Tu letra, {letraUsuario} no se encuentra en la palabra ")
        elif letraUsuario in letrasAdivinadas:
            print("\n Ya escogiste esa letra. Por favor escoge una letra nueva ")
        else:
            print("\n Esta letra no es valida ")
    if intentos == 0:
        print(diagramas.vidas[intentos])
        print (f"!AHORCADO! perdiste. Lo lamento mucho. La palabra era {palabra} ")
    else:
        print(f"!EXCELENTE! ¡Adivinaste la palabra {palabra}! ")

palabra = random.choice(bd_palabras.bdPalabras).upper()

juegoAhorcado(palabra)