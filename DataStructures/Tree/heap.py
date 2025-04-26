# Función heapify para garantizar que la propiedad del max-heap se mantenga
def heapify(arr, n, i, key_fn):
    largest = i  # Cambiar "smallest" por "largest" para max-heap
    left = 2 * i + 1
    right = 2 * i + 2

    # Comparamos el hijo izquierdo con el nodo actual (i)
    if left < n and key_fn(arr[left]) > key_fn(arr[largest]):  # Cambiar '<' por '>'
        largest = left

    # Comparamos el hijo derecho con el nodo actual (i)
    if right < n and key_fn(arr[right]) > key_fn(arr[largest]):  # Cambiar '<' por '>'
        largest = right

    # Si el nodo actual no es el más grande, intercambiamos y seguimos haciendo heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest, key_fn)

# Función para construir el heap desde una lista de elementos
def build_heap(arr, key_fn):
    n = len(arr)
    # Empezamos a hacer heapify desde el último nodo no hoja
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key_fn)

# Función para insertar un nuevo elemento en el heap
def heap_insert(arr, key_fn, value):
    arr.append(value)
    i = len(arr) - 1
    # Nos aseguramos de que el elemento insertado mantenga la propiedad del max-heap
    while i > 0 and key_fn(arr[i]) > key_fn(arr[(i - 1) // 2]):  # Cambiar '<' por '>'
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2

# Función para extraer el elemento máximo (la raíz del heap)
def heap_pop(arr, key_fn):
    if len(arr) == 0:
        return None

    root = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, len(arr), 0, key_fn)  # Aseguramos que el heap mantenga la propiedad

    return root

