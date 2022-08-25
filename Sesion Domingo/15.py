""" Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es 
menor. No considerar el caso en que ambos números son iguales. """

a = int(input("Ingrese un numero "))
b = int(input("Ingrese un numero "))

if a<b:
    print(f"{a} es el menor")
elif b<a:
    print(f"{b} es el menor")
else:
    print("No existe esa opcion ")
