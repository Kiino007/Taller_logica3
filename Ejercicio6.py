#Ordenación de edades: Un grupo de personas tiene diferentes edades. Utiliza inserción para ordenarlas de menor a mayor.

def insercion(edades):

    for i in range(1, len(edades)):
        clave = edades[i]
        j = i - 1

        while j >= 0 and edades[j] > clave:
            edades[j + 1] = edades[j]
            j -= 1

        edades[j + 1] = clave

    return edades


edades = [32, 29, 18, 19, 24]
edades_ordenadas = insercion(edades)

print(f"Edades de menor a mayor: {edades_ordenadas}")