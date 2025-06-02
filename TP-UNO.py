import random
import msvcrt  # Solo funciona en Windows

'''
Funcion tirar , validar jugada, una funciona para que juegue la compu
'''

mazo = [[1,"ROJO"], [2,"ROJO"], [3,"ROJO"], [3,"ROJO"],[4,"ROJO"],[1,"AZUL"], [2,"AZUL"], [3,"AZUL"], [3,"AZUL"],[4,"AZUL"]] 

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
        print(i+1, " -> ",mazo[i])
        
def validarCarta (cartaEnJuego, cartaUsuario):
      check = False
      if (cartaEnJuego[0] == cartaUsuario[0] or cartaEnJuego[1] == cartaUsuario[1]):
          check = True
      return check

# Nueva función para seleccionar carta con flechas y Enter
def seleccionar_con_flechas(mazo, msgOpcion0):
    indice = 0
    while True:
        print("\n" * 50)  # limpiar pantalla básica
        print("Usa ← y → para elegir carta. ENTER para jugarla.")
        print(msgOpcion0)
        mostrarMazo(mazo)
        # Mostrar selección con flecha
        print(f"\nSeleccionada -> {indice+1} -> {mazo[indice]}")
        print("0 -> Tomar carta / Pasar turno")

        tecla = msvcrt.getch()
        if tecla == b'\xe0':  # tecla especial (flechas)
            flecha = msvcrt.getch()
            if flecha == b'K':  # flecha izquierda
                indice = (indice - 1) % len(mazo)
            elif flecha == b'M':  # flecha derecha
                indice = (indice + 1) % len(mazo)
        elif tecla == b'\r':  # Enter
            return indice + 1  # para que coincida con input anterior (1-based)
        elif tecla == b'0':  # presionar 0 para tomar carta o pasar
            return 0

# Modificamos sólo turnoUsuario para usar seleccionar_con_flechas en lugar de input
def turnoUsuario (mazoUsuario, mazoGeneral, cartaEnJuego):
    salir = False
    tomoUnaCarta = False
    msgOpcion0 = "0  -> Tomar una carta"
    print("es tu turno! Elegí una opcion o carta del mazo para jugar!")
    while salir == False :
      print (msgOpcion0)
      mostrarMazo(mazoUsuario)
      
      opcion = seleccionar_con_flechas(mazoUsuario, msgOpcion0)
      
      if opcion < 0 or opcion > len(mazoUsuario)+1:
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
              print("no es una carta valida amiguin")
              print ("la carta en juego es: ", cartaEnJuego)
          
    return cartaEnJuego, mazoUsuario

#Programa principal

mazoPC = repartir(7,mazo)
mazoUsuario = repartir(7,mazo)
indiceUsuario = 0
cartaEnJuego = repartir(1,mazo)[0]

while len(mazoPC) > 0 and len(mazoUsuario) > 0 :
    print ("la carta en juego es: ", cartaEnJuego)
    cartaEnJuego, mazoUsuario= turnoUsuario(mazoUsuario,mazo,cartaEnJuego)
    
mostrarMazo(mazoUsuario)
