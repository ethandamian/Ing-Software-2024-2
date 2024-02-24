import time
from model import Usuarios_model
from model import Peliculas_model
from model import Rentar_model


def menu_principal():
    print("BIENVENIDO, ELIJA UNA OPCIÓN")
    print("1. Ver registros de una tabla")
    print("2. Buscar un registro por id ")
    print("3. Actualizar un registro (solo nombre o fecha de renta para la tabla rentas)")
    print("4. Eliminar un registro (o todos los registros de una tabla)")
    print("5. Salir")


def menu_tablas():
    print("-"*100)
    print("ELIJA UNA TABLA")
    print("1. Usuarios")
    print("2. Películas")
    print("3. Rentas")
    print("4. Regresar al menú principal")




def pedir_id():
    return "Introduzca el id del registro que desea buscar: "

def pedir_id_por_nombre():
    return "Introduzca el id del registro que desea cambiarle el nombre: "

def pedir_id_a_eliminar():
    return "Introduzca el id del registro que desea eliminar: "

def pedir_nombre_a_buscar():
    return "Introduzca el nombre del registro que desea buscar: "

def pedir_fecha_a_buscar():
    return "Introduzca la fecha de renta que desea buscar (en formato aaa-mm-dd): "


def eliminar_registros():
    print("-"*100)
    print("ELIJA UNA OPCIÓN DE ELIMINACIÓN")
    print("1. Eliminar un registro")
    print("2. Eliminar todos los registros de la tabla")
    print("3. Cancelar y regresar al menú principal")


def salir_menu_principal():
    # imprime "Saliendo al menu principal..." con color azul
    print("-"*100)
    print("\033[94m"+"Saliendo al menu principal..."+"\033[0m")
    print("-"*100)
    time.sleep(1)

def opcion_no_valida():
    print("-"*100)
    print("\033[91m"+"Opción no válida, intente de nuevo"+"\033[0m")
    print("-"*100)

def salir():
    print("Saliendo...")
    time.sleep(1)

def confirma_accion():
    print("¿Está seguro de que desea realizar esta acción? (s/n)")

def imprimir_peticion(lista):
    for i in lista:
        print(i)



def menu():
    while True:
        menu_principal()
        try:
            opcion = int(input("Introduzca el número de la opción que desea: "))
            if opcion == 1:
                menu_tablas()
                opcion_tabla = int(input("Introduzca el número de la tabla que desea: "))
                if opcion_tabla == 1:
                    imprimir_peticion(Usuarios_model.obtener_usuarios())
                elif opcion_tabla == 2:
                    imprimir_peticion(Peliculas_model.obtener_peliculas())
                elif opcion_tabla == 3:
                    imprimir_peticion(Rentar_model.obtener_rentas())
                elif opcion_tabla == 4:
                    salir_menu_principal()
                    continue
                else:
                    opcion_no_valida()
            elif opcion == 2:
                menu_tablas()
                opcion_tabla = int(input("Introduzca el número de la tabla que desea: "))
                if opcion_tabla == 1:
                    id = int(input(pedir_id()))
                    print(Usuarios_model.obtener_usuario_por_id(id))
                    print("-"*100)
                elif opcion_tabla == 2:
                    id = int(input(pedir_id()))
                    print(Peliculas_model.obtener_pelicula_por_id(id))
                    print("-"*100)
                elif opcion_tabla == 3:
                    id = int(input(pedir_id()))
                    print(Rentar_model.obtener_renta_por_id(id))
                    print("-"*100)
                elif opcion_tabla == 4:
                    salir_menu_principal()
                    continue
                else:
                    opcion_no_valida()
            elif opcion == 3:
                menu_tablas()
                opcion_tabla = int(input("Introduzca el número de la tabla que desea: "))
                if opcion_tabla == 1:
                    nombre = input(pedir_nombre_a_buscar())
                    imprimir_peticion(Usuarios_model.obtener_usuario_por_nombre(nombre))
                    id = int(input(pedir_id_por_nombre()))
                    nombre = input("Introduzca el nuevo nombre: ")
                    Usuarios_model.actualizar_nombre_usuario(nombre, id)
                elif opcion_tabla == 2:
                    nombre = input(pedir_nombre_a_buscar())
                    imprimir_peticion(Peliculas_model.obtener_pelicula_por_nombre(nombre))
                    id = int(input(pedir_id_por_nombre()))
                    nombre = input("Introduzca el nuevo nombre: ")
                    Peliculas_model.actualizar_nombre_pelicula(nombre, id)
                elif opcion_tabla == 3:
                    fecha = input(pedir_fecha_a_buscar())
                    imprimir_peticion(Rentar_model.obtener_fecha_renta(fecha))
                    id = int(input(pedir_id()))
                    fecha = input("Introduzca la nueva fecha de renta (en formato aaa-mm-dd): ")
                    Rentar_model.actualizar_fecha_renta(fecha, id)
                elif opcion_tabla == 4:
                    salir_menu_principal()
                    continue
                else:
                    opcion_no_valida()
            elif opcion == 4:
                menu_tablas()
                opcion_tabla = int(input("Introduzca el número de la tabla que desea: "))
                eliminar_registros()
                opcion_eliminar = int(input("Introduzca el número de la opción que desea: "))
                if opcion_eliminar == 1:
                    if opcion_tabla == 1:
                        id = int(input(pedir_id_a_eliminar()))
                        
                        confirmacion = input(confirma_accion())
                        if confirmacion == "s":
                            Usuarios_model.eliminar_usuario_por_id(id)
                        else:
                            print("Acción cancelada")
                    elif opcion_tabla == 2:
                        id = int(input(pedir_id_a_eliminar()))
                        
                        confirmacion = input(confirma_accion())
                        if confirmacion == "s":
                            Peliculas_model.eliminar_pelicula_por_id(id)
                        else:
                            print("Acción cancelada")
                    elif opcion_tabla == 3:
                        id = int(input(pedir_id_a_eliminar()))
                        
                        confirmacion = input(confirma_accion())
                        if confirmacion == "s":
                            Rentar_model.eliminar_renta_por_id(id)
                        else:
                            print("Acción cancelada")
                    elif opcion_tabla == 4:
                        salir_menu_principal()
                        continue
                    else:
                        opcion_no_valida()
                elif opcion_eliminar == 2:
                    if opcion_tabla == 1:
                        confirmacion = input(confirma_accion())
                        if confirmacion == "s":
                            Usuarios_model.borrar_tabla_usuarios()
                        else:
                            print("Acción cancelada")
                    elif opcion_tabla == 2:
                        
                        confirmacion = input(confirma_accion())
                        if confirmacion == "s":
                            Peliculas_model.borrar_tabla_peliculas()
                        else:
                            print("Acción cancelada")
                    elif opcion_tabla == 3:
                        
                        confirmacion = input(confirma_accion())
                        if confirmacion == "s":
                            Rentar_model.borrar_tabla_rentas()
                        else:
                            print("Acción cancelada")
                    elif opcion_tabla == 4:
                        salir_menu_principal()
                        continue
                    else:
                        opcion_no_valida()
                elif opcion_eliminar == 3:
                    salir_menu_principal()
                    continue
                else:
                    opcion_no_valida()
            elif opcion == 5:
                salir()
                break
            else:
                opcion_no_valida()
        except ValueError:
            opcion_no_valida()


