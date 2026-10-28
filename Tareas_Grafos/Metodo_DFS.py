
# Metodo iterativo para realizar un recorrido DFS

class Grafo:
    def __init__(self):
        self.adyacencia = {}

    def agregar_arista(self, origen, destino):
        # Registrar los nodos si aun no existen
        if origen not in self.adyacencia:
            self.adyacencia[origen] = []

        if destino not in self.adyacencia:
            self.adyacencia[destino] = []

        # Conectar los nodos en ambas direcciones
        self.adyacencia[origen].append(destino)
        self.adyacencia[destino].append(origen)

    def dfs_iterativo(self, inicio):
        visitados = set()
        pila = [inicio]
        resultado = []

        while pila:
            actual = pila.pop()

            if actual not in visitados:
                visitados.add(actual)
                resultado.append(actual)

                # Agregar los vecinos pendientes a la pila
                for vecino in self.adyacencia.get(actual, []):
                    if vecino not in visitados:
                        pila.append(vecino)

        return resultado


# Inicializar el grafo
g = Grafo()

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")
g.agregar_arista("C", "E")

# Mostrar el recorrido en profundidad
print("Resultado del recorrido DFS:", g.dfs_iterativo("A"))
