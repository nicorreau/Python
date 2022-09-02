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
    
for llave, valor in diccionarios.items():
    print(llave, valor)

for llave in diccionarios.keys():
    print(llave)

for valor in diccionarios.values():
    print(valor)

diccionario = {
    
        1:          'valores conbinados',
        'COLTIS':   'Colombian TI Software',
        'IDE':      'Entorno de Desarrollo Integrado',
        'OOP':      'Objec Oriented Programming'
}

print(diccionario)
print(len(diccionario))
print(diccionario['IDE'])
print(diccionario.get('OOP'))
#cambiar un valor por otro
diccionario['COLTIS'] = 'colombian ti sas'
print(diccionario)

diccionario[1] = 'cambie valor conbinado con la key numerica'
print(diccionario)

for key, value in diccionario.items():
    print(key,value)

for key in diccionario.keys():
    print(key)

for value in diccionario.values():
    print(value)

diccionario.pop('OOP')
print(diccionario)
diccionario.clear()
print(diccionario)
diccionario['IDE']='Netbeans'
print(diccionario)

