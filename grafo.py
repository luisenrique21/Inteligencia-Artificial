# grafo
import time
inicio = time.time()
import grafo as GR
class Graph():
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de los nodos adyacentes 
    def __init__(self, graph={}):
        self.graph = graph
# Devuelve una representación formal del contenido del grafo
    def __repr__(self):
        nodes = ''
        for node, edges in self.graph.items():
            nodes += f'{node}: {edges}\n'
        return nodes

    # Iterador para recorrer todos los nodos del grafo
    def __iter__(self):
        self.iter_obj = iter(self.graph)
        return self.iter_obj

    # Devuelve los nodos del grafo como una lista
    def nodes(self):
        return list(self.graph.keys())

    # Devuelve los arcos del grafo como una lista de tuplas
    # (nodo_origen, nodo_destino)
    def edges(self, node=None):
        if node:
            if self.existNode(node):
                return [(node, e) for e in self.graph[node]]
            else:
                return []
        else:
            return [(n, e) for n in self.graph.keys() for e in self.graph[n]]

    # Devuelve el número de nodos del grafo
    def order(self):
        return len(self.graph)

    # Devuelve el número de arcos del grafo
    def size(self):
        arcs = []
        for node, edges in self.graph.items():
            for edge in edges:
                sorted_edge = sorted([node, edge])
                if sorted_edge not in arcs:
                    arcs.append(sorted_edge)
        return len(arcs)
                   
    # Devuelve el número de arcos que conectan con el nodo
    # Los lazos se cuentan doblemente
    def degree(self, node):
        if self.graph == {}:
            return -1       # grafo vacío
        degree = len(self.graph[node])
        if node in self.graph[node]:
            degree += 1     # existe un lazo
        return degree

    # Devuelve el grado máximo
    def Delta(self):
        if self.graph == {}:
            return -1       # grafo vacío
        degrees = [self.degree(node) for node in self.graph]
        degrees.sort(reverse=True)
        return degrees[0]
        # Devuelve el camino más corto entre dos nodos
    # camino más corto == menos nodos
    def shortestPath(self, start, end):
        path = sorted(self.findPaths(start, end), key = len)
        return path[0] if path else []

    # Consulta si el grafo está vacío
    def isEmpty(self):
        return self.graph == {}

    # Consulta si el nodo existe en el grafo
    def existNode(self, node):
        return node in self.graph.keys()

    # Consulta si el arco existe en el grafo
    def existEdge(self, edge):
        n1, n2 = tuple(edge)
        return (n1, n2) in self.edges(n1) or (n2, n1) in self.edges(n2)

class WeightedGraph(GR.Graph):
    # Constructor, por defecto crea un diccionario vacío
    # El grafo se presenta como un diccionario de la forma
    # {nodo: [arcos]}
    # arcos es una lista de tuplas de la forma (nodo_destino, peso) 
    def __init__(self, graph={}):
        super().__init__(graph)

    # Devuelve el número de arcos del grafo
    def size(self):
        arcs = []
        for node, edges in self.graph.items():
            for edge, w in edges:
                sorted_edge = sorted([node, edge])
                if sorted_edge not in arcs:
                    arcs.append(sorted_edge)
        return len(arcs)


    # Recorrido en profundidad (Depth First Search)
    def DFS(self, node):
        visited = [node]
        stack = [node]
        while stack:
            current = stack.pop()
            if current not in visited:
                visited.append(current)
            for e, _ in self.graph[current]:    # para cada nodo adyacente
                if e not in visited:
                    stack.append(e)
        return visited

    # Recorrido en anchura (Breadth-First Search)
    def BFS(self, node):
        visited = [node]
        queue = [node]
        while queue:
            current = queue.pop(0)
            if current not in visited:
                visited.append(current)
            for e, _ in self.graph[current]:    # para cada nodo adyacente
                if e not in visited:
                    queue.append(e)
        return visited

    # Devuelve todos los caminos entre dos nodos
    def findPaths(self, start, end, path = []):
        if start not in self.graph or end not in self.graph:
            return []
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node, _ in self.graph[start]:       # para cada nodo adyacente
            if node not in path:
                newpaths = self.findPaths(node, end, path)
                for subpath in newpaths:
                    paths.append(subpath)
        return paths

    def shortestPath(self, start, end):
        INF = float('inf')
        # Diccionario de nodos con un peso infinito
        unvisited = {node: INF for node in self.graph.keys()}
        # Diccionario de predecesores
        predecessor = {node: node for node in self.graph.keys()} 
        visited = {}
        current = start
        currentWeight = 0
        unvisited[current] = currentWeight      # nodo origen peso 0
        while True:
            for node, weight in self.graph[current]:
                if node not in unvisited:
                    continue                    # nodo ya tratado
                newWeight = currentWeight + weight
                if unvisited[node] > newWeight:
                    # Tomar el nodo con el menor peso
                    unvisited[node] = newWeight
                    predecessor[node] = current # predecesor con el menor peso
            visited[current] = currentWeight    # visitado con el menor peso 
            unvisited.pop(current)              # eliminar de los no visitados
            if not unvisited:
                break       # Terminar el bucle si no hay nodos por visitar
            # Tomar el nodo con el menor peso de los no visitados
            candidates = [(n, w) for n, w in unvisited.items() if w != INF]
            current, currentWeight = sorted(candidates, key = lambda x: x[1])[0]
        # Reconstrucción del camino de longitud mínima
        # Se parte del nodo final al inicial
        path = []
        node = end
        while True:
            path.append(node)
            if(node == predecessor[node]):
                break
            node = predecessor[node]
        # Devuelve una tupla con el camino y el peso total
        return (path[::-1], visited[end])
import grafo as GRP


# Grafo ejemplo con listas de adyacencia y pesos asociados
grafo = {'A': [('B', 1), ('C', 2)],
         'B': [('A', 1), ('C', 4)],
         'C': [('A', 2), ('B', 4), ('D', 5)],
         'D': [('A', 3), ('C', 5)]

           }


def testGrafo():
    g = GRP.WeightedGraph(grafo)    # Crear el grafo con el diccionario de ejemplo

    print('Grafo')
    print(g)                    # Visualizar el grafo
    print('Iteración')
    for n in g:                 # Iterar sobre los nodos y arcos del grafo
        print(n)
        print(g.edges(n))
    print('Nodos:', g.nodes())  # Visualizar todos los nodos


    print('Medidas')
    print('Orden:', g.order())              # Obtener orden
    print('Tamaño:', g.size())              # Obtener tamaño
    
    # Obtener todos los caminos posibles entre dos nodos
    #print(g.findPaths('A', 'C'))
    # Obtener el camino más corto entre dos nodos
    path, weight = g.shortestPath('B', 'D')
    print(f'Dijkstra: ruta B-D:{path} peso:{weight}')

if __name__ == '__main__':
    testGrafo()

fin = time.time()
print(fin-inicio) # 1.0005340576171875