 #Lista de números aleatorios: Genera una lista de 20 números aleatorios y ordénalos con el algoritmo de mergesort... Burbuja

import random

def burbuja(lista):

    n = len(lista)

    for i in range(n):

        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


numeros_aleatorios = [random.randint(1, 100) for _ in range(20)]
print("Numeros aleatorios sin orden:", numeros_aleatorios)

numeros_ordenados = burbuja(numeros_aleatorios)
print(f"Numeros ordenados: {numeros_ordenados}")