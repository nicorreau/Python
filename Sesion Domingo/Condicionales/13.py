""" Comidas Rápidas Antoine ofrece hamburguesas vegetarianas y no 
vegetarianas a sus clientes. Los ingredientes para cada tipo de hamburguesa
se muestran a continuación.
• Ingredientes vegetarianos: Tomate y tarta de lentejas.
• Ingredientes no vegetarianos: Carne, Jamón y Queso.
Escribe un programa que pregunte a los usuarios si quieren hamburguesa
vegetariana y, en base a sus respuestas, les muestre un menú con los 
ingredientes disponibles para elegir. Solo puede elegir un ingrediente que 
no sea la pan y lechuga que se encuentran en todas las hamburguesas. 
Finalmente, deberás indicar en pantalla si la hamburguesa seleccionada es 
vegetariana o no y todos los ingredientes que contiene """



print ("******Comidas rapidas antoine*******\n")
hamburguesa = input("Que tipo de hamburguesa quiere, vegetariana o no vegetariana ? \n")

if hamburguesa.lower() == "vegetariana".lower():
    ingredientes = input("Escoja un ingrediente: Tomate y tarta \n").lower()
elif hamburguesa.lower() == "No vegetariana".lower():
    ingredientes = input("Escoja un ingrediente: carne, jamon y queso \n").lower()
print (f"La hamburguesa que escogio es {hamburguesa} y tiene {ingredientes} de ingredientes " )