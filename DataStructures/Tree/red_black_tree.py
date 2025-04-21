from DataStructures.Tree import rbt_node as node
from DataStructures.List import single_linked_list as sl
RED = 0
BLACK = 1

def new_map():
    tree = {
        'root': None,
        'type': 'RBT'
    }
    return tree

def update_size(node):
    size_left = node['left']['size'] if node['left'] else 0
    size_right = node['right']['size'] if node['right'] else 0
    node['size'] = 1 + size_left + size_right
    
    
def default_compare(key, element):
    if key < element['key']:
        return -1
    elif key > element['key']:
        return 1
    else:
        return 0

def flip_node_color(node_rbt):
    if node_rbt is None:
        return None
    node_rbt['color'] = BLACK if node_rbt['color'] == RED else RED
    return node_rbt


def flip_colors(node_rbt):
    flip_node_color(node_rbt)
    if node_rbt['left']:
        flip_node_color(node_rbt['left'])
    if node_rbt['right']:
        flip_node_color(node_rbt['right'])
    return node_rbt

def put(my_rbt, key, value):
    my_rbt['root'] = insert_node(my_rbt['root'], key, value)
    my_rbt['root']['color'] = BLACK  # Asegura que la raíz siempre sea negra
    return my_rbt


def insert_node(root, key, value):
    if root is None:
        return node.new_node(key, value)

    if key < root['key']:
        root['left'] = insert_node(root['left'], key, value)
    elif key > root['key']:
        root['right'] = insert_node(root['right'], key, value)
    else:
        root['value'] = value  

    if node.is_red(root['right']) and not node.is_red(root['left']):
        root = rotate_left(root)

    if node.is_red(root['left']) and node.is_red(root['left']['left']):
        root = rotate_right(root)

    if node.is_red(root['left']) and node.is_red(root['right']):
        flip_colors(root)

    update_size(root)

    return root


def rotate_left(h):
    x = h['right']
    h['right'] = x['left']
    x['left'] = h
    x['color'] = h['color']
    node.change_color(h, 0)
    update_size(h)
    update_size(x)
    return x

def rotate_right(h):
    x = h['left']
    h['left'] = x['right']
    x['right'] = h
    x['color'] = h['color']
    node.change_color(h, 0)  
    update_size(h)
    update_size(x)
    return x


def size(my_rbt):
    return size_tree(my_rbt['root']) if my_rbt['root'] else 0

def size_tree(root):
    if root is None:
        return 0
    return 1 + size_tree(root['left']) + size_tree(root['right'])


def get_node(root, key):
    while root is not None:
        if key < root['key']:
            root = root['left']
        elif key > root['key']:
            root = root['right']
        else:
            return root['value']
    return None

def get(my_rbt, key):
    if my_rbt is not None:
        return get_node(my_rbt['root'], key)

def get_min(my_rbt):
    return get_min_node(my_rbt['root'])


def get_min_node(root):
    if root is None:
        return None  # Si el árbol está vacío, no hay una llave mínima.
    
    while root['left'] is not None:
        root = root['left']  # Sigue hacia el hijo izquierdo
    
    return root['key']  # Retorna la llave del nodo más a la izquierda

def get_max(my_rbt):
    return get_max_node(my_rbt['root'])

def get_max_node(root):
    if root is None:
        return None
    
    while root and root['right'] is not None:
        root = root['right']
    
    return root['key'] if root else None

def balance(root):
    if node.is_red(root['right']) and not node.is_red(root['left']):
        root = rotate_left(root)
    if node.is_red(root['left']) and node.is_red(root['left']['left']):
        root = rotate_right(root)
    if node.is_red(root['left']) and node.is_red(root['right']):
        flip_colors(root)
    
    update_size(root)
    return root


def move_red_left(root):
    """
    Mueve un nodo rojo hacia la izquierda.
    """
    flip_colors(root)
    if node.is_red(root['right']['left']):
        root['right'] = rotate_right(root['right'])
        root = rotate_left(root)
        flip_colors(root)
    return root

def move_red_right(root):
    """
    Mueve un nodo rojo hacia la derecha.
    """
    flip_colors(root)
    if node.is_red(root['left']['left']):
        root = rotate_right(root)
        flip_colors(root)
    return root


def contains(my_rbt, key):
    return get(my_rbt, key) is not None

def delete_min(my_rbt):
    if my_rbt['root'] is None:
        return my_rbt

    if not node.is_red(my_rbt['root']['left']) and not node.is_red(my_rbt['root']['right']):
        node.change_color(my_rbt['root'], node.RED)

    my_rbt['root'] = delete_min_node(my_rbt['root'])

    if my_rbt['root'] is not None:
        node.change_color(my_rbt['root'], node.BLACK)

    return my_rbt

def delete_min_node(root):
    if root['left'] is None:
        return None
    if not node.is_red(root['left']) and not node.is_red(root['left'].get('left')):
        root = move_red_left(root)
    root['left'] = delete_min_node(root['left'])
    return balance(root)

def delete_max(my_rbt):
    if my_rbt['root'] is None:
        return my_rbt

    if not node.is_red(my_rbt['root']['left']) and not node.is_red(my_rbt['root']['right']):
        node.change_color(my_rbt['root'], node.RED)

    my_rbt['root'] = delete_max_node(my_rbt['root'])

    if my_rbt['root'] is not None:
        node.change_color(my_rbt['root'], node.BLACK)

    return my_rbt

def delete_max_node(root):
    if node.is_red(root['left']):
        root = rotate_right(root)

    if root['right'] is None:
        return None

    if not node.is_red(root['right']) and not node.is_red(root['right'].get('left')):
        root = move_red_right(root)

    root['right'] = delete_max_node(root['right'])
    return balance(root)

def remove(my_rbt, key):
    if not contains(my_rbt['root'], key):
        return my_rbt

    if not node.is_red(my_rbt['root']['left']) and not node.is_red(my_rbt['root']['right']):
        node.change_color(my_rbt['root'], node.RED)

    my_rbt['root'] = remove_node(my_rbt['root'], key)

    if my_rbt['root']:
        node.change_color(my_rbt['root'], node.BLACK)

    return my_rbt

def remove_node(root, key):
    if key < root['key']:
        if root['left']:
            if not node.is_red(root['left']) and not node.is_red(root['left'].get('left')):
                root = move_red_left(root)
            root['left'] = remove_node(root['left'], key)
    else:
        if node.is_red(root['left']):
            root = rotate_right(root)
        if key == root['key'] and root['right'] is None:
            return None
        if root['right']:
            if not node.is_red(root['right']) and not node.is_red(root['right'].get('left')):
                root = move_red_right(root)
            if key == root['key']:
                min_node = get_min_node(root['right'])
                root['key'] = min_node['key']
                root['value'] = min_node['value']
                root['right'] = delete_min_node(root['right'])
            else:
                root['right'] = remove_node(root['right'], key)
    return balance(root)

def is_empty(my_rbt):
    return my_rbt['root'] is None

def key_set(my_rbt):
    key_list = sl.new_list()
    if my_rbt['root'] is not None:
        key_set_tree(my_rbt['root'], key_list)
    return key_list

def key_set_tree(root, key_list):
    if root is not None:
        key_set_tree(root['left'], key_list)  # Recorrido izquierdo
        sl.add_last(key_list, root['key'])
        key_set_tree(root['right'], key_list)  # Recorrido derecho

def value_set(my_rbt):
    value_list = sl.new_list()
    if my_rbt['root'] is not None:
        value_set_tree(my_rbt['root'], value_list)
    return value_list

def value_set_tree(root, value_list):
    if root is not None:
        value_set_tree(root['left'], value_list)  # Recorrido izquierdo
        sl.add_last(value_list, root['value'])
        value_set_tree(root['right'], value_list)  # Recorrido derecho

def floor(my_rbt, key):
    return floor_key(my_rbt['root'], key)

def floor_key(root, key):
    if root is None:
        return None  # Si no hay nodo, no hay una llave precedente

    if key == root['key']:
        return root['key']  # Si la llave es igual a la raíz, retornamos la raíz misma

    if key < root['key']:
        # Si la llave es menor que la raíz, seguimos buscando en el subárbol izquierdo
        return floor_key(root['left'], key)

    # Si la llave es mayor que la raíz, la raíz podría ser la llave precedente
    right = floor_key(root['right'], key)
    return right if right is not None else root['key']

def ceiling(my_rbt, key):
    return ceiling_key(my_rbt['root'], key)

def ceiling_key(root, key):
    if root is None:
        return None  # Si no hay nodo, no hay una llave sucesora

    if key == root['key']:
        return root['key']  # Si la llave es igual a la raíz, retornamos la raíz misma

    if key > root['key']:
        # Si la llave es mayor que la raíz, seguimos buscando en el subárbol derecho
        return ceiling_key(root['right'], key)

    # Si la llave es menor que la raíz, la raíz podría ser la llave sucesora
    left = ceiling_key(root['left'], key)
    return left if left is not None else root['key']

def select(my_rbt, pos):
    return select_key(my_rbt['root'], pos)

def select_key(root, pos):
    if root is None:
        return None  # Si el nodo es None, no hay llave

    left_size = size_tree(root['left'])  # Usar size_tree para obtener el tamaño del subárbol izquierdo
    
    if left_size == pos:
        return root['key']  # Si la posición coincide con el tamaño del subárbol izquierdo, esta es la llave
    elif left_size > pos:
        return select_key(root['left'], pos)  # Si la posición está en el subárbol izquierdo
    else:
        return select_key(root['right'], pos - left_size - 1)  # Si la posición está en el subárbol derecho

def rank(my_rbt, key):
    return rank_keys(my_rbt['root'], key)

def rank_keys(root, key):
    if root is None:
        return 0  # Si no hay nodo, no hay llaves predecesoras

    left_size = size_tree(root['left'])  # Tamaño del subárbol izquierdo
    
    if key < root['key']:
        return rank_keys(root['left'], key)  # Si la llave es menor que la raíz, buscamos en el subárbol izquierdo
    elif key > root['key']:
        return left_size + 1 + rank_keys(root['right'], key)  # Si la llave es mayor, contamos el subárbol izquierdo + la raíz y seguimos en el subárbol derecho
    else:
        return left_size  # Si la llave es igual, retornamos el tamaño del subárbol izquierdo

def height(my_rbt):
    if my_rbt is not None:
        return height_tree(my_rbt['root'])
    return 0

def height_tree(root):
    if root is None:
        return -1  # La altura de un árbol vacío es -1
    left_height = height_tree(root['left'])
    right_height = height_tree(root['right'])
    return max(left_height, right_height) + 1  #

def keys(my_rbt, key_initial, key_final):
    keys_list = sl.new_list()
    if my_rbt is not None:
        keys_range(my_rbt['root'], key_initial, key_final, keys_list)
    return keys_list

def keys_range(root, key_initial, key_final, keys_list):
    if root is None:
        return
    if key_initial < root['key']:  # Si la llave inicial es menor que la raíz, exploramos el subárbol izquierdo
        keys_range(root['left'], key_initial, key_final, keys_list)
    
    if key_initial <= root['key'] <= key_final:  # Si la llave está en el rango, la agregamos
        sl.add_last(keys_list,root['key'])
    
    if key_final > root['key']:  # Si la llave final es mayor que la raíz, exploramos el subárbol derecho
        keys_range(root['right'], key_initial, key_final, keys_list)

def values(my_rbt, key_initial, key_final):
    values_list = sl.new_list()
    if my_rbt is not None:
        values_range(my_rbt['root'], key_initial, key_final, values_list)
    return values_list

def values_range(root, key_initial, key_final, values_list):
    if root is None:
        return
    if key_initial < root['key']:  # Si la llave inicial es menor que la raíz, exploramos el subárbol izquierdo
        values_range(root['left'], key_initial, key_final, values_list)
    
    if key_initial <= root['key'] <= key_final:  # Si la llave está en el rango, agregamos el valor
        sl.add_last(values_list,root['value'])
    
    if key_final > root['key']:  # Si la llave final es mayor que la raíz, exploramos el subárbol derecho
        values_range(root['right'], key_initial, key_final, values_list)
