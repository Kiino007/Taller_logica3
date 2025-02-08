#Ordenación de notas de estudiantes: Dado un arreglo de calificaciones, ordénalas de menor a mayor usando el método de burbuja.

def burbuja(calificaciones):

    numeros = len(calificaciones)

    for i in range(numeros):
        for j in range(0, numeros-i-1):
            if calificaciones[j] > calificaciones[j+1]:
                calificaciones[j], calificaciones[j+1] = calificaciones[j+1], calificaciones[j]

    return calificaciones


calificaciones = [90, 50, 80, 65, 95, 40]
calificaciones_ordenadas = burbuja(calificaciones)

print(f"Calificaciones por orden ascendente: {calificaciones_ordenadas}")