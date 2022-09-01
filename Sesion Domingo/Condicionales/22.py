año = int(input("\nIngrese un año "))

if (año % 4 == 0 and not (año % 100 ==0)) or (año % 400 == 0 and año % 100 == 0) :
    bisiesto =True
    if bisiesto == True:
        print ("El año es bisiesto ")
else: print ("El año no es bisiesto ")

