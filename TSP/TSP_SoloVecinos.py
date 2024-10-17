import itertools
import random

# Generar un grafo completo sin bucles (eliminar conexiones consigo mismo)
def generar_grafo_sin_bucles(n):
    grafo = {}
    nodos = [f'c{i+1}' for i in range(n)]
    for i in nodos:
        grafo[i] = {}
        for j in nodos:
            if i != j:
                # Asignar un costo aleatorio más pequeño para otras conexiones
                grafo[i][j] = random.randint(1, 20)
    return grafo

# Resolver el TSP de forma exhaustiva considerando múltiples rutas con el mismo costo mínimo
def tsp_exhaustivo(grafo):
    nodos = list(grafo.keys())
    rutas_permutadas = itertools.permutations(nodos)
    rutas_optimas = []
    costo_minimo = float('inf')

    for ruta in rutas_permutadas:
        costo_actual = 0
        for i in range(len(ruta) - 1):
            costo_actual += grafo[ruta[i]][ruta[i+1]]
        costo_actual += grafo[ruta[-1]][ruta[0]]  # Agregar el costo de regreso al nodo inicial
        if costo_actual < costo_minimo:
            costo_minimo = costo_actual
            rutas_optimas = [ruta]  # Reiniciar la lista con la nueva mejor ruta
        elif costo_actual == costo_minimo:
            rutas_optimas.append(ruta)  # Agregar la ruta que tiene el mismo costo mínimo

    # Devolver las mejores rutas y su costo
    return rutas_optimas, costo_minimo

# Algoritmo greedy para el TSP
def tsp_greedy(nodo_inicial, grafo):
    nodos = list(grafo.keys())
    ruta = [nodo_inicial]
    nodos_restantes = set(nodos) - {nodo_inicial}
    nodo_actual = nodo_inicial
    costo_total = 0

    while nodos_restantes:
        # Encontrar el vecino más cercano que no haya sido visitado
        vecino_mas_cercano = None
        menor_costo = float('inf')

        # Iterar a través de los vecinos restantes y elegir el primero que tenga el menor costo
        for vecino in nodos_restantes:
            costo = grafo[nodo_actual][vecino]
            if costo < menor_costo:
                menor_costo = costo
                vecino_mas_cercano = vecino

        # Sumar el costo al total y movernos al vecino más cercano
        costo_total += menor_costo
        ruta.append(vecino_mas_cercano)
        nodos_restantes.remove(vecino_mas_cercano)
        nodo_actual = vecino_mas_cercano

    # Regresar al nodo inicial para cerrar el ciclo
    costo_regreso = grafo[nodo_actual][nodo_inicial]
    costo_total += costo_regreso
    ruta.append(nodo_inicial)

    return ruta, costo_total

# Convertir el grafo al formato de listas anidadas estilo Maxima, simulando nombres sin comillas
def convertir_a_formato_maxima(grafo):
    formato_maxima = []
    for nodo, vecinos in grafo.items():
        # Formatear el nodo y los vecinos como cadenas sin comillas visibles
        nodo_sin_comillas = nodo
        lista_vecinos = [[vecino, costo] for vecino, costo in vecinos.items()]
        formato_maxima.append([nodo_sin_comillas, lista_vecinos])
    return formato_maxima

# Función para mostrar el formato de salida estilo Maxima, sin comillas en los nombres
def mostrar_formato_maxima(formato_maxima):
    salida = "[\n"
    for nodo, vecinos in formato_maxima:
        salida += f"  [{nodo}, ["
        salida += ", ".join([f"[{vecino}, {costo}]" for vecino, costo in vecinos])
        salida += "]],\n"
    salida = salida.rstrip(",\n") + "\n]"
    print(salida)

# Generar el grafo sin bucles (sin conexiones consigo mismo)
grafo_sin_bucles = generar_grafo_sin_bucles(4)
print("Grafo sin bucles y con costos:")
for nodo, vecinos in grafo_sin_bucles.items():
    print(f"{nodo}: {vecinos}")

#Grafo de ejemplo.
grafo4 = {
    'c1': {'c2': 5, 'c3': 18, 'c4': 1},
    'c2': {'c1': 13, 'c3': 20, 'c4': 4},
    'c3': {'c1': 14, 'c2': 17, 'c4': 20},
    'c4': {'c1': 10, 'c2': 6, 'c3': 1}
}

# Convertir al formato de listas anidadas estilo Maxima
grafo_formato_maxima = convertir_a_formato_maxima(grafo_sin_bucles)
print("Grafo en formato estilo Maxima:")
mostrar_formato_maxima(grafo_formato_maxima)

# Resolver el TSP de forma exhaustiva
rutas_optimas, costo_minimo = tsp_exhaustivo(grafo_sin_bucles)
print("\nMejores rutas encontradas:")
for ruta in rutas_optimas:
    print(ruta)
print("Costo mínimo de las rutas:", costo_minimo)

# Resolver el TSP de forma greedy
ruta_greedy, costo_greedy = tsp_greedy("c1", grafo_sin_bucles)
print("\nRuta encontrada por el algoritmo greedy:")
print(ruta_greedy)
print("Costo total de la ruta greedy:", costo_greedy)
