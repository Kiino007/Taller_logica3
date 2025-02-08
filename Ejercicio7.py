#Ranking de puntuaciones: Un juego guarda las puntuaciones de jugadores. Ordena las puntuaciones en orden descendente usando inserción.

def insercion_descendente(puntuaciones):

    for i in range(1, len(puntuaciones)):
        clave = puntuaciones[i]
        j = i - 1

        while j >= 0 and puntuaciones[j] < clave:
            puntuaciones[j + 1] = puntuaciones[j]
            j -= 1

        puntuaciones[j + 1] = clave

    return puntuaciones


puntuaciones = [110, 400, 870, 9000, 2510]
puntuaciones_ordenadas = insercion_descendente(puntuaciones)

print(f"Puntuaciones ordenadas en orden descendente: {puntuaciones_ordenadas}")