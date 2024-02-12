import re
import random

nombre_jugador1=''
nombre_jugador2=''
puntaje_jugador1 = 0
puntaje_jugador2 = 0
juegos_jugador1 = 0
juegos_jugador2 = 0
sets_jugador1 = 0
sets_jugador2 = 0

def verificar_texto_solo_letras(texto_recibido):
    return bool(re.match('^[A-Za-z]+$', texto_recibido))

def solicitar_nombre_jugador(mensaje):
    while True:
        try:
            nombre = input(mensaje)
            if not verificar_texto_solo_letras(nombre):
                raise ValueError("El nombre debe contener solo letras.")
            return nombre
        except ValueError as error:
            print(error)
            print('Intenta nuevamente.')

def solicitar_punto(nombre_jugador1: str, nombre_jugador2: str):
    while True:
        ganador_punto = input(f"¿Quién ganó el punto, {nombre_jugador1.upper()} o {nombre_jugador2.upper()}?: ").lower()
        if ganador_punto in [nombre_jugador1.lower(), nombre_jugador2.lower()]:
            return ganador_punto
        else:
            print("Nombre del jugador invalido, intente nuevamente")




def punto_jugador1(nombre_jugador1: str):
    global puntaje_jugador1, puntaje_jugador2,juegos_jugador1
    game = ""

    if puntaje_jugador1 == 0:
        puntaje_jugador1 = 15
    elif puntaje_jugador1 == 15:
        puntaje_jugador1 = 30
    elif puntaje_jugador1 == 30:
        puntaje_jugador1 = 40
    elif puntaje_jugador1 == 40:
        if puntaje_jugador2 == 40:
            puntaje_jugador1 = "Adv"
        elif puntaje_jugador2 == "Adv":
            puntaje_jugador2 = 40
        else:
            game = f"\033[94mGame para {nombre_jugador1}\033[0m"
            print("-" * 50)
            print(game)
            print("-" * 50)
            juegos_jugador1 += 1
            reiniciar_puntaje()
            sistema_de_sets()
            saque(nombre_jugador1)
    elif puntaje_jugador1 == "Adv":
        game = f"\033[94mGame para {nombre_jugador1}\033[0m"
        print("-" * 50)
        print(game)
        print("-" * 50)
        juegos_jugador1 += 1

        reiniciar_puntaje()
        sistema_de_sets()
        saque(nombre_jugador1)

    if game == "":
        print(f"\033[93m{nombre_jugador1} se lleva el punto\033[0m")
    obtener_puntaje()


def punto_jugador2(nombre_jugador2: str):
    global puntaje_jugador1, puntaje_jugador2,juegos_jugador2
    game = ""

    if puntaje_jugador2 == 0:
        puntaje_jugador2 = 15
    elif puntaje_jugador2 == 15:
        puntaje_jugador2 = 30
    elif puntaje_jugador2 == 30:
        puntaje_jugador2 = 40
    elif puntaje_jugador2 == 40:
        if puntaje_jugador1 == 40:
            puntaje_jugador2 = "Adv"
        elif puntaje_jugador1 == "Adv":
            puntaje_jugador1 = 40
        else:
            game =f"\033[94mGame para {nombre_jugador2}\033[0m"
            print("-" * 50)
            print(game)
            print("-" * 50)
            juegos_jugador2 += 1
            reiniciar_puntaje()
            sistema_de_sets()
            saque(nombre_jugador2)


    elif puntaje_jugador2 == "Adv":

        game = f"\033[94mGame para {nombre_jugador2}\033[0m"
        print("-" * 50)
        print(game)
        print("-" * 50)
        juegos_jugador2 += 1
        reiniciar_puntaje()
        sistema_de_sets()
        saque(nombre_jugador2)

    if game == "":
        print(f"\033[93m{nombre_jugador2} se lleva el punto\033[0m")
    obtener_puntaje()


def reiniciar_puntaje():
    global puntaje_jugador1, puntaje_jugador2
    puntaje_jugador1 = 0
    puntaje_jugador2 = 0

def reiniciar_juegos():
    global juegos_jugador1, juegos_jugador2
    juegos_jugador1 = 0
    juegos_jugador2 = 0

def obtener_puntaje():
    print(f"\033[1mPuntos:\033[0m {puntaje_jugador1}-{puntaje_jugador2}")
    print(f"\033[1mJuegos:\033[0m {juegos_jugador1}-{juegos_jugador2}")
    print(f"\033[1mSets:\033[0m {sets_jugador1}-{sets_jugador2}")

def sistema_de_puntos(ganador_punto:str):
    if ganador_punto.lower() == nombre_jugador1.lower():
        punto_jugador1(nombre_jugador1)

    else:
        punto_jugador2(nombre_jugador2)


def sistema_de_sets():
    global sets_jugador1,sets_jugador2
    if juegos_jugador1 >= 6 and juegos_jugador1 - juegos_jugador2 >= 2:
        print("-" * 50)
        print(f"\033[91mSet para {nombre_jugador1}\033[0m")
        print("-" * 50)
        sets_jugador1 += 1
        reiniciar_juegos()
    elif juegos_jugador2 >= 6 and juegos_jugador2 - juegos_jugador1 >= 2:
        print("-"*50)
        print(f"\033[91mSet para {nombre_jugador2}\033[0m")
        print("-" * 50)
        sets_jugador2 +=1
        reiniciar_juegos()

    cambio_de_cancha()


def saque(ganador_punto:str):
    if ganador_punto.lower() == nombre_jugador1.lower():
        print(f"\033[95mSaque de {nombre_jugador2}\033[0m")
    else:
        print(f"\033[95mSaque de {nombre_jugador1}\033[0m")


def cambio_de_cancha():
    if juegos_jugador1 + juegos_jugador2 % 2 == 1:
        print("-"*100)
        print("\033[92mCAMBIO DE CANCHA\033[0m")
        print("-"*100)
        print("\n")
def fin_del_juego():
    fin = False
    if sets_jugador1 >= 2:
        print("~" * 100)
        print(f"El jugador {nombre_jugador1} ha ganado")
        fin = True
    elif sets_jugador2 >= 2:
        print("~" * 100)
        print(f"El jugador {nombre_jugador2} ha ganado")
        fin = True
    return fin

def juego_tenis():
    global juegos_jugador1, juegos_jugador2,nombre_jugador1,nombre_jugador2
    nombre_jugador1 = solicitar_nombre_jugador("Ingrese el nombre del primer jugador: ")
    nombre_jugador2 = solicitar_nombre_jugador("Ingrese el nombre del segundo jugador: ")

    print(f"INICIO DE JUEGO")
    print(f"\033[95mSaque de {random.choice([nombre_jugador1,nombre_jugador2])}\033[0m")
    while True:
        ganador_punto = solicitar_punto(nombre_jugador1, nombre_jugador2)
        sistema_de_puntos(ganador_punto)
        if fin_del_juego():
            print("FIN DEL JUEGO")
            print("~"*100)
            break







if __name__ == '__main__':
    juego_tenis()


