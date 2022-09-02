""" estudiantes = ['juan','johan','emilia']

#recorrer
print(f'recorrer toda la coleccion : \n{estudiantes}')
#sacar uno a uno con for
print('--- con for---')
for estudiante in estudiantes:
    print(estudiante)

print('--- agregar al ultimo en la cola---')
estudiantes.append('Mijail')
print(estudiantes)



print('--- agregar en la cola en una posicion ---')
estudiantes.insert(2,'Andres')
print(estudiantes)

print('--- agregar en la cola en una posicion ---')
estudiantes.remove("juan")
print(estudiantes)

print('\n --- eliminar al ultimo en la cola---')
estudiantes.pop()
print(estudiantes)

estudiantes.clear()
print(estudiantes)

del estudiantes

print(estudiantes) #si se imprime da error porque ya no existe

bandas = ('acdc','pantera','nirvana')
print(bandas)
print(len(bandas))
print(bandas[1])
print(bandas[-1])
print(bandas[1:])
for banda in bandas:
    print(banda)

bandas[2] = 'DevilDriver'
print(bandas)

bandasLista = list(bandas)#convertimos a lista 
bandasLista[2] = 'DevilDriver'#vaya a la posicion 2 y lo cambia por Devil
print(bandasLista)
bandas = tuple(bandasLista)#ahora convertir la lista a tuplas de nuevo
del bandas#eliminamos la tupla
print(bandas)#imprimimos """

# set
""" cursos = {"Java","Python","C#"}
print(cursos)
print(len(cursos))
print("Java" in cursos)
cursos.add("MERN")
print(cursos) """

diccionarios = {
    
    "COLTIS": "Colombian TI software",
    "IDE": "Entorno de desarrollo integrado"
}

for item,valor in diccionarios.items():
    print(f"clave: {item},  valor:{valor} ")