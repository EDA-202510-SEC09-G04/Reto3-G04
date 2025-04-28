import sys
from App import logic
from tabulate import tabulate
from datetime import datetime


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
    catalog, primeros, ultimos = logic.load_data(control)
    return catalog, primeros, ultimos

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
    
    res = logic.req_1(control, fecha_inicial, fecha_final)

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
    print("\nPrimeros 5 registros:")
    print(tabulate(rows[:5], headers=headers, tablefmt="pipe"))
    print("\nÚltimos 5 registros:")
    print(tabulate(rows[-5:], headers=headers, tablefmt="pipe"))



def print_req_2(control):
    
    fecha_inicial = input('Ingrese la fecha inicial (YYYY-MM-DD): ')
    fecha_final = input('Ingrese la fecha final (YYYY-MM-DD): ')

    res, tiempo = logic.req_2(control,fecha_inicial,fecha_final)

    headers = ['DR_NO', 'DATE OCC', 'TIME OCC', 'AREA','AREA NAME', 'Part 1-2','Crm Cd', 'Status']
    
    print('\nTiempo de ejcución' + str(tiempo))
    print("\nPrimeros 5 registros:")
    print(res[:5])
    print("\nÚltimos 5 registros:")
    print(res[-5:])



def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    area = input('Ingrese el area que quiere consultar: ')
    n = int(input('Ingrese el n que quiere consultar: '))
    res, size = logic.req_3(control, n, area)
    
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
    
    headers = ['DR_NO', 'Date Rptd', 'TIME OCC','AREA', 'AREA NAME', 'Part 1-2', 'Crm Cd', 'Status', 'LOCATION']
    rows = [[d[h] for h in headers] for d in res]

    print('\n Tiempo de ejecución: ' + str(time))
    print('\nTotal registros que cumplen el filtro de edad' + str(size))
    print(tabulate(rows, headers=headers, tablefmt="pipe"))

   

def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    n = int(input('Ingrese el n que quiere consultar: '))
    inicial = input('Ingrese la fecha inicial en formato yy-mm-dd: ')
    final = input('Ingrese la fecha final en formato yy-mm-dd: ')

    res, size = logic.req_5(control, n, inicial, final)
    
    print('\nTotal crimenes no resueltos entre el rango de fechas: ' + str(size))
    
    headers = ['area_number', 'area_name', 'count', 'mayor', 'menor']
    rows = [[d[h] for h in headers] for d in res]
    
    print("\n N registros:")
    print(tabulate(rows, headers=headers, tablefmt="pipe"))
    

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(control):
    n = int(input('Ingrese el número N de crímenes más comunes a calcular: '))
    sexo = input('Ingrese el sexo de la víctima (M/F): ')
    edad_inicial = int(input('Ingrese la edad inicial: '))
    edad_final = int(input('Ingrese la edad final: '))
    
    resultados = logic.req_7(control, n, sexo, edad_inicial, edad_final)
    
    for crimen in resultados:
        print(f"Código del crimen: {crimen['codigo']}")
        print(f"Cantidad de crímenes cometidos: {crimen['total']}")
        print("Cantidad de crímenes por edad:")
        for edad, cantidad in crimen['por_edad'].items():
            print(f"  Edad {edad}: {cantidad}")
        print("Cantidad de crímenes por año:")
        for anio, cantidad in crimen['por_anio'].items():
            print(f"  Año {anio}: {cantidad}")
        print("-" * 40)


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


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
            catalog, primeros, ultimos = load_data(control)
            #print(catalog['por_fecha_ocurrido'])
            
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
