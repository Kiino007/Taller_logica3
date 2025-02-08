#Ordenación de nombres por longitud: Ordena una lista de nombres según la cantidad de caracteres utilizando ordenamiento burbuja.

def burbuja_por_longitud(nombres):

    longitud = len(nombres)

    for i in range(longitud):
        for j in range(0, longitud-i-1):
            if len(nombres[j]) > len(nombres[j+1]):
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]

    return nombres


nombres = ["Garen", "Lux", "Kayn", "Rakan", "Kevin"]
nombres_ordenados = burbuja_por_longitud(nombres)

print(f"El orden de los nombres por longitud es:, {nombres_ordenados}")