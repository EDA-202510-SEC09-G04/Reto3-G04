def heapify(arr, n, i, key_fn):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and key_fn(arr[left]) < key_fn(arr[smallest]):
        smallest = left

    if right < n and key_fn(arr[right]) < key_fn(arr[smallest]):
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest, key_fn)


def build_heap(arr, key_fn):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i, key_fn)


def heap_insert(arr, key_fn, value):
    arr.append(value)
    i = len(arr) - 1
    while i > 0 and key_fn(arr[i]) < key_fn(arr[(i - 1) // 2]):
        arr[i], arr[(i - 1) // 2] = arr[(i - 1) // 2], arr[i]
        i = (i - 1) // 2


def heap_pop(arr, key_fn):
    if len(arr) == 0:
        return None

    root = arr[0]
    arr[0] = arr[-1]
    arr.pop()
    heapify(arr, len(arr), 0, key_fn)

    return root


# Función de ejemplo para extraer el valor que queremos ordenar
def key_fn(item):
    return item['value']  # Aquí puedes cambiar la clave de ordenación


# Ejemplo de uso
heap = [{'value': 5}, {'value': 3}, {'value': 8}, {'value': 1}, {'value': 4}]
build_heap(heap, key_fn)

print("Heap:", heap)

# Insertar nuevo elemento
heap_insert(heap, key_fn, {'value': 2})
print("Heap after insert:", heap)

# Extraer el elemento mínimo
min_item = heap_pop(heap, key_fn)
print("Min item:", min_item)
print("Heap after pop:", heap)
