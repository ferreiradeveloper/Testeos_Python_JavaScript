message='Hello Python World'
print(message)

message='Hello Python Chash course World'
print(message)

name = 'franciSco ferreIra'
print(name.title())
print(name.upper())
print(name.lower())

# las cadenas f estan en Python a partir de la versión 3.6, sustituyendo a format
# pero su uso es un poco complicado var_name = "{} {}".format(first_name, last_name)
first_name= 'edward'
last_name = 'ferreira'
full_name = f"Hello, {first_name} {last_name}"
print(full_name.title())

# add espacios en blanco \t (tab)
print("Python")
print("\tPython")

#add new lines \n
print("Lenguajes:\nPython\nC#\nJavaScript")
print("Lenguajes:\n\tPython\n\tC#\n\tJavaScript") #muchos combinando ambas

## Eliminar espacios en blanco
favority_languaje = 'Python  '
print(favority_languaje.rstrip()) # elimina los espacios a la derecha
favority_languaje = '  Python'
print(favority_languaje.lstrip()) # elimina los espacios a la derecha

# Para hacer uso del '(apostrofe), debemos encrerrar en comillas dobles la cadena
message = "One of the Python's strengths is its devierse community."
print(message)

## Usando números y operando con ellos
a = 2 + 3
print('Suma: ', a)
b = 3 - 1
print('Resta: ', b)
c = 3 * 4
print('producto: ', c)
d = 3 ** 4
print('Potencia: ', d)

# gerarquia de operadores
a = 2 + 3 * 4
print(a)
b = (2 + 3) * 4
print(b)

# Números enteros y flotantes
a = 23
b = 2.3
c = 1/4

print(a,b,c)

# Aportando legibilidad a los números con _
a = 14_000_000_000
print(a)

# Asignación multiple
x, y, z = 0, 1, 2 # se debe respetar el orden de asignacion
print(x, y, z)

# Constantes en python son solo indicativas
IP = '198.169.1.1'
print(IP)

