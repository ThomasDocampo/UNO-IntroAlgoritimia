import random
import os
import msvcrt  # Para captura de teclas en Windows
from colorama import init, Fore, Style
init(autoreset=True)

mazo = [[1,"ROJO"], [2,"ROJO"], [3,"ROJO"],[4,"ROJO"],[5,"ROJO"],[6,"ROJO"],[7,"ROJO"],[8,"ROJO"],[9,"ROJO"],[0,"ROJO"], ["+2","ROJO"], ["BLOQUEO", "ROJO"],
        [1,"AZUL"], [2,"AZUL"], [3,"AZUL"],[4,"AZUL"],[5,"AZUL"],[6,"AZUL"],[7,"AZUL"],[8,"AZUL"],[9,"AZUL"],[0,"AZUL"], ["+2","AZUL"], ["BLOQUEO", "AZUL"],
        [1,"VERDE"], [2,"VERDE"], [3,"VERDE"],[4,"VERDE"],[5,"VERDE"],[6,"VERDE"],[7,"VERDE"],[8,"VERDE"],[9,"VERDE"],[0,"VERDE"], ["+2","VERDE"], ["BLOQUEO", "VERDE"],
        [1,"AMARILLO"], [2,"AMARILLO"], [3,"AMARILLO"],[4,"AMARILLO"],[5,"AMARILLO"],[6,"AMARILLO"],[7,"AMARILLO"],[8,"AMARILLO"],[9,"AMARILLO"],[0,"AMARILLO"], ["+2","AMARILLO"], ["BLOQUEO", "AMARILLO"]]

mazoPC = []
mazoUsuario = []
cartaEnJuego = []

jugadores = [
    ["bruno", 70],
    ["mar", 65],
    ["vicky", 55],
    ["thomas", 50],
    ["vera", 45],
    ["lu", 30]
]

def repartir(cant,mazo):
     lista = []
     while cant > 0 :
        lista.append(mazo[random.randint(0, len(mazo)-1)])
        cant= cant -1
     return lista

def mostrarMazo(mazo):
    for i in range(len(mazo)):
        carta = mazo[i]
        numero, color = carta
        if color == "ROJO":
            color_print = Fore.RED
        elif color == "AZUL":
            color_print = Fore.BLUE
        elif color == "VERDE":
            color_print = Fore.GREEN
        elif color == "AMARILLO":
            color_print = Fore.YELLOW
        else:
            color_print = Style.RESET_ALL
        
        print(f"{i+1} -> {color_print}{numero} {color}{Style.RESET_ALL}")

def validarCarta(cartaEnJuego, cartaUsuario):
    check = False
    if cartaEnJuego[0] == cartaUsuario[0] or cartaEnJuego[1] == cartaUsuario[1]:
        check = True
    elif (cartaUsuario[0] in ["+2", "BLOQUEO"]) and cartaEnJuego[1] == cartaUsuario[1]:
        check = True
    return check


# Nueva función para selección con flechas
def seleccionar_con_flechas(mazo, msgOpcion0, cartaEnJuego):
    indice = 0
    while True:
        os.system('cls')
        numero, color = cartaEnJuego
        if color == "ROJO":
            color_print = Fore.RED
        elif color == "AZUL":
            color_print = Fore.BLUE
        elif color == "VERDE":
            color_print = Fore.GREEN
        elif color == "AMARILLO":
            color_print = Fore.YELLOW
        else:
            color_print = Style.RESET_ALL
        
        print(f"\nLa carta en juego es: {color_print}{numero} {color}{Style.RESET_ALL}")
        print(msgOpcion0)
        print("0  -> Tomar carta / Pasar turno\n")
        for i in range(len(mazo)):
            prefijo = "->" if i == indice else "  "
            print(f"{prefijo} {i+1} -> {mazo[i][0]} {mazo[i][1]}")
        tecla = msvcrt.getch()
        if tecla == b'\xe0':  # Flechas
            flecha = msvcrt.getch()
            if flecha == b'K':  # Izquierda
                indice = (indice - 1) % len(mazo)
            elif flecha == b'M':  # Derecha
                indice = (indice + 1) % len(mazo)
        elif tecla == b'\r':  # Enter
            return indice + 1
        elif tecla == b'0':
            return 0

def turnoUsuario (mazoUsuario, mazoGeneral, cartaEnJuego):
    salir = False
    tomoUnaCarta = False
    opcion = -1
    msgOpcion0 = "0  -> Tomar una carta"
    print("es tu turno! Elegí una opcion o carta del mazo para jugar!")
    while salir == False :
      opcion = seleccionar_con_flechas(mazoUsuario, msgOpcion0, cartaEnJuego)
      if opcion < 0 or opcion > len(mazoUsuario):
           print ("opcion no valida!")
      elif opcion == 0 and tomoUnaCarta == False:
          print ( "el usuario toma una carta" )
          mazoUsuario = mazoUsuario + repartir(1,mazoGeneral)
          tomoUnaCarta = True
          msgOpcion0 = "0  -> Pasar turno"
      elif opcion == 0 and tomoUnaCarta == True :
          salir = True
          opcion = -1
      else :
          opcion = opcion-1
          if(validarCarta(cartaEnJuego, mazoUsuario[opcion])):
              cartaEnJuego = mazoUsuario[opcion]
              del mazoUsuario[opcion]
              salir = True
          else:
              print("No es una carta valida.")
              numero, color = cartaEnJuego
              if color == "ROJO":
                  color_print = Fore.RED
              elif color == "AZUL":
                  color_print = Fore.BLUE
              elif color == "VERDE":
                    color_print = Fore.GREEN
              elif color == "AMARILLO":
                  color_print = Fore.YELLOW
              else:
                color_print = Style.RESET_ALL

                print(f"\nLa carta en juego es: {color_print}{numero} {color}{Style.RESET_ALL}")
    return cartaEnJuego, mazoUsuario

def turnoPC(mazoPC, mazoGeneral, cartaEnJuego):
    print("\nTurno de la computadora...")
    jugada_valida = False
    i = 0

    while i < len(mazoPC) and not jugada_valida:
        if validarCarta(cartaEnJuego, mazoPC[i]):
            cartaEnJuego = mazoPC[i]
            print("La computadora jugó: ", cartaEnJuego[0],cartaEnJuego[1])
            del mazoPC[i]
            jugada_valida = True
        else:
            i += 1

    if jugada_valida==False:
        print("La computadora no tiene cartas válidas. Toma una carta...")
        nueva_carta = repartir(1, mazoGeneral)[0]
       
        if validarCarta(cartaEnJuego, nueva_carta):
            cartaEnJuego = nueva_carta
            print("¡La computadora jugó la carta que tomó! ", cartaEnJuego[0],cartaEnJuego[1])
        else:
            mazoPC.append(nueva_carta)
            print("La computadora no pudo jugar. Pasa el turno.")

    input("\nPresione Enter para continuar...")
    return cartaEnJuego, mazoPC

def registrar_usuario():
    print("\n=== REGISTRO DE USUARIO ===")
    nombre = input("Ingrese su nombre: ")
    while len(nombre.strip()) == 0:
        print("El nombre no puede estar vacío")
        nombre = input("Ingrese su nombre: ")
    return nombre

def reglas():
    print("\n=== REGLAS DEL UNO ===")
    print("1. Cada jugador recibe 7 cartas al inicio")
    print("2. Se juega por turnos")
    print("3. Se puede jugar una carta si coincide con el número o color de la carta en juego")
    print("4. Si no tenes una carta válida, tenes que tomar una carta del mazo")
    print("5. La carta de bloqueo le roba el turno al jugador contrincante")
    print("6. La carta +2 indica que el jugador contrincante deberá tomar dos cartas del mazo y perderá el turno")
    print("7. El primer jugador que se quede sin cartas gana")
    input("\nPresione Enter para continuar...")

def ranking():
    print("\n=== RANKING DE JUGADORES ===")
    ranking_ordenado = []
    for jugador in jugadores:
        ranking_ordenado.append(jugador)
    
    # Ordenar la lista usando el método burbuja
    for i in range(len(ranking_ordenado)):
        for j in range(len(ranking_ordenado)-1):
            if ranking_ordenado[j][1] < ranking_ordenado[j+1][1]:
                temp = ranking_ordenado[j]
                ranking_ordenado[j] = ranking_ordenado[j+1]
                ranking_ordenado[j+1] = temp
    
    # Mostrar el ranking
    for i in range(len(ranking_ordenado)):
        print(f"{i+1}. {ranking_ordenado[i][0]}: {ranking_ordenado[i][1]} puntos")
    
    input("\nPresione Enter para continuar...")

def actualizar_puntuacion(nombre, puntos):
    for i in range(len(jugadores)):
        if jugadores[i][0].lower() == nombre.lower():
            jugadores[i][1] += puntos
            return
    jugadores.append([nombre.lower(), puntos])

def menu():
    while True:
        os.system('cls')
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Iniciar partida")
        print("2. Reglas del juego")
        print("3. Ranking de jugadores")
        print("4. Salir del juego")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            return True
        elif opcion == "2":
            reglas()
        elif opcion == "3":
            ranking()
        elif opcion == "4":
            print("\n¡Gracias por jugar!")
            return False
        else:
            print("\nOpción no válida")
            input("Presione Enter para continuar...")

def iniciar_juego():
    nombre_usuario = registrar_usuario()
    print(f"\n¡Bienvenido {nombre_usuario}!")
    input("Presione Enter para continuar...")
    
    while menu():
        mazoPC = repartir(7, mazo)
        mazoUsuario = repartir(7, mazo)
        cartaEnJuego = repartir(1, mazo)[0]
        turno = 0  # 0 = Usuario, 1 = PC
        efecto_pendiente = None  # Para controlar el efecto de +2 o BLOQUEO

        while len(mazoPC) > 0 and len(mazoUsuario) > 0:
            os.system('cls')
            print(f"\nJugador: {nombre_usuario}")
            print("\nLa cantidad de cartas que tiene la computadora es: ", len(mazoPC))
            numero, color = cartaEnJuego
            if color == "ROJO":
                color_print = Fore.RED
            elif color == "AZUL":
                color_print = Fore.BLUE
            elif color == "VERDE":
                color_print = Fore.GREEN
            elif color == "AMARILLO":
                color_print = Fore.YELLOW
            else:
                color_print = Style.RESET_ALL

            print(f"\nLa carta en juego es: {color_print}{numero} {color}{Style.RESET_ALL}")


            # Aplicar efecto pendiente, si lo hay, y saltar turno
            if efecto_pendiente == "MAS2":
                if turno == 0:
                    print("¡Efecto +2! El jugador toma 2 cartas y pierde el turno.")
                    mazoUsuario += repartir(2, mazo)
                    turno = 1
                else:
                    print("¡Efecto +2! La computadora toma 2 cartas y pierde el turno.")
                    mazoPC += repartir(2, mazo)
                    turno = 0
                efecto_pendiente = None
                input("\nPresione Enter para continuar...")
                continue

            elif efecto_pendiente == "BLOQUEO":
                if turno == 0:
                    print("¡BLOQUEO! El jugador pierde el turno.")
                    turno = 1
                else:
                    print("¡BLOQUEO! La computadora pierde el turno.")
                    turno = 0
                efecto_pendiente = None
                input("\nPresione Enter para continuar...")
                continue

            # Turnos normales
            if turno == 0:
                cartaEnJuego, mazoUsuario = turnoUsuario(mazoUsuario, mazo, cartaEnJuego)
                # Detectar si la carta jugada es +2 o BLOQUEO para activar efecto
                if cartaEnJuego[0] == "+2":
                    efecto_pendiente = "MAS2"
                elif cartaEnJuego[0] == "BLOQUEO":
                    efecto_pendiente = "BLOQUEO"
                turno = 1

            else:
                cartaEnJuego, mazoPC = turnoPC(mazoPC, mazo, cartaEnJuego)
                # Detectar si la carta jugada es +2 o BLOQUEO para activar efecto
                if cartaEnJuego[0] == "+2":
                    efecto_pendiente = "MAS2"
                elif cartaEnJuego[0] == "BLOQUEO":
                    efecto_pendiente = "BLOQUEO"
                turno = 0

        # Final del juego
        if len(mazoUsuario) == 0:
            print("¡Ganaste!")
            actualizar_puntuacion(nombre_usuario, 15)
        else:
            print("¡Ganó la computadora!")
            actualizar_puntuacion(nombre_usuario, -5)
        
        input("\nPresione Enter para continuar...")

iniciar_juego()

