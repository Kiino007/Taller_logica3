# Ordenación de caracteres en una palabra: Dada una palabra, ordénala alfabéticamente utilizando el método de inserción.

def insercion_alfabetica(palabra):

    caracteres = list(palabra)
    
    for i in range(1, len(caracteres)):
        clave = caracteres[i]
        j = i - 1

        while j >= 0 and caracteres[j] > clave:
            caracteres[j + 1] = caracteres[j]
            j -= 1

        caracteres[j + 1] = clave
    
    return ''.join(caracteres)


palabra = "valorant"
palabra_ordenada = insercion_alfabetica(palabra)

print(f"Palabra ordenada alfabeticamente: {palabra_ordenada}")