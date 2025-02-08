#Ordenación de distancia entre ciudades: Dado un arreglo con distancias entre ciudades, ordénalas de menor a mayor usando inserción.

def insercion_distancias(distancias):

    for i in range(1, len(distancias)):
        clave = distancias[i]
        j = i - 1

        while j >= 0 and distancias[j] > clave:
            distancias[j + 1] = distancias[j]
            j -= 1

        distancias[j + 1] = clave

    return distancias


distancias_ciudades = [900, 500, 2500, 1000, 1150]
distancias_ordenadas = insercion_distancias(distancias_ciudades)

print("Distancias de menor a mayor: {distancias_ordenadas}")