
import heapq


class SistemaGPS:
    def __init__(self):
        # Diccionario para guardar las ciudades y sus conexiones
        self.grafo = {}

    def agregar_ciudad(self, ciudad):
        # Registrar la ciudad si no está agregada
        if ciudad not in self.grafo:
            self.grafo[ciudad] = []
            return True
        return False

    def agregar_ruta(self, origen, destino, tiempo):
        # Verificar que el tiempo sea válido
        if tiempo <= 0:
            print("El tiempo debe ser mayor que cero.")
            return

        # Registrar las ciudades si hacen falta
        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)

        # Revisar si ya hay una conexión entre las ciudades
        for ciudad, minutos in self.grafo[origen]:
            if ciudad == destino:
                print("La ruta ya se encuentra registrada.")
                return

        # Guardar la conexión en los dos sentidos
        self.grafo[origen].append((destino, tiempo))
        self.grafo[destino].append((origen, tiempo))

        print("La ruta se agregó correctamente.")

    def mostrar_ciudades(self):
        # Verificar si hay ciudades guardadas
        if not self.grafo:
            print("Todavía no hay ciudades registradas.")
            return

        print("\n--- LISTADO DE CIUDADES Y CONEXIONES ---")

        for ciudad, rutas in self.grafo.items():
            print(f"\n{ciudad}:")

            if not rutas:
                print("  No tiene rutas conectadas.")
            else:
                for destino, tiempo in rutas:
                    print(f"  -> {destino}: {tiempo} minutos")

    def dijkstra(self, origen, destino):
        # Verificar que las dos ciudades estén registradas
        if origen not in self.grafo or destino not in self.grafo:
            print("No se encontraron una o ambas ciudades.")
            return

        # Inicializar las distancias de todas las ciudades
        distancias = {
            ciudad: float("inf") for ciudad in self.grafo
        }
        distancias[origen] = 0

        # Registrar las ciudades anteriores del recorrido
        anteriores = {}

        # Cola de prioridad con el tiempo y la ciudad
        cola = [(0, origen)]

        while cola:
            tiempo_actual, ciudad_actual = heapq.heappop(cola)

            # Saltar si ya existe un tiempo más corto
            if tiempo_actual > distancias[ciudad_actual]:
                continue

            # Finalizar cuando se alcance el destino
            if ciudad_actual == destino:
                break

            # Examinar las conexiones de la ciudad actual
            for vecino, tiempo in self.grafo[ciudad_actual]:
                nuevo_tiempo = tiempo_actual + tiempo

                if nuevo_tiempo < distancias[vecino]:
                    distancias[vecino] = nuevo_tiempo
                    anteriores[vecino] = ciudad_actual

                    heapq.heappush(
                        cola, (nuevo_tiempo, vecino)
                    )

        # Comprobar si se pudo llegar al destino
        if distancias[destino] == float("inf"):
            print("No se encontró una ruta entre las ciudades.")
            return

        # Recuperar el recorrido desde el destino hasta el origen
        ruta = []
        ciudad_actual = destino

        while ciudad_actual != origen:
            ruta.append(ciudad_actual)
            ciudad_actual = anteriores[ciudad_actual]

        ruta.append(origen)
        ruta.reverse()

        # Presentar la ruta encontrada
        print("\n--- RESULTADO DE LA RUTA MÁS RÁPIDA ---")
        print("Ciudad de origen:", origen)
        print("Ciudad de destino:", destino)
        print("Recorrido:", " -> ".join(ruta))
        print("Tiempo total:", distancias[destino], "minutos")

    def menu(self):
        # Mostrar las opciones del programa
        while True:
            print("\n===== SISTEMA DE NAVEGACIÓN GPS =====")
            print("1. Consultar ciudades y rutas")
            print("2. Registrar una ciudad")
            print("3. Registrar una ruta")
            print("4. Encontrar la ruta más rápida")
            print("5. Salir")

            opcion = input("Ingrese una opción: ").strip()

            if opcion == "1":
                self.mostrar_ciudades()

            elif opcion == "2":
                ciudad = input("Ingrese el nombre de la ciudad: ").strip()

                if ciudad:
                    if self.agregar_ciudad(ciudad):
                        print("La ciudad se registró correctamente.")
                    else:
                        print("Esta ciudad ya está registrada.")
                else:
                    print("Debe ingresar el nombre de la ciudad.")

            elif opcion == "3":
                origen = input("Ingrese la ciudad de origen: ").strip()
                destino = input("Ingrese la ciudad de destino: ").strip()

                try:
                    tiempo = float(
                        input("Ingrese el tiempo en minutos: ")
                    )

                    if not origen or not destino:
                        print("Debe ingresar ambas ciudades.")
                    elif origen == destino:
                        print("Las ciudades deben ser diferentes.")
                    else:
                        self.agregar_ruta(origen, destino, tiempo)

                except ValueError:
                    print("Ingrese un valor numérico válido.")

            elif opcion == "4":
                origen = input("Ingrese la ciudad de origen: ").strip()
                destino = input("Ingrese la ciudad de destino: ").strip()

                self.dijkstra(origen, destino)

            elif opcion == "5":
                print("Gracias por utilizar el Sistema GPS.")
                break

            else:
                print("Opción incorrecta. Intente de nuevo.")


# Crear una instancia del sistema GPS
gps = SistemaGPS()

# Registrar algunas rutas de ejemplo
gps.agregar_ruta("Managua", "Masaya", 35)
gps.agregar_ruta("Managua", "Granada", 45)
gps.agregar_ruta("Masaya", "Granada", 20)
gps.agregar_ruta("Granada", "Rivas", 60)
gps.agregar_ruta("Masaya", "León", 75)
gps.agregar_ruta("León", "Managua", 50)

# Ejecutar el menú principal
gps.menu()
