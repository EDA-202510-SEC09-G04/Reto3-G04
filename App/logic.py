import time
import os
import csv
import sys
import pprint as pprint
from datetime import datetime
from DataStructures.Map import map_separate_chaining as msc
from DataStructures.List import array_list as lt
from DataStructures.List import single_linked_list as slist
from DataStructures.Map import map_entry as me
from DataStructures.Map import map_functions as mf
from DataStructures.Utils import error as error
from DataStructures.Tree import red_black_tree as rbt
from DataStructures.Tree import heap as hp


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
        'por_fecha_reportado': rbt.new_map(),
        'por_area': msc.new_map(29,0.75),
        'por_edad': rbt.new_map()
    }
    return catalog


# Funciones para la carga de datos

def load_data(catalog):
    """
    Carga los datos del reto
    """
    tiempo_inicial = get_time()
    files = data_dir + 'Crime_in_LA_20.csv'
    input_file = csv.DictReader(open(files, encoding='utf-8'))


    for row in input_file:
        row['DATE OCC'] = datetime.strptime(row["DATE OCC"], "%m/%d/%Y %I:%M:%S %p")
        row['Date Rptd'] = datetime.strptime(row["Date Rptd"], "%m/%d/%Y %I:%M:%S %p")

        fecha_ocurrido = row['DATE OCC'].date()
        #lista general
        lt.add_last(catalog['registros'], row)
        
        #arbol por fechas de ocurrido
        if not rbt.contains(catalog['por_fecha_ocurrido'], fecha_ocurrido):
            rbt.put(catalog['por_fecha_ocurrido'], fecha_ocurrido, [])
        
        node = rbt.get(catalog['por_fecha_ocurrido'], fecha_ocurrido)
        node.append(row)
        
        #arbol por fechas reportado
        fecha_reportado = row['Date Rptd'].date()
        if not rbt.contains(catalog['por_fecha_reportado'], fecha_reportado):
            rbt.put(catalog['por_fecha_reportado'], fecha_reportado, [])
            
        node2 = rbt.get(catalog['por_fecha_reportado'], fecha_reportado)
        node2.append(row)
        
        #hash de area -> lista de diccionarios -> priority queue por fecha reportado
        area = row['AREA NAME']
        if not msc.contains(catalog['por_area'], area):
            msc.put(catalog['por_area'], area, [])
        
        area_list = msc.get(catalog['por_area'], area)
        area_list.append(row)
        msc.put(catalog['por_area'], area, area_list)
        
        #arbol por edad -> lista de crimenes con victima de esas edades
        edad = int(row['Vict Age'])
        if not rbt.contains(catalog['por_edad'], edad):
            rbt.put(catalog['por_edad'], edad, [])
        
        node = rbt.get(catalog['por_edad'], edad)
        node.append(row)
    
    primeros = catalog['registros']['elements'][:5]
    ultimos = catalog['registros']['elements'][-5:]
    
    tiempo_final = get_time()
    delta = delta_time(tiempo_inicial, tiempo_final)
    
    return catalog, primeros, ultimos, delta
            
        

# Funciones de consulta sobre el catálogo
def busqueda_entre_fechas(node, inicial, final, resultados):
    
    if node is None:
        return
    # Si la clave del nodo actual está dentro del rango, agregamos su información
    if inicial <= node['key'] <= final:
        resultados.extend(node['value'])  

    # Si la clave del nodo actual es mayor que el inicio, podemos encontrar más a la izquierda
    if inicial < node['key']:
        busqueda_entre_fechas(node['left'], inicial, final, resultados)

    # Si la clave del nodo actual es menor que el final, podemos encontrar más a la derecha
    if node['key'] < final:
        busqueda_entre_fechas(node['right'], inicial, final, resultados)

def busqueda_entre_edades(node, edad_inicial, edad_final, res):
    if node is None:
        return
    
    if edad_inicial < node['key']:
        busqueda_entre_edades(node['left'], edad_inicial, edad_final, res)
    
    if edad_inicial <= node['key'] <= edad_final:
        res.extend(node['value'])
    
    if node['key'] < edad_final:
        busqueda_entre_edades(node['right'], edad_inicial, edad_final, res)

        
def rango_fechas_catalogo(catalog):
    """
    Devuelve la fecha mínima y máxima de los crímenes cargados
    """
    fechas = [row['DATE OCC'].date() for row in catalog['registros']['elements']]
    fechas.sort()
    return fechas[0], fechas[-1]

def get_data(catalog, id):
    """
    Retorna un dato por su ID.
    """
    #TODO: Consulta en las Llamar la función del modelo para obtener un dato
    pass


def req_1(catalog,fecha_inicial,fecha_final):
    
    tiempo_inicial = get_time()
    
    fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d").date()
    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d").date()

    # Recorrer el árbol manualmente
    root = catalog['por_fecha_ocurrido']['root']
    crimenes_en_rango = []
    busqueda_entre_fechas(root, fecha_inicial, fecha_final, crimenes_en_rango)

   
    crimenes_list = []
    for crimen in crimenes_en_rango:
        if isinstance(crimen, dict):
            crimenes_list.append(crimen)

    print("Cantidad total de crímenes después de buscar:", len(crimenes_list))

    # Definir key de ordenamiento
    def key_fn(item):
        hora = int(item['TIME OCC']) if isinstance(item['TIME OCC'], str) else item['TIME OCC']
        return (
            item['DATE OCC'].date(),
            hora,
            ''.join(chr(255 - ord(c)) for c in item['AREA NAME'])
        )

    # Ordenar
    
    crimenes_ordenados = sorted(crimenes_list, key=key_fn, reverse=True)

    tiempo_final = get_time()
    delta = delta_time(tiempo_inicial, tiempo_final)


    return crimenes_ordenados, delta

def req_2(catalog, fecha_inicial, fecha_final):


    tiempo_inicial = get_time()
    root = catalog['por_fecha_reportado']['root']
    fecha_inicial = datetime.strptime(fecha_inicial, "%Y-%m-%d").date()
    fecha_final = datetime.strptime(fecha_final, "%Y-%m-%d").date()
    resultados = []
    result_data = []
    
    busqueda_entre_fechas(root,fecha_inicial,fecha_final,resultados)
    
    
    for i in resultados:
        
        if i['Part 1-2'] == '1':
         new_data = {
            
            'DR_NO': i['DR_NO'],
            'DATE OCC':i['DATE OCC'],
            'TIME OCC': i['TIME OCC'],
            'AREA':i['AREA'],
            'AREA NAME':i['AREA NAME'],
            'Part 1-2': i['Part 1-2'],
            'Crm Cd':i['Crm Cd'],
            'Status':i['Status']
            
         }
         
         result_data.append(new_data)

    tiempo_final = get_time()
    
    delta_time = tiempo_final - tiempo_inicial

    return result_data , delta_time




         
    

    


def req_3(catalog, n, area):
    """
    Retorna el resultado del requerimiento 3
    """
    #lista de los crimenes del area
    tiempo_inicial = get_time()
    
    area_selected = msc.get(catalog['por_area'], area)
    
    #crear heap a partir del area
    def key_fn(item):
        return (item['Date Rptd'], ''.join(chr(255 - ord(c)) for c in item['AREA NAME']))

    hp.build_heap(area_selected, key_fn)
    size = len(area_selected)
    
    top_n = []
    for _ in range(n):  
        top_n.append(hp.heap_pop(area_selected, key_fn))
    
    tiempo_final = get_time()
    delta_time = tiempo_final - tiempo_inicial    
    
    return top_n, size, delta_time
    
    
    
def numero_crimenes_por_edad(catalog,n,edad_inicial,edad_final):
    
    root = catalog['por_edad']['root']
    resultado = []
    resultado_crimenes_graves = []
    resultado_crimenes_pequeños = []
    total_number = len(resultado)
    
    
    busqueda_entre_fechas(root,edad_inicial,edad_final,resultado)
    resultado.sort(key=lambda x: x ['Vict Age'])
    
    for i in range(n,1,-1):
        
        new_data = {
            'DR_NO': resultado[i]['DR_NO'],
            'Date Rptd': resultado[i]['Date Rptd'],
            'DATE OCC': resultado[i]['DATE OCC'],
            'TIME OCC': resultado[i]['TIME OCC'],
            'AREA': resultado[i]['AREA'],
            'AREA NAME': resultado[i]['AREA NAME'],
            'Part 1-2': resultado[i]['Part 1-2'],
            'Crm Cd': resultado[i]['Crm Cd'],
            'Vict Age': resultado[i]['Vict Age'],
            'Status': resultado[i]['Status'],
            'LOCATION': resultado[i]['LOCATION']
            
        }
        
        if resultado[i]['Part 1-2'] == '1':
            
            resultado_crimenes_graves.append(new_data)
        
        elif resultado[i]['Part 1-2'] == '2':
            
            resultado_crimenes_pequeños.append(new_data)
    
    
    
    resultado_crimenes_graves.sort(key= lambda x: (-int(x['Vict Age']), x['Date Rptd']))
    resultado_crimenes_pequeños.sort(key= lambda x: (-int(x['Vict Age']), x['Date Rptd']))
    
    return resultado_crimenes_graves + resultado_crimenes_pequeños, total_number
            
    
    
   
        
        

    
    


def req_4(catalog,n,edad_inicial,edad_final):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    tiempo_incial = get_time()
    resultados, total = numero_crimenes_por_edad(catalog,n,edad_inicial,edad_final)
    tiempo_final = get_time()
    
    delta_time = tiempo_final - tiempo_incial

    
    return resultados, total, delta_time

def req_5(catalog, n, inicial, final):
    """
    Retorna el resultado del requerimiento 5
    """
    #buscar crimenes entre rango de fechas con el arbol por fecha

    #cambiar a formato m d y
    tiempo_inicial = get_time()

    inicial = datetime.strptime(inicial, "%Y-%m-%d").date()
    final = datetime.strptime(final, "%Y-%m-%d").date()
    root= catalog['por_fecha_ocurrido']['root']
    res = []
    busqueda_entre_fechas(root, inicial, final, res)
    
    #lista por areas
    areas = {}
    size = 0
    for crimen in res:
        if crimen['Status'] == 'IC':
            size += 1
            area = crimen['AREA']
            if not area in areas:
                dato = {
                    'area_number': crimen['AREA'],
                    'area_name' : crimen['AREA NAME'],
                    'count' : 0,
                    'mayor': datetime.strptime('01/01/1000', "%m/%d/%Y"),
                    'menor': datetime.strptime('01/01/3000', "%m/%d/%Y"),
                }
                areas[area] = dato
                
            dato = areas[area]
            #aumentar counter
            dato['count'] = dato['count'] + 1
            
            #cambiar la date mayor o menor si la fecha del crimen es mayor o menor 
            if crimen['DATE OCC'].date() < dato['menor'].date():
                dato['menor'] = crimen['DATE OCC']
            if crimen['DATE OCC'].date() > dato['mayor'].date():
                dato['mayor'] = crimen['DATE OCC']

            
           
            
    lista_areas = [
        {'area_number': area_number,
        'area_name': data['area_name'],
        'count': data['count'],
        'mayor': data['mayor'],
        'menor': data['menor']}
        for area_number, data in areas.items()
    ]
    
    #crear heap a partir del area
    def key_fn(item):
        return (item['count'], ''.join(chr(255 - ord(c)) for c in item['area_name']))
    
    hp.build_heap(lista_areas, key_fn)
    
    top_n = []
    for _ in range(n):  
        top_n.append(hp.heap_pop(lista_areas, key_fn))
        
    tiempo_final = get_time()
    delta_time = tiempo_final - tiempo_inicial
    return top_n, size, delta_time
    

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


def req_7(catalog, n, sexo, edad_inicial, edad_final):
    tiempo_inicial = get_time()
    
    resultados = {}
    
    res = []
    root = catalog['por_edad']['root']
    busqueda_entre_edades(root, edad_inicial, edad_final, res)
    
    for crimen in res:
        if crimen['Vict Sex'] == sexo:
            codigo = crimen['Crm Cd']
            anio = crimen['DATE OCC'].year
            edad = int(crimen['Vict Age'])
            if codigo not in resultados:
                resultados[codigo] = {'total': 0, 'por_edad': {}, 'por_anio': {}}
            resultados[codigo]['total'] += 1
            resultados[codigo]['por_edad'][edad] = resultados[codigo]['por_edad'].get(edad, 0) + 1
            resultados[codigo]['por_anio'][anio] = resultados[codigo]['por_anio'].get(anio, 0) + 1

    lista_resultados = [
        {'codigo': codigo, 
         'total': data['total'], 
         'por_edad': data['por_edad'], 
         'por_anio': data['por_anio']}
        for codigo, data in resultados.items()
    ]
    
    lista_resultados.sort(key=lambda x: (-x['total'], x['codigo']))
    
    tiempo_final = get_time()
    delta_time = tiempo_final - tiempo_inicial
    
    return lista_resultados[:n], delta_time


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
