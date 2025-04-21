
from pprint import pprint
from DataStructures.List.single_linked_list import add_last, new_list
import DataStructures.Tree.bst_node as bst


def new_map():
    
    map = {'root': None}
    
    return map



def put (my_bst, key,value):
    
   my_bst['root'] =  insert_node(my_bst['root'],key,value)
   
   return my_bst
   

def insert_node(root,key,value):
    if root is None:
        return bst.new_node(key, value)

    if key < root['key']:
        root['left'] = insert_node(root.get('left'), key, value)
    elif key > root['key']:
        root['right'] = insert_node(root.get('right'), key, value)
    else:
        root['value'] = value
        return root  

    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size

    return root



def get(my_bst,key):

    
    node = get_node(my_bst['root'],key)
    if node is not None:
        return node['value']
    else:
        return None


def get_node(root, key):
    if root is None:
        return None

    if root['key'] == key:
        return root
    elif key < root['key']:
        return get_node(root['left'], key)
    elif key > root['key']:
        return get_node(root['right'], key)
        


def encontrar_minimo(nodo):
    
    actual = nodo
    
    while actual['left']:
        
        actual = actual['left']
        
    return actual




def remove(my_bst,key):
    
    my_bst['root'] = remove_node(my_bst['root'],key)
    return my_bst


def remove_node(root,key):
    
    if root == None:
        
        return root
    
    
    if  root['key'] > key:
        
        root['left'] = remove_node(root['left'],key)
        
    elif root['key'] < key:
        
        root['right'] = remove_node(root['right'],key)
        
    
    else:
        
        # Caso 1: El nodo no tiene hijos
        
        if root['left'] is None and root['right'] is None:
            
            return None
        
        # Caso 2: El nodo solo tiene un hijo
        
        if  root['left'] is None:
            
            return root['right']
        
        elif root['right'] is None:
            
            return root['left']
        
        #Caso 3: El nodo tiene dos hijos
        
        sucesor = encontrar_minimo(root['right'])
        root['key'] = sucesor['key']
        root['value'] = sucesor['value']
        root['right'] = remove_node(root['right'], sucesor['key'])
        
    left_size = root['left']['size'] if root['left'] else 0
    right_size = root['right']['size'] if root['right'] else 0
    root['size'] = 1 + left_size + right_size

    
    
    return root




def contains(my_bst,key):
    
   nodo =  get(my_bst,key)
   
   
   if nodo is not None:
       
       return True
   
   else:
       
       return False
   
   

   
def size(my_bst):
    
    return size_tree(my_bst['root'])
   


def size_tree(root):
    
    if root is None:
        
        return 0
    
    return 1 + size_tree(root['right']) + size_tree(root['left'])



def is_empty(my_bst):
    
    if my_bst['root'] is None:
        
        return True
    
    else:
        
        return False
    
    
    
def key_set(my_bst):
    
    
    return key_set_tree(my_bst['root'],None)
    
    
def key_set_tree(root, resultado = None):
    
    if resultado is None:
        
        resultado = new_list()
        
        
    if root is not None:
        
        
        key_set_tree(root['left'],resultado)
        add_last(resultado,root['key'])
        key_set_tree(root['right'], resultado)
        
    return resultado


#COMIENZO FUNCIONES POR DESARROLLAR



def value_set(my_bst):
    return value_set_tree(my_bst['root'], None)


def value_set_tree(root, resultado=None):
    if resultado is None:
        resultado = new_list()

    if root is not None:
        value_set_tree(root['left'], resultado)
        add_last(resultado,root['value'])
        value_set_tree(root['right'], resultado)

    return resultado

def get_min(my_bst):
    min_node = get_min_node(my_bst['root'])
    if min_node is not None:
        return min_node['key']
    else:
        return None

def get_min_node(node):
    current = node
    while current is not None and current['left'] is not None:
        current = current['left']
    return current



def get_max(my_bst):
    max_node = get_max_node(my_bst['root'])
    if max_node is not None:
        return max_node['key']
    else:
        return None

def get_max_node(node):
    current = node
    while current is not None and current['right'] is not None:
        current = current['right']
    return current

def delete_min(my_bst):
    my_bst['root'] = delete_min_tree(my_bst['root'])
    return my_bst

def delete_min_tree(node):
    if node is None:
        return None

    # Caso base: si ya no hay hijo izquierdo, este es el mínimo
    if node['left'] is None:
        return node['right']

    node['left'] = delete_min_tree(node['left'])

    left_size = node['left']['size'] if node['left'] else 0
    right_size = node['right']['size'] if node['right'] else 0
    node['size'] = 1 + left_size + right_size

    return node

def delete_max(my_bst):
    my_bst['root'] = delete_max_tree(my_bst['root'])
    return my_bst
def delete_max_tree(node):
    if node is None:
        return None

    if node['right'] is None:
        return node['left']  

    node['right'] = delete_max_tree(node['right'])

    left_size = node['left']['size'] if node['left'] else 0
    right_size = node['right']['size'] if node['right'] else 0
    node['size'] = 1 + left_size + right_size

    return node


def floor(my_bst, key):
    result = floor_key(my_bst['root'], key)
    if result is not None:
        return result['key']
    else:
        return None

def floor_key(root, key):
    if root is None:
        return None

    if root['key'] == key:
        return root

    if root['key'] > key:
        return floor_key(root['left'], key)

    temp = floor_key(root['right'], key)
    if temp is not None:
        return temp
    else:
        return root
    
def ceiling(my_bst, key):
    result = ceiling_key(my_bst['root'], key)
    if result is not None:
        return result['key']
    else:
        return None
    
def ceiling_key(root, key):
    if root is None:
        return None

    if root['key'] == key:
        return root

    if root['key'] < key:
        return ceiling_key(root['right'], key)

    temp = ceiling_key(root['left'], key)
    if temp is not None:
        return temp
    else:
        return root

def select(my_bst, pos):
    node = select_key(my_bst['root'], pos)
    if node is not None:
        return node['key']
    else:
        return None

def select_key(root, pos):
    if root is None:
        return None

    left_size = 0
    if root['left'] is not None:
        left_size = root['left']['size']

    if pos < left_size:
        return select_key(root['left'], pos)
    elif pos > left_size:
        return select_key(root['right'], pos - left_size - 1)
    else:
        return root

def rank(my_bst, key):
    return rank_keys(my_bst['root'], key)

def rank_keys(root, key):
    if root is None:
        return 0

    if key < root['key']:
        return rank_keys(root['left'], key)
    
    elif key > root['key']:
        left_size = 0
        if root['left'] is not None:
            left_size = root['left']['size']
        return 1 + left_size + rank_keys(root['right'], key)
    
    else: 
        left_size = 0
        if root['left'] is not None:
            left_size = root['left']['size']
        return left_size
    
def height(my_bst):
    return height_tree(my_bst['root'])

def height_tree(root):
    if root is None:
        return 0

    left_height = height_tree(root['left'])
    right_height = height_tree(root['right'])

    return 1 + max(left_height, right_height)

def keys(my_bst, key_initial, key_final):
    list_key = new_list()
    keys_range(my_bst['root'], key_initial, key_final, list_key)
    return list_key


def keys_range(root, key_initial, key_final, list_key):
    if root is None:
        return

    if root['key'] > key_initial:
        keys_range(root['left'], key_initial, key_final, list_key)

    if key_initial <= root['key'] <= key_final:
        add_last(list_key, root['key'])  

    if root['key'] < key_final:
        keys_range(root['right'], key_initial, key_final, list_key)

def values(my_bst, key_initial, key_final):
    list_values = new_list()
    values_range(my_bst['root'], key_initial, key_final, list_values)
    return list_values


def values_range(root, key_initial, key_final, list_values):
    if root is None:
        return

    # Buscar en el subárbol izquierdo si es posible
    if root['key'] > key_initial:
        values_range(root['left'], key_initial, key_final, list_values)

    # Solo agregar si está dentro del rango
    if key_initial <= root['key'] <= key_final:
        add_last(list_values, root['value'])

    # Buscar en el subárbol derecho si es posible
    if root['key'] < key_final:
        values_range(root['right'], key_initial, key_final, list_values)


def default_compare(key, element):
   if key == bst.get_key(element):
      return 0
   elif key > bst.get_key(element):
      return 1
   return -1