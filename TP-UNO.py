import random

'''
Funcion tirar , validar jugada, 

'''

mazo = ["1 ROJO", "2 ROJO", "3 ROJO", "4 ROJO","5 ROJO"] #Otro planteo?


mazoPC = []
mazoUsuario = []

def repartir(cant,mazo):
     lista = []
     while cant > 0 :
        lista.append(mazo[random.randint(0, len(mazo)-1)])
        cant= cant -1
     return lista
    
def mostrarMazo(msg, mazo) :
    print(msg)
    for i in range(0,len(mazo)) :
        print(i+1, " -> ",mazo[i])

#Programa principal
#While para manejar los turnos
    
        
mazoPC = repartir(7,mazo)
mazoUsuario = repartir(7,mazo)
mostrarMazo("el mazo de la pc es",mazoPC)


mostrarMazo("tu mazo es",mazoUsuario)


