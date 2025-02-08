#Orden de llegada de corredores: Dado un listado de tiempos de llegada en una carrera, ordénalos de menor a mayor usando burbuja.

def burbuja(tiempos):

    cantidad = len(tiempos)

    for i in range(cantidad):
        for j in range(0, cantidad-i-1):
            if tiempos[j] > tiempos[j+1]:
                tiempos[j], tiempos[j+1] = tiempos[j+1], tiempos[j]

    return tiempos


tiempos_de_llegada = [15.15, 10.1, 11.9, 17.5, 9.3]
tiempos_ordenados = burbuja(tiempos_de_llegada)

print(f"El orden ascendente de los tiempos es: {tiempos_ordenados}") 