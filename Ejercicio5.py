#Ordenación de precios de productos: Un sistema de inventario tiene precios desordenados. Ordénalos ascendentemente con burbuja.

def burbuja(precios):

    cantidad = len(precios)

    for i in range(cantidad):
        for j in range(0, cantidad-i-1):
            if precios[j] > precios[j+1]:
                precios[j], precios[j+1] = precios[j+1], precios[j]

    return precios


precios = [1400, 10000, 3400, 450, 8650]
precios_ordenados = burbuja(precios)

print(f"Orden de precios ascendentemente: {precios_ordenados}")