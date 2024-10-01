'''
Las listas son colecciones de elementos en un orden particular. Podemos tener lñostas de un solo tipo de datos
pero esto no tiene porqte ser asi, es mas podemos tener listas que contengan listas, esta debe se incluida entre []
y es realidad es un array, sus elementos seran separados por coma.
'''

bicycles = ['trek','cannondale','redline', 'specialized', 'moongoosse','royal', 'benoto']
print(bicycles)

''' 
    Como las listas son colecciones ordenadas de elementos podemos acceder a ellos por su indice,
    siempre empezando por cero (0) como todo array.
'''
elemento_1 = bicycles[0]
print(elemento_1)

## Modificando, Añadiendo y Eliminando Elementos de una Lista
''' para modificar accedemos a el indixe del elemento'''
bicycles[4]= 'mongoose'
bicycles[6]= 'benotto'
print(bicycles)

# add elementos al final de la lista 
bicycles.append('ducati')
print(bicycles)

# insertar elementos en una lista
''' con el metodo insert() añadimos elementos a una lista en la poscición requerida usando el indice de esta como argumento'''
bicycles.insert(3,'decatlon')
print(bicycles)

# Eliminar elementos en una lista
''' si se conoce el indice del elemento a eliminar podemos usar "del" '''
del bicycles[8]
print(bicycles)
