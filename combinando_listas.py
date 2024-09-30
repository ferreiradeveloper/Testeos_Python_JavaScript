import timeit


# Código tradicional
def combinacion_tradicional():
    nombres = ["Frank","Edward","Junior"] * 100000
    edades = [55,29,22] * 100000
    combinados = []
    for i in range(len(nombres)):
        combinados.append((nombres[i], edades[i]))
    return combinados

# Forma rapida y simple con zip
def combinacion_zip():
    nombres = ["Frank","Edward","Junior"] * 100000
    edades = [55,29,22] * 100000
    combinados = list(zip(nombres, edades))
    return combinados

# Medicion de tiempo
tradicional_time = timeit.timeit(combinacion_tradicional, number= 100)
zip_time = timeit.timeit(combinacion_zip, number= 100)

print(f"Tiempo tradicional: {tradicional_time:5f} segundos")
print(f"Tiempo con zip: {zip_time:5f} segundos")