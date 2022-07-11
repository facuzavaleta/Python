import random

PuntosJugador1 = 0; gamesJugador1 = 0; SetsJugador1 = 0
PuntosJugador2 = 0; gamesJugador2 = 0; SetsJugador2 = 0
punto = 0

def point():
    global punto
    enter = input("Presione enter para anotar un punto al azar (o escriba el número del jugador para anotar el punto manualmente): ")
    
    if enter == "1":
        punto = 1
    elif enter == "2":
        punto = 2
    else:
        punto = random.randint(1, 2)

    return punto

def tieBreak():
    print("Tie Break!")
    marcador()
    flag = True
    global punto, PuntosJugador1, PuntosJugador2, gamesJugador1, gamesJugador2, SetsJugador1, SetsJugador2

    while flag == True:

        if PuntosJugador1 >= 7 and PuntosJugador1 >= PuntosJugador2 + 2:
                print("game y Set Jugador 1!")
                SetsJugador1 += 1
                resetGames()
                flag = False
                marcador()

        elif PuntosJugador2 >= 7 and PuntosJugador2 >= PuntosJugador1 + 2:
                print("game y Set Jugador 2!")
                SetsJugador2 += 1
                resetGames()
                flag = False
                marcador()
        else:
            point()

            if punto == 1:
                print("\nPunto Jugador 1!")
                PuntosJugador1 += 1
                marcador()

            if punto == 2:
                print("\nPunto Jugador 2!")
                PuntosJugador2 += 1
                marcador()

def resetPoints():
    global PuntosJugador1, PuntosJugador2
    PuntosJugador1 = PuntosJugador2 = 0

def resetGames():
    global gamesJugador1, gamesJugador2
    gamesJugador1 = gamesJugador2 = 0
    resetPoints()

def resetSets():
    global SetsJugador1, SetsJugador2
    SetsJugador1 = SetsJugador2 = 0
    resetGames()

def winner():
    global SetsJugador1, SetsJugador2

    if SetsJugador1 > 2:
        print(f"\nGana Jugador 1 {SetsJugador1} a {SetsJugador2}!")
        nuevoJuego = input("\nDesea jugar nuevamente: [y] o [n]: ")

        if nuevoJuego == "y":
            resetSets()
            game()
        else:
            exit()

    elif SetsJugador2 > 2:
        print(f"\nGana Jugador 2! {SetsJugador2} a {SetsJugador1}")
        nuevoJuego = input("Desea jugar nuevamente: [y] o [n]")

        if nuevoJuego == "y":
            resetSets()
            game()
        else:
            exit()

    else:
        return False
    
def marcador():
    print(f"""
==============================
|| Marcador:
|| Jugador 1: {PuntosJugador1} | G:{gamesJugador1} | S:{SetsJugador1}
|| Jugador 2: {PuntosJugador2} | G:{gamesJugador2} | S:{SetsJugador2}
==============================\n""")

def game():
    global punto, PuntosJugador1, PuntosJugador2, gamesJugador1, gamesJugador2, SetsJugador1, SetsJugador2

    start = input(f"""
                            =======================================================
                            || Simulador de puntuación para Tennis - Paddle      ||
                            ||         Presione Enter para comenzar              ||
                            =======================================================
    """)
    marcador()

    while True:

        if gamesJugador1 == 7 or (gamesJugador1 == 6 and gamesJugador2 < 5):
            SetsJugador1 += 1
            print("Set Jugador 1!")
            resetGames()
            marcador()
        elif gamesJugador2 == 7 or (gamesJugador2 == 6 and gamesJugador1 < 5):
            SetsJugador2 += 1
            print("Set Jugador 2!")
            resetGames()
            marcador()
        elif gamesJugador1 == 6 and gamesJugador2 == 6:
            tieBreak()
        
        if winner() == False:
            point()

            if punto == 1:

                if PuntosJugador1 == 40 and PuntosJugador2 == "Adv":
                    print("\nPunto Jugador 1!")
                    PuntosJugador2 = 40
                    marcador()
                elif PuntosJugador1 == 40 and PuntosJugador2 == 40:
                    print("\nVentaja Jugador 1!")
                    PuntosJugador1 = "Adv"
                    marcador()
                elif PuntosJugador1 == "Adv":
                    print ("\nPunto Jugador 1! Game jugador 1")
                    gamesJugador1 += 1    
                    resetPoints()            
                    marcador()            
                elif PuntosJugador1 == 40 and PuntosJugador2 < 40:
                    print ("\nPunto Jugador 1! Game jugador 1")
                    gamesJugador1 += 1
                    resetPoints()
                    marcador()
                elif PuntosJugador1 == 0 or PuntosJugador1 == 15:
                    print("\nPunto jugador 1!")
                    PuntosJugador1 += 15
                    marcador()
                elif PuntosJugador1 == 30:
                    print("\nPunto jugador 1!")
                    PuntosJugador1 += 10
                    marcador()
                
            elif punto == 2:

                if PuntosJugador2 == 40 and PuntosJugador1 == "Adv":
                    print("\nPunto Jugador 2!")
                    PuntosJugador1 = 40
                    marcador()
                elif PuntosJugador2 == 40 and PuntosJugador1 == 40:
                    print("\nVentaja Jugador 2!")
                    PuntosJugador2 = "Adv"
                    marcador()
                elif PuntosJugador2 == "Adv":
                    print ("\nPunto Jugador 2! Game jugador 2")
                    gamesJugador2 += 1
                    resetPoints()
                    marcador()         
                elif PuntosJugador2 == 40 and PuntosJugador1 < 40:
                    print ("\nPunto Jugador 2! Game jugador 2")
                    gamesJugador2 += 1
                    resetPoints()
                    marcador()
                elif PuntosJugador2 == 0 or PuntosJugador2 == 15:
                    print("\nPunto jugador 2!")
                    PuntosJugador2 += 15
                    marcador()
                elif PuntosJugador2 == 30:
                    print("\nPunto jugador 2!")
                    PuntosJugador2 += 10
                    marcador()

game()