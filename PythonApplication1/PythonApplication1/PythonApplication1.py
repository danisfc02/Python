import random 

nameP1 =input("Inserte el nombre del jugador 1")
nameP2 =input("Inserte el nombre del jugador 2")
nameP3 =input("Inserte el nombre del jugador 3")

puntosP1 = 121
puntosP2 = 121
puntosP3 = 121

numGame = 1


while (puntosP1 > 0 and puntosP2 > 0 and puntosP3 > 0):

    print("Partida numero ", numGame)

    num1P1 = random.randrange(1,50)
    num2P1 = random.randrange(1,50)
    num3P1 = random.randrange(1,50)
    sumaP1 = num1P1 + num2P1 + num3P1
    puntosP1 = puntosP1 - sumaP1


    print("El jugador " , nameP1,"ha sacado" , num1P1, ",", num2P1, "y", num3P1)
    print("Al jugador " , nameP1,"le quedan", puntosP1, "puntos para ganar")
    

    num1P2 = random.randrange(1,50)
    num2P2 = random.randrange(1,50)
    num3P2 = random.randrange(1,50)
    sumaP2 = num1P2 + num2P2 + num3P2
    puntosP2 = puntosP2 - sumaP2

    print("El jugador " , nameP2,"ha sacado" , num1P2, ",", num2P2, "y", num3P2)
    print("Al jugador " , nameP2,"le quedan", puntosP2, "puntos para ganar")


    num1P3 = random.randrange(1,50)
    num2P3 = random.randrange(1,50)
    num3P3 = random.randrange(1,50)
    sumaP3 = num1P3 + num2P3 + num3P3
    puntosP3 = puntosP3 - sumaP3

    print("El jugador " , nameP3,"ha sacado" , num1P3, ",", num2P3, "y", num3P3)
    print("Al jugador " , nameP3,"le quedan", puntosP3, "puntos para ganar")

    if puntosP1 <= 0:
        print("El jugador " , nameP1,"ha ganado en la ronda",numGame)

    if puntosP2 <= 0:
        print("El jugador " , nameP2,"ha ganado en la ronda",numGame)

    if puntosP3 <= 0:
        print("El jugador " , nameP3,"ha ganado en la ronda",numGame)
    
    numGame = numGame + 1

    if (numGame == 4):
        print("Ningún jugador ha ganado")
    

if(puntosP1 <= 0 or puntosP2 <= 0 or puntosP3 <= 0):
    print("Juego terminado")
   
    
    
    

