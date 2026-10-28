
# Calcular el grado de entrada y salida de cada nodo

def calcular_grados(grafo):
    for nodo in grafo:
        entrada = 0
        salida = len(grafo[nodo])

        # Contar cuantas conexiones llegan al nodo
        for vecinos in grafo.values():
            for vecino in vecinos:
                if vecino == nodo:
                    entrada += 1

        print(nodo, "- Grado de entrada:", entrada,
              "| Grado de salida:", salida)


# Definir el grafo dirigido
grafo = {
    'A': ['B', 'C'],
    'B': ['C'],
    'C': ['A'],
    'D': ['C']
}

# Calcular los grados de los nodos
calcular_grados(grafo)
