
# Funcion para encontrar el camino exacto usando Dijkstra
import heapq


def dijkstra(grafo, inicio, destino):
    distancias = {inicio: 0}
    anteriores = {}
    cola = [(0, inicio)]

    while cola:
        distancia, nodo = heapq.heappop(cola)

        if distancia > distancias[nodo]:
            continue

        if nodo == destino:
            break

        # Revisar los vecinos del nodo actual
        for vecino, peso in grafo.get(nodo, []):
            nueva_distancia = distancia + peso

            if nueva_distancia < distancias.get(vecino, float('inf')):
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo
                heapq.heappush(cola, (nueva_distancia, vecino))

    # Si no se llega al destino, devolver una lista vacia
    if destino not in distancias:
        return []

    # Reconstruir el camino encontrado
    camino = []
    actual = destino

    while actual != inicio:
        camino.append(actual)
        actual = anteriores[actual]

    camino.append(inicio)
    camino.reverse()

    return camino


# Definir el grafo con sus conexiones y pesos
grafo = {
    'A': [('B', 10), ('C', 4)],
    'B': [('D', 5)],
    'C': [('B', 2), ('D', 12)],
    'D': []
}

# Obtener el recorrido desde A hasta D
camino = dijkstra(grafo, 'A', 'D')

print("Ruta encontrada:", camino)
