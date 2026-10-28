
# Funcion para comprobar si un grafo dirigido contiene ciclos

def tiene_ciclo(grafo):
    visitados = set()
    pila = set()

    def dfs(nodo):
        visitados.add(nodo)
        pila.add(nodo)

        # Recorrer los nodos conectados
        for vecino in grafo[nodo]:
            if vecino not in visitados:
                if dfs(vecino):
                    return True
            elif vecino in pila:
                return True

        pila.remove(nodo)
        return False

    # Revisar todos los nodos del grafo
    for nodo in grafo:
        if nodo not in visitados:
            if dfs(nodo):
                return True

    return False


# Definir el grafo dirigido
grafo = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

# Mostrar si se encontro un ciclo
if tiene_ciclo(grafo):
    print("Se detecto un ciclo en el grafo.")
else:
    print("No se encontraron ciclos en el grafo.")
