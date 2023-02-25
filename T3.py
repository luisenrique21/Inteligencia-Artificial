# Definimos una función para leer los datos del archivo
import time
inicio = time.time()
def leer_archivo(nombre_archivo):
    with open(nombre_archivo) as archivo:
        datos = archivo.readlines()
        n, capacidad = map(int, datos[0].split())     #CAMBIAR A FLOTANTE SI SE TRATA DE PURO NUMERO CON DECIMALES
        elementos = []
        for i in range(1, len(datos)):
            valor, peso = map(int, datos[i].split())  #CAMBIAR A FLOTANTE SI SE TRATA DE PURO NUMERO CON DECIMALES
            elementos.append((valor, peso))
        return n, capacidad, elementos

# Definimos la función para resolver el problema de la mochila
def mochila(nombre_archivo):
    # Leemos los datos del archivo
    n, capacidad, elementos = leer_archivo(nombre_archivo)

    # Ordenamos los elementos por su cociente valor/peso de forma descendente
    elementos = sorted(elementos, key=lambda x: x[0]/x[1], reverse=True)

    # Creamos una lista para almacenar las soluciones parciales
    soluciones = [(0, [])]

    # Recorremos los elementos de la lista
    for valor, peso in elementos:
        # Creamos una nueva lista para almacenar las soluciones parciales que incluyen el elemento actual
        nuevas_soluciones = []
        # Recorremos las soluciones parciales existentes
        for peso_parcial, elementos_parciales in soluciones:
            # Comprobamos si podemos añadir el elemento actual a la solución parcial actual
            if peso_parcial + peso <= capacidad:
                # Si es posible, añadimos el elemento a la solución parcial
                nuevas_soluciones.append((peso_parcial + peso, elementos_parciales + [(valor, peso)]))
        # Añadimos las nuevas soluciones a la lista de soluciones parciales
        soluciones += nuevas_soluciones

    # Seleccionamos la solución con el mayor valor
    solucion_final = max(soluciones, key=lambda x: sum([v for v, p in x[1]]))

    # Devolvemos la solución final
    return solucion_final

# Ejemplo de uso
nombre_archivo = 'f10_l-d_kp_20_879.txt'

# Resolvemos el problema de la mochila
solucion = mochila(nombre_archivo)

# Mostramos la solución
print("La solución es:")
print(f"  Valor optimo: {sum([v for v, p in solucion[1]])}")
print(f"  Peso total: {solucion[0]}")
print(f"  Elementos incluidos: {solucion[1]}")
fin = time.time()
print(fin-inicio)