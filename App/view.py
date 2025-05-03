import sys
from App import logic
from tabulate import tabulate
from datetime import datetime
import pprint as pprint


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Ejecutar Rango de fechas")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8 (Bono)")
    print("0- Salir")

def load_data(control):
    """
    Carga los datos
    """
    catalog, primeros, ultimos, delta = logic.load_data(control)
    return catalog, primeros, ultimos, delta

def print_rango_fechas(control):
    """
    Imprime el rango de fechas cargadas en el catálogo
    """
    fecha_min, fecha_max = logic.rango_fechas_catalogo(control)
    print("\nFechas cargadas en el catálogo:")
    print(f"Desde: {fecha_min} Hasta: {fecha_max}")

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
    Función que imprime la solución del Requerimiento 1 en consola
    """
    fecha_inicial = input('Ingrese la fecha inicial (YYYY-MM-DD): ')
    fecha_final = input('Ingrese la fecha final (YYYY-MM-DD): ')
    
    res, delta = logic.req_1(control, fecha_inicial, fecha_final)

    headers = ['DR_NO', 'DATE OCC', 'TIME OCC', 'AREA NAME', 'Crm Cd', 'LOCATION']
    
    rows = []
    for crimen in res:
        fila = [
            crimen['DR_NO'],
            crimen['DATE OCC'].strftime("%Y-%m-%d"),
            crimen['TIME OCC'],
            crimen['AREA NAME'],
            crimen['Crm Cd'],
            crimen['LOCATION']
        ]
        rows.append(fila)

    print("\nTotal registros encontrados:", len(res))
    print("\nRegistros encontrados:")
    if len(rows) > 10:
        rows_to_show = rows[:5] + rows[-5:]
    else:
        rows_to_show = rows
    print(tabulate(rows_to_show, headers=headers, tablefmt="pipe"))
    print(f"\nTiempo de ejecución: {delta} ms")




def print_req_2(control):
    
    fecha_inicial = input('Ingrese la fecha inicial (YYYY-MM-DD): ')
    fecha_final = input('Ingrese la fecha final (YYYY-MM-DD): ')

    res, tiempo = logic.req_2(control,fecha_inicial,fecha_final)

    headers = ['DR_NO', 'DATE OCC', 'TIME OCC', 'AREA','AREA NAME', 'Part 1-2','Crm Cd', 'Status']
    primeros = res[:5]
    ultimos = res[-5:]
    
    def format_row(d, headers):
        row = []
        for h in headers:
            val = d.get(h, '')
            if isinstance(val, datetime):
                val = val.strftime('%Y-%m-%d')
            row.append(val)
        return row

    rows = [format_row(d, headers) for d in primeros]
    rows2 = [format_row(d, headers) for d in ultimos]


    print('\nTiempo de ejcución' + str(tiempo))
    print("\nPrimeros 5 registros:")
        
    print(tabulate(rows, headers=headers, tablefmt="pipe"))

    print("\nÚltimos 5 registros:")
    print(tabulate(rows2, headers=headers, tablefmt="pipe"))



def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    area = input('Ingrese el area que quiere consultar: ')
    n = int(input('Ingrese el n que quiere consultar: '))
    res, size, delta = logic.req_3(control, n, area)
    
    print(f"\nTiempo de ejecución (ms): {delta:.2f}")
    
    headers = ['DR_NO', 'Date Rptd', 'TIME OCC', 'AREA NAME', 'Rpt Dist No', 'Part 1-2', 'Crm Cd', 'Status', 'LOCATION']
    rows = [[d[h] for h in headers] for d in res]

    print('\nTotal registros en el area: ' + str(size))
    
    print("\n N registros:")
    print(tabulate(rows, headers=headers, tablefmt="pipe"))
    


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    edad_inicial = int(input('ingrese la edad incial: '))
    edad_final = int(input('ingrese la edad final: '))
    numero_datos = int(input('Ingrese el número de datos que desea consultar:'))
    res, size,time = logic.req_4(control,numero_datos,edad_inicial,edad_final)
    
    headers = ['DR_NO', 'Date Rptd', 'TIME OCC','AREA', 'AREA NAME', 'Part 1-2', 'Crm Cd','Vict Age', 'Status', 'LOCATION']
    rows = [[d[h] for h in headers] for d in res]

    print('\n Tiempo de ejecución: ' + str(time))
    print('\nTotal registros que cumplen el filtro de edad ' + str(size))
    print(tabulate(rows, headers=headers, tablefmt="pipe"))

   

def print_req_5(control):
    """
    Función que imprime la solución del Requerimiento 5 en consola
    """
    fecha_inicial = input('Ingrese la fecha inicial (YYYY-MM-DD): ')
    fecha_final = input('Ingrese la fecha final (YYYY-MM-DD): ')
    n = int(input('Ingrese el número de áreas a consultar: '))

    res, size, delta = logic.req_5(control, n, fecha_inicial, fecha_final)

    headers = ['area_number', 'area_name', 'count', 'menor', 'mayor']
    rows = []
    for area in res:
        fila = [
            area['area_number'],
            area['area_name'],
            area['count'],
            area['menor'].strftime("%Y-%m-%d"),
            area['mayor'].strftime("%Y-%m-%d")
        ]
        rows.append(fila)

    print("\nTotal de incidentes resueltos IC:", size)
    print("\nÁreas con más incidentes:")
    print(tabulate(rows, headers=headers, tablefmt="pipe"))
    print(f"\nTiempo de ejecución: {delta} ms")

    

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    n = int(input('Ingrese el número de áreas a consultar: '))
    sexo = input('Ingrese el sexo consultar: ')
    mes = int(input('Ingrese el mes a consultar: '))
    
    res, delta = logic.req_6(control, n, sexo, mes)


    formatted_data = [
        (id_, name, value, ', '.join([f'{year}: {count}' for year, count in years.items()]))
        for id_, name, value, years in res
    ]

    headers = ['ID', 'Area', 'Crimenes', 'Por año']
    print(tabulate(formatted_data, headers=headers, tablefmt='grid'))
    print(f"\nTiempo de ejecución: {delta} ms")





def print_req_7(control):
    """
    Función que imprime la solución del Requerimiento 7 en consola
    """
    n = int(input('Ingrese la cantidad de crímenes: '))
    sexo = input('Ingrese el sexo de la víctima (M/F/X): ')
    edad_inicial = int(input('Ingrese edad mínima: '))
    edad_final = int(input('Ingrese edad máxima: '))

    res, delta = logic.req_7(control, n, sexo, edad_inicial, edad_final)

    headers = ['Código', 'Total Crímenes', 'Por Edad', 'Por Año']
    rows = []
    for crimen in res:
        fila = [
            crimen['codigo'],
            crimen['total'],
            crimen['por_edad'],
            crimen['por_anio']
        ]
        rows.append(fila)

    print("\nCrímenes encontrados:")
    print(tabulate(rows, headers=headers, tablefmt="pipe"))
    print(f"\nTiempo de ejecución: {delta} ms")



def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    n = int(input('Ingrese la cantidad de crímenes: '))
    tipo = (input('Ingrese el tipo: '))
    area = (input('Ingrese el area de partida: '))
    primeros, ultimos, delta = logic.req_8(control, area, n, tipo)
    print('N crimenes más cercanos: ')
    table_data = [
        (round(score, 2), area, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"), code)
        for score, area, start, end, code in primeros]
    table_data2 = [
        (round(score, 2), area, start.strftime("%Y-%m-%d"), end.strftime("%Y-%m-%d"), code)
        for score, area, start, end, code in ultimos]

    headers = ["Distancia", "Area", "Fecha Crimen 1", "Fecha Crimen 2", "Tipo"]

    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))
    print('')
    print('')
    print('N crimenes más lejanos: ')
    print(tabulate(table_data2, headers=headers, tablefmt="fancy_grid"))
    
    print(f"\nTiempo de ejecución: {delta} ms")

    


# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print_rango_fechas(control)

        if int(inputs) == 1:
            print("Cargando información de los archivos ....\n")
            catalog, primeros, ultimos, delta = load_data(control)
            #print(catalog['por_fecha_ocurrido'])
            
            print(f"\nTiempo de ejecución de la carga de datos: {delta:.3f} ms")
            
            headers = ['DR_NO', 'Date Rptd', 'DATE OCC', 'AREA NAME', 'Crm Cd']
            rows = [[d[h] for h in headers] for d in primeros]
            rows2 = [[d[h] for h in headers] for d in ultimos]

            size = len(catalog['registros']['elements'])
            print('\nTotal registros cargados: ' + str(size))
            
            print("\nPrimeros 5 registros:")
            print(tabulate(rows, headers=headers, tablefmt="pipe"))
            print("\nUltimos 5 registros:")
            print(tabulate(rows2, headers=headers, tablefmt="pipe"))


        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print_req_4(control)

        elif int(inputs) == 6:
            print_req_5(control)

        elif int(inputs) == 7:
            print_req_6(control)

        elif int(inputs) == 8:
            print_req_7(control)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
