#Ordenación de ventas diarias: Se registraron ventas diarias de una tienda. Ordénalas en orden ascendente con inserción.

def insercion_ventas(ventas):

    for i in range(1, len(ventas)):
        clave = ventas[i]
        j = i - 1

        while j >= 0 and ventas[j] > clave:
            ventas[j + 1] = ventas[j]
            j -= 1

        ventas[j + 1] = clave

    return ventas


ventas_diarias = [30, 200, 70, 150, 50, 80]
ventas_ordenadas = insercion_ventas(ventas_diarias)

print(f"Ventas en orden ascendente: {ventas_ordenadas}")