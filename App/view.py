import sys
from App import logic
from tabulate import tabulate


def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
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
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


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
    # TODO: Imprimir el resultado del requerimiento 4
    pass


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
    """
        Función que imprime la solución del Requerimiento 7 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 7
    pass


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
