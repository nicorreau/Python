""" 7.	Escriba un programa que le pida al usuario que ingrese dos números y muestre su división en la pantalla. Si el divisor es 0, el programa mostrará un error. """

num1 = float(input("Digite un numero "))
num2 = float(input("Digite un numero "))

if num2 == 0:
    print ("Error")
else:
    division = num1/num2
    print ("La divison " + str(division))