#Ordenación de nombres por orden alfabético inverso: Usa el método de shell sort para ordenar una lista de nombres en orden descendente... Burbuja

def burbuja_descendente(lista):

    n = len(lista)

    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] < lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    return lista


nombres = ["JayceJ", "Fiora", "Heimerdinger", "Vi", "Morgana", "Lucian", "Darius", "Anivia"]
print("Lista de nombres antes de ordenar:", nombres)

nombres_ordenados = burbuja_descendente(nombres)
print(f"Nombres ordenados en orden alfabetico inverso: {nombres_ordenados}")