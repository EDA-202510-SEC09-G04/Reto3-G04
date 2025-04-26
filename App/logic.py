import time
import os
import csv
import sys
import pprint as pprint
from datetime import datetime
#from DataStructures.Map import map_separate_chaining as msc
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as slist
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.Utils import error as error
from DataStructures.Tree import red_black_tree as rbt

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
data_dir = os.path.dirname(os.path.realpath('__file__')) + '/Data/'

defualt_limit = 1000
sys.setrecursionlimit(defualt_limit*10)
csv.field_size_limit(2147483647)

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        'registros': lt.new_list(),
        'por_fecha_ocurrido': rbt.new_map(),
        'por_fecha_reportado': rbt.new_map()
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    files = data_dir + 'Crime_in_LA_20.csv'
    input_file = csv.DictReader(open(files, encoding='utf-8'))


    for row in input_file:
        row['DATE OCC'] = datetime.strptime(row["DATE OCC"], "%m/%d/%Y %I:%M:%S %p")
        fecha = row['DATE OCC'].date()
        #lista general
        lt.add_last(catalog['registros'], row)
        
        #arbol por fechas de ocurrido
        if not rbt.contains(catalog['por_fecha_ocurrido'], fecha):
            rbt.put(catalog['por_fecha_ocurrido'], fecha, [])
        
        node = rbt.get(catalog['por_fecha_ocurrido'], fecha)
        node.append(row)
        
    #total_reportes = catalog['por_fecha_ocurrido']['root']['size']
    #print(total_reportes)
    
    primeros = catalog['registros']['elements'][:5]
    ultimos = catalog['registros']['elements'][-5:]
    return catalog, primeros, ultimos 
            
        

# Funciones de consulta sobre el catálogo

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog):
    """
    Retorna el resultado del requerimiento 2
    """
    # TODO: Modificar el requerimiento 2
    pass


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog):
    """
    Retorna el resultado del requerimiento 7
    """
    # TODO: Modificar el requerimiento 7
    pass


def req_8(catalog):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed
