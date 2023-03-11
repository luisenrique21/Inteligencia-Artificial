import time
inicio = time.time()

def bellman_ford(grafo, origen, destino):
    distancias = {vertice: float('inf') for vertice in grafo}
    distancias[origen] = 0
    previos = {vertice: None for vertice in grafo} # nodos previos al camino mas corto
    solucion_optima = float('inf')

    for _ in range(len(grafo) - 1):
        for vertice in grafo:
            for vecino, peso in grafo[vertice]:
                nueva_distancia = distancias[vertice] + peso
                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    previos[vecino] = vertice

    for vertice in grafo:
        for vecino, peso in grafo[vertice]:
            if distancias[vertice] + peso < distancias[vecino]:
                print("El grafo contiene un ciclo de peso negativo")
                return

            if vertice == destino:
                solucion_optima = min(solucion_optima, distancias[destino])


    print(f"Solución óptima: {solucion_optima}")

    # reconstruir el camino mas corto
    camino = []
    nodo_actual = destino
    while nodo_actual is not None:
        camino.append(nodo_actual)
        nodo_actual = previos[nodo_actual]
    camino.reverse()

    print(f"Camino más corto: {camino}")
    return distancias





grafo = {'A': [('B', 1), ('C', 2), ('D', 3), ('O',2), ('X', 2), ('A0', 2)],
         'B': [('A', 1), ('C', 4), ('F',2), ('M',4)],
         'C': [('A', 2), ('B', 4), ('D', 5), ('E', 5), ('U', 3), ('V', 3)],
         'D': [('A', 3), ('C', 5), ('E', 1), ('T', 1), ('X', 3)],
         'E': [('C', 5), ('D', 1), ('I', 3), ('L', 3)],
         'F': [('B', 2), ('G', 3), ('H', 2), ('U', 2)],
         'G': [('F', 3), ('H', 4), ('I', 2), ('J', 3), ('U', 3)],
         'H': [('F', 2), ('G', 4), ('K', 2)],
         'I': [('E', 3), ('G', 2), ('J', 5), ('K', 5), ('R', 3), ('V', 2)],
         'J': [('G', 3), ('I', 5), ('N', 3), ('D0', 2)],
         'K': [('M', 5), ('H', 2), ('I', 5), ('B0', 3), ('D0', 2)],
         'L': [('E', 3), ('T', 2), ('P', 3), ('W', 1)],
         'M': [('B', 4), ('K', 5), ('B0', 2), ('H0', 2)],
         'N': [('J', 3), ('S', 3), ('Y', 2)],
         'O': [('A', 2), ('T', 2), ('P', 4), ('A0', 3), ('E0', 3)],
         'P': [('O', 4), ('L', 3), ('C0', 2), ('E0', 2)],
         'Q': [('T', 5), ('S', 5), ('W', 2), ('Z', 2)],
         'R': [('I', 3), ('S', 1), ('Y', 2), ('Z', 2)],
         'S': [('Q', 5), ('R', 1), ('N', 3)],
         'T': [('D', 1), ('O', 2), ('L', 2), ('Q', 5)],
         'U': [('C', 3), ('F', 2), ('G', 3)],
         'V': [('C', 3), ('I', 2)],
         'W': [('L', 1), ('Q', 2), ('Z', 3), ('C0', 3)],
         'X': [('A', 2), ('D', 3)],
         'Y': [('N', 2), ('R', 2), ('Z', 4)],
         'Z': [('Q', 2), ('R', 2), ('W', 3), ('Y', 4)],
         'A0': [('A', 2), ('O', 3), ('H0', 3)],
         'B0': [('M', 2), ('K', 3), ('D0', 3)],
         'C0': [('P', 2), ('W', 3), ('F0', 3)],
         'D0': [('K', 2), ('J', 1), ('B0', 2), ('G0', 2), ('I0', 2)],
         'E0': [('O', 3), ('P', 2), ('F0', 3), ('M0', 3)],
         'F0': [('C0', 3), ('G0', 5), ('E0', 3), ('J0', 2), ('K0',2), ('N0', 2)],
         'G0': [('F0', 5), ('D0', 2)],
         'H0': [('A0', 3), ('I0', 2), ('M', 2), ('L0', 2), ('M0', 5)],
         'I0': [('H0', 2), ('D0', 2)],
         'J0': [('F0', 2), ('N0', 2), ('U0', 3)],
         'K0': [('F0', 2), ('L0', 2)],
         'L0': [('H0', 2), ('K0', 2)],
         'M0': [('H0', 5), ('E0', 3)],
         'N0': [('F0', 2), ('J0', 2)],
         'O0': [('P0', 2), ('Q0', 2)],
         'P0': [('T0', 3), ('O0', 2)],
         'Q0': [('O0', 2), ('R0', 3)],
         'R0': [('Q0', 3), ('S0', 3)],
         'S0': [('V0', 2), ('R0', 3)],
         'T0': [('P0', 3), ('U0', 3)],
         'U0': [('W0', 4), ('T0', 3), ('X0', 3), ('J0', 3)],
         'V0': [('S0', 2), ('W0', 3), ('X0', 3)],
         'W0': [('V0', 3), ('U0', 4), ('X0', 4)],
         'X0': [('W0', 4), ('V0', 3), ('U0', 3)],
           }


#valor_optimo, distancia =
bellman_ford(grafo, 'A','O')
fin = time.time()
print(fin-inicio)
#print(f"El valor óptimo es {valor_optimo} y la distancia es {distancia}")