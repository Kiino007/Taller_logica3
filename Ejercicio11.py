#Ordenación de salarios: Dado un conjunto de salarios de empleados, ordénalos utilizando el método de selección... burbuja

def burbuja_salarios(salarios):

    n = len(salarios)
    
    for i in range(n):

        for j in range(0, n-i-1):

            if salarios[j] > salarios[j+1]:
                salarios[j], salarios[j+1] = salarios[j+1], salarios[j]

    return salarios


salarios_empleados = [850, 2800, 900, 1500, 1350]
salarios_ordenados = burbuja_salarios(salarios_empleados)

print(f"Salarios de menor a mayor: {salarios_ordenados}")