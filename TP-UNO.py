import random

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
        print(i+1, " -> ",mazo[i])
        
def validarCarta (cartaEnJuego, cartaUsuario):
      check = False
      if (cartaEnJuego[0] == cartaUsuario[0] or cartaEnJuego[1] == cartaUsuario[1]):
          check = True
      return check
      
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
    
        
       
           

mostrarMazo("mazoUsuario")
