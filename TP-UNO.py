import random

'''
Funcion tirar , validar jugada, una funciona para que juegue la compu

'''
mazo = [[1,"ROJO"], [2,"ROJO"], [3,"ROJO"], [3,"ROJO"],[4,"ROJO"],[1,"AZUL"], [2,"AZUL"], [3,"AZUL"], [3,"AZUL"],[4,"AZUL"]] #Otro planteo?

mazoPC = []
mazoUsuario = []
#Funcion para repartir las cartas a los jugadores
def repartir(cant,mazo):
     lista = []
     while cant > 0 :
        lista.append(mazo[random.randint(0, len(mazo)-1)])
        cant= cant -1
     return lista

#Funcion para visualizar las cartas del jugador
def mostrarMazo(msg, mazo):
    print(msg)
    for i in range(0,len(mazo)):
        print(i+1, " -> ",mazo[i])

#Programa principal
mazoPC = repartir(7,mazo)
mazoUsuario = repartir(7,mazo)
mostrarMazo("El mazo de la pc es: ",mazoPC)

mostrarMazo("Tu mazo es: ",mazoUsuario)


