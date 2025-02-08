#Ordenación de puntajes deportivos: Ordena una lista de puntajes deportivos utilizando el método de quicksort... Burbuja

def burbuja_puntajes(puntajes):

    n = len(puntajes)

    for i in range(n):

        for j in range(0, n-i-1):

            if puntajes[j] > puntajes[j+1]:
                puntajes[j], puntajes[j+1] = puntajes[j+1], puntajes[j]

    return puntajes


puntajes_deportivos = [90, 45, 55, 39, 60]
puntajes_ordenados = burbuja_puntajes(puntajes_deportivos)

print(f"Puntajes de menor a mayor: {puntajes_ordenados}")