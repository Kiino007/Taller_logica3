#Temperaturas diarias: Un sensor registra las temperaturas de una semana. Ordena los valores de mayor a menor utilizando burbuja.

def burbuja_descendente(temperaturas):

    longitud_grados = len(temperaturas)

    for i in range(longitud_grados):
        for j in range(0, longitud_grados-i-1):
            if temperaturas[j] < temperaturas[j+1]:
                temperaturas[j], temperaturas[j+1] = temperaturas[j+1], temperaturas[j]

    return temperaturas


temperaturas = [2, 15, 25, 7, 27, 12]
temperaturas_ordenadas = burbuja_descendente(temperaturas)

print(f"Temperaturas ordenadas de mayor a menor: {temperaturas_ordenadas}")