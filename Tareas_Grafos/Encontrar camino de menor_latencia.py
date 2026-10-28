
# Encontrar la ruta con menor latencia entre dos nodos
import heapq


def dijkstra(grafo, inicio, destino):
    distancias = {inicio: 0}
    anteriores = {}
    cola = [(0, inicio)]

    while cola:
        distancia, nodo = heapq.heappop(cola)

        # Ignorar si ya existe una distancia menor
        if distancia > distancias[nodo]:
            continue

        if nodo == destino:
            break

        # Revisar las conexiones del nodo actual
        for vecino, latencia in grafo.get(nodo, []):
            nueva_distancia = distancia + latencia

            if nueva_distancia < distancias.get(vecino, float('inf')):
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = nodo
                heapq.heappush(cola, (nueva_distancia, vecino))

    # Comprobar si existe una ruta al destino
    if destino not in distancias:
        return [], float('inf')

    # Reconstruir el recorrido encontrado
    ruta = []
    actual = destino

    while actual != inicio:
        ruta.append(actual)
        actual = anteriores[actual]

    ruta.append(inicio)
    ruta.reverse()

    return ruta, distancias[destino]


# Crear el grafo con latencias expresadas en milisegundos
grafo = {
    'A': [('B', 10), ('C', 4)],
    'B': [('D', 5)],
    'C': [('B', 2), ('D', 12)],
    'D': []
}

# Calcular la ruta desde A hasta D
ruta, latencia = dijkstra(grafo, 'A', 'D')

print("Ruta con menor latencia:", " -> ".join(ruta))
print("Latencia acumulada:", latencia, "ms")
