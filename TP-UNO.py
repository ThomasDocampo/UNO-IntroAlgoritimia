import random
import os

'''
Funcion tirar , validar jugada, una funciona para que juegue la compu
'''

mazo = [[1,"ROJO"], [2,"ROJO"], [3,"ROJO"], [3,"ROJO"],[4,"ROJO"],[1,"AZUL"], [2,"AZUL"], [3,"AZUL"], [3,"AZUL"],[4,"AZUL"]] #Otro planteo?

mazoPC = []
mazoUsuario = []
cartaEnJuego = []

#Funcion para repartir las cartas a los jugadores
def repartir(cant,mazo):
     lista = []
     while cant > 0 :
        lista.append(mazo[random.randint(0, len(mazo)-1)])
        cant= cant -1
     return lista

#Funcion para visualizar las cartas del jugador
def mostrarMazo(mazo):
    for i in range(0,len(mazo)):
        carta = mazo[i]
        print(i+1, " -> ", carta[0], carta[1])

#Funcion para validar si una carta es jugable
def validarCarta (cartaEnJuego, cartaUsuario):
      check = False
      if (cartaEnJuego[0] == cartaUsuario[0] or cartaEnJuego[1] == cartaUsuario[1]):
          check = True
      return check

#Funcion turno del usuario
def turnoUsuario (mazoUsuario, mazoGeneral, cartaEnJuego):
    salir = False
    tomoUnaCarta = False
    opcion = -1
    msgOpcion0 = "0  -> Tomar una carta"
    print("es tu turno! Elegí una opcion o carta del mazo para jugar!")
    while salir == False :
      print (msgOpcion0)
      mostrarMazo(mazoUsuario)
      
      opcion = int(input("Elija una opcion:"))
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
              print ("La carta en juego es: ", cartaEnJuego[0],cartaEnJuego[1])
    return cartaEnJuego, mazoUsuario

#Funcion turno de la computadora 
def turnoPC(mazoPC, mazoGeneral, cartaEnJuego):
    print("\nTurno de la computadora...")
    jugada_valida = False
    i = 0

    # Carta jugable
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

    return cartaEnJuego, mazoPC

#Juego
#aca va el menu 
#hay que hacer ranking 

mazoPC = repartir(7,mazo)
mazoUsuario = repartir(7,mazo)
indiceUsuario = 0
cartaEnJuego = repartir(1,mazo)[0]
turno = 0  # 0 = Usuario, 1 = PC

while len(mazoPC) > 0 and len(mazoUsuario) > 0 :
    os.system('cls') #limpiar consola (en windows)
    print ("\nLa cantidad de cartas que tiene la computadora es: ", len(mazoPC))
    print ("\nLa carta en juego es: ", cartaEnJuego[0],cartaEnJuego[1])
    
    if turno == 0:
        cartaEnJuego, mazoUsuario = turnoUsuario(mazoUsuario, mazo, cartaEnJuego)
        turno = 1
    else:
        cartaEnJuego, mazoPC = turnoPC(mazoPC, mazo, cartaEnJuego)
        turno = 0

#Termina Juego
if len(mazoUsuario) == 0:
    print("¡Ganaste!")
else:
    print("¡Ganó la computadora!")
