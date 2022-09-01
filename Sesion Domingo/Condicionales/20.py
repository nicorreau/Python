

while True:
    voto = input("\nPor quien va a votar, A,B,C \n").upper()
    if voto == "A":
        print ("Su voto es por el partido rojo")
        break
    elif voto == "B" or voto == "C":    
        print ("Su voto es por el partido verde ")
        break
    else:
        print ("Su opcion es invalida")
        
        