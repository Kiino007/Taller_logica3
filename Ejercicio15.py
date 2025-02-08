#Ordenación de productos por fecha de caducidad: Dado un conjunto de productos con fechas de caducidad, ordénalos utilizando el método de heapsort.

def burbuja_productos(productos):

    n = len(productos)

    for i in range(n):
        for j in range(0, n-i-1):
            if productos[j][1] > productos[j+1][1]:
                productos[j], productos[j+1] = productos[j+1], productos[j]

    return productos


productos = [
    ("Chocolatina", "2025-04-18"),
    ("Arroz", "2025-07-20"),
    ("Cocacola", "2025-02-15"),
    ("Quesito", "2025-02-10"),
    ("Boliquesos", "2025-10-05")
]

print("Productos sin ordenar:", productos)

productos_ordenados = burbuja_productos(productos)
print(f"Productos ordenados por fecha de caducidad: {productos_ordenados}")