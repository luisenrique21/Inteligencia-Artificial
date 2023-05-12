import csv
import heapq
import time
inicio = time.time()
# Abrir el archivo CSV y leer los datos
with open('i_5_2.csv', 'r') as f:
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
max_valor = 70
min_estrés = float('inf')
min_duracion = 0
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


# Clase Nodo para el algoritmo A*
class Nodo:
    def __init__(self, actividades, valor, duracion, estres, indice):
        self.actividades = actividades
        self.valor = valor
        self.duracion = duracion
        self.estres = estres
        self.indice = indice

    def __lt__(self, otro):
        return self.valor < otro.valor

    def calcular_f(self):
        # Calcula el valor de la función de evaluación f = g + h
        g = self.valor
        h = self.duracion + self.estres
        return g + h

    def expandir(self):
        # Expande el nodo actual agregando actividades que cumplan los requerimientos
        nodos_hijos = []
        for i in range(self.indice + 1, len(data)):
            actividad_actual = data[i]
            requerimiento1 = actividad_actual[8]
            requerimiento2 = actividad_actual[9]
            if requerimiento1 == 0 or requerimiento1 in [a[3] for a in self.actividades]:
                if requerimiento2 == 0 or requerimiento2 in [a[3] for a in self.actividades]:
                    valor_nuevo = self.valor + actividad_actual[5]
                    duracion_nueva = self.duracion + actividad_actual[4]
                    estres_nuevo = self.estres + actividad_actual[6]
                    if duracion_nueva <= max_tiempo and estres_nuevo <= min_estrés:
                        actividades_nuevas = self.actividades + [actividad_actual]
                        nodo_hijo = Nodo(actividades_nuevas, valor_nuevo, duracion_nueva, estres_nuevo, i)
                        nodos_hijos.append(nodo_hijo)
        return nodos_hijos

# Función para encontrar el conjunto de actividades con valor máximo utilizando el algoritmo A*
def encontrar_mochila():
    global max_valor, min_estrés, min_duracion, actividades_seleccionadas
    heap = [Nodo([], 0, 0, 0, -1)]
    while heap:
        nodo_actual = heapq.heappop(heap)
        if nodo_actual.duracion < max_tiempo and nodo_actual.estres <= min_estrés:
            valor_actual, duracion_actual, estres_actual = calcular_mochila(nodo_actual.actividades)
            if valor_actual >= max_valor and valor_actual <= max_valor:
                max_valor = valor_actual
                min_estrés = estres_actual
                min_duracion = duracion_actual
                actividades_seleccionadas = nodo_actual.actividades
        for nodo_hijo in nodo_actual.expandir():
            heapq.heappush(heap, nodo_hijo)

# Llamada a la función para encontrar la mochila
encontrar_mochila()

# Imprimir la información de las actividades seleccionadas
print("Actividades seleccionadas:")
acum = 0
dura = 0
for actividad in actividades_seleccionadas:
    print(f"{actividad[1]} (Duración: {actividad[4]}, Valor: {actividad[5]})")
    acum += actividad[5]
    dura += actividad[4]
    i = len(actividades_seleccionadas)
print("Con una calificación de: ", acum)
print("Con un tiempo de:", dura)
fin = time.time()
print(fin-inicio)