import csv
import time
inicio = time.time()

# Abrir el archivo CSV y leer los datos
with open('f_1_0.csv', 'r') as f:
    reader = csv.reader(f)
    data = list(reader)

# Convertir las cadenas de texto a números
for i in range(len(data)):
    data[i][0] = int(data[i][0])
    data[i][1] = int(data[i][1])
    data[i][2] = int(data[i][2])
    data[i][3] = int(data[i][3])
    data[i][4] = int(data[i][4])
    data[i][5] = int(data[i][5])
    data[i][6] = float(data[i][6])
    data[i][7] = int(data[i][7])
    data[i][8] = int(data[i][8])
    data[i][9] = int(data[i][9])

# Variables de la mochila
max_tiempo = 120
max_valor_permitido= 100
max_valor=max_valor_permitido
min_estrés = float('inf')
min_duracion = float('inf')
actividades_seleccionadas = []

# Función que calcula el valor, duración y estrés total de un conjunto de actividades
def calcular_mochila(actividades):
    valor_total = 0
    duracion_total = 0
    estres_total = 0
    for actividad in actividades:
        valor_total += actividad[5]
        duracion_total += actividad[4]
        estres_total += actividad[6]
    return valor_total, duracion_total, estres_total

# Función recursiva para encontrar el conjunto de actividades óptimo
def encontrar_mochila(indice, actividades):
    global max_valor, min_estrés, min_duracion, actividades_seleccionadas
    if indice == len(data):
        # Fin de la recursión, comprobar si el conjunto actual es mejor que el mejor encontrado hasta ahora
        valor_actual, duracion_actual, estres_actual = calcular_mochila(actividades)
        if duracion_actual <= max_tiempo and valor_actual >= max_valor_permitido and valor_actual <= max_valor_permitido and estres_actual <= min_estrés:
            max_valor = valor_actual
            min_estrés = estres_actual
            min_duracion = duracion_actual
            actividades_seleccionadas = actividades
        return
    # Excluir la actividad actual
    encontrar_mochila(indice+1, actividades)
    # Incluir la actividad actual si cumple los requisitos
    actividad_actual = data[indice]
    requerimiento1 = actividad_actual[8]
    requerimiento2 = actividad_actual[9]
    if requerimiento1 == 0 or requerimiento1 in [a[3] for a in actividades]:
        if requerimiento2 == 0 or requerimiento2 in [a[3] for a in actividades]:
            encontrar_mochila(indice+1, actividades+[actividad_actual])

# Llamar a la función recursiva para encontrar la mochila óptima
encontrar_mochila(0, [])


# Imprimir los resultados
print("Actividades seleccionadas:")
acum = 0
dura = 0
for actividad in actividades_seleccionadas:
    print("Materia:", actividad[0], "Tema:", actividad[1], "Subtema:", actividad[2], "Número de actividad:", actividad[3], "Duración:", actividad[4], "Valor:", actividad[5])
    acum +=actividad[5]
    dura +=actividad[4]

    i=len(actividades_seleccionadas)
print("Con una calificación de: ", (acum))
print("Con un tiempo de:", dura)
fin = time.time()
print(fin-inicio)
