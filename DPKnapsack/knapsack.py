# Programa knapsack sin utilizar librerías externas
import random

# Función para generar ítems aleatorios
def generate_random_items(n_items, max_value, max_weight):
    items = []
    for i in range(n_items):
        value = random.randint(1, max_value)
        weight = random.randint(1, max_weight)
        name = chr(97 + i)  # Generar nombres como 'a', 'b', 'c', etc.
        items.append((name, [value, weight]))
    return items

def knapsack(items, capacity):
    # Inicializar la tabla del knapsack
    n = len(items)
    dp = [[(0, []) for _ in range(capacity + 1)] for _ in range(n)]
    
    # Llenar la tabla con la lógica del knapsack
    for i in range(n):
        name, (value, weight) = items[i]
        for w in range(1, capacity + 1):
            if weight > w:
                # Si el peso del objeto es mayor que el peso permitido
                dp[i][w] = dp[i - 1][w] if i > 0 else dp[i][w]
            else:
                if i == 0:
                    dp[i][w] = (value, [name])
                else:
                    previous_value, previous_items = dp[i - 1][w]
                    value_with_item, items_with_item = dp[i - 1][w - weight]
                    value_with_item += value
                    items_with_item = items_with_item + [name]
                    if value_with_item > previous_value:
                        dp[i][w] = (value_with_item, items_with_item)
                    else:
                        dp[i][w] = dp[i - 1][w]
    
    # Crear la tabla que refleje el formato esperado sin librerías
    result = [["xx"] + [i for i in range(1, capacity + 1)]]
    
    for i in range(n):
        name = items[i][0]
        row = [name]
        for w in range(1, capacity + 1):
            value, packed_items = dp[i][w]
            row.append([value, packed_items])
        result.append(row)
    
    # Retornar el resultado como lista
    return result

# Lista de items
items = [ 
("w", [70,1]),
("g", [60,1]),
("n", [90,2]),
("b", [90,4]),
("s", [80,1])
]

items2 = [ 
    ('g', [1500,1]),
    ('s', [3000,4]),
    ('l', [2000,3]),
    ('i', [2000,1])
]

items3 = [ 
("a", [10, 2]),
("b", [20, 3]),
("c", [50, 4]),
("d", [60, 5])
]




# Función para generar el formato de salida compatible con Maxima
def knapsack_maxima_format(items):
    output = "[\n"
    for name, (value, weight) in items:
        output += f"[{name}, [{value},{weight}]],\n"
    output = output.rstrip(",\n") + "\n]"
    return output

def print_knapsack_table(result):
    # Determinar el ancho máximo para cada columna
    col_widths = [max(len(str(item)) for item in col) for col in zip(*result)]
    
    # Imprimir la tabla con el formato ajustado
    for row in result:
        print(" | ".join(f"{str(item):<{col_widths[i]}}" for i, item in enumerate(row)))

# Generar ítems aleatorios y mostrarlos en formato Maxima
# Cuantos items quiere, peso máximo de precio, peso máximo de mochila.
random_items = generate_random_items(6, 1000, 8)
# imprimir en formato maxima.
maxima_format_output = knapsack_maxima_format(random_items)

# Mostrar el resultado en formato Maxima
print("Lista generada: ")
print(maxima_format_output, "\n")


# Capacidad del knapsack

print("Resultado: ")
# Ejecutar el knapsack y mostrar el resultado
#encontrar knapsack con la lista generada e inserte de cuantas columnas.
result = knapsack(random_items, 4)
print_knapsack_table(result)
