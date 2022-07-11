import random

PuntosJugador1 = 0; GamesJugador1 = 0; SetsJugador1 = 0
PuntosJugador2 = 0; GamesJugador2 = 0; SetsJugador2 = 0
punto = 0

def Point():
    global punto
    enter = input("Presione enter para anotar un punto al azar (o escriba el número del jugador para anotar el punto manualmente): ")
    
    if enter == "1":
        punto = 1
    elif enter == "2":
        punto = 2
    else:
        punto = random.randint(1, 2)

    return punto

def TieBreak():
    print("Tie Break!")
    Marcador()
    flag = True
    global punto, PuntosJugador1, PuntosJugador2, GamesJugador1, GamesJugador2, SetsJugador1, SetsJugador2

    while flag == True:

        if PuntosJugador1 >= 7 and PuntosJugador1 >= PuntosJugador2 + 2:
                print("Game y Set Jugador 1!")
                SetsJugador1 += 1
                ResetGames()
                flag = False
                Marcador()

        elif PuntosJugador2 >= 7 and PuntosJugador2 >= PuntosJugador1 + 2:
                print("Game y Set Jugador 2!")
                SetsJugador2 += 1
                ResetGames()
                flag = False
                Marcador()
        else:
            Point()

            if punto == 1:
                print("\nPunto Jugador 1!")
                PuntosJugador1 += 1
                Marcador()

            if punto == 2:
                print("\nPunto Jugador 2!")
                PuntosJugador2 += 1
                Marcador()

def ResetPoints():
    global PuntosJugador1, PuntosJugador2
    PuntosJugador1 = PuntosJugador2 = 0

def ResetGames():
    global GamesJugador1, GamesJugador2
    GamesJugador1 = GamesJugador2 = 0
    ResetPoints()

def ResetSets():
    global SetsJugador1, SetsJugador2
    SetsJugador1 = SetsJugador2 = 0
    ResetGames()

def Winner():
    global SetsJugador1, SetsJugador2

    if SetsJugador1 > 2:
        print(f"\nGana Jugador 1 {SetsJugador1} a {SetsJugador2}!")
        nuevoJuego = input("\nDesea jugar nuevamente: [y] o [n]: ")

        if nuevoJuego == "y":
            ResetSets()
            Game()
        else:
            exit()

    elif SetsJugador2 > 2:
        print(f"\nGana Jugador 2! {SetsJugador2} a {SetsJugador1}")
        nuevoJuego = input("Desea jugar nuevamente: [y] o [n]")

        if nuevoJuego == "y":
            ResetSets()
            Game()
        else:
            exit()

    else:
        return False
    
def Marcador():
    print(f"""
==============================
|| Marcador:
|| Jugador 1: {PuntosJugador1} | G:{GamesJugador1} | S:{SetsJugador1}
|| Jugador 2: {PuntosJugador2} | G:{GamesJugador2} | S:{SetsJugador2}
==============================\n""")

def Game():
    global punto, PuntosJugador1, PuntosJugador2, GamesJugador1, GamesJugador2, SetsJugador1, SetsJugador2

    start = input(f"""
                            =======================================================
                            || Simulador de puntuación para Tennis - Paddle      ||
                            ||         Presione Enter para comenzar              ||
                            =======================================================
    """)

    while True:

        if GamesJugador1 == 7 or (GamesJugador1 == 6 and GamesJugador2 < 5):
            SetsJugador1 += 1
            print("Set Jugador 1!")
            ResetGames()
            Marcador()
        elif GamesJugador2 == 7 or (GamesJugador2 == 6 and GamesJugador1 < 5):
            SetsJugador2 += 1
            print("Set Jugador 2!")
            ResetGames()
            Marcador()
        elif GamesJugador1 == 6 and GamesJugador2 == 6:
            TieBreak()
        
        if Winner() == False:
            Point()

            if punto == 1:

                if PuntosJugador1 == 40 and PuntosJugador2 == "Adv":
                    print("\nPunto Jugador 1!")
                    PuntosJugador2 = 40
                    Marcador()
                elif PuntosJugador1 == 40 and PuntosJugador2 == 40:
                    print("\nVentaja Jugador 1!")
                    PuntosJugador1 = "Adv"
                    Marcador()
                elif PuntosJugador1 == "Adv":
                    print ("\nPunto Jugador 1! Game jugador 1")
                    GamesJugador1 += 1    
                    ResetPoints()            
                    Marcador()            
                elif PuntosJugador1 == 40 and PuntosJugador2 < 40:
                    print ("\nPunto Jugador 1! Game jugador 1")
                    GamesJugador1 += 1
                    ResetPoints()
                    Marcador()
                elif PuntosJugador1 == 0 or PuntosJugador1 == 15:
                    print("\nPunto jugador 1!")
                    PuntosJugador1 += 15
                    Marcador()
                elif PuntosJugador1 == 30:
                    print("\nPunto jugador 1!")
                    PuntosJugador1 += 10
                    Marcador()
                
            elif punto == 2:

                if PuntosJugador2 == 40 and PuntosJugador1 == "Adv":
                    print("\nPunto Jugador 2!")
                    PuntosJugador1 = 40
                    Marcador()
                elif PuntosJugador2 == 40 and PuntosJugador1 == 40:
                    print("\nVentaja Jugador 2!")
                    PuntosJugador2 = "Adv"
                    Marcador()
                elif PuntosJugador2 == "Adv":
                    print ("\nPunto Jugador 2! Game jugador 2")
                    GamesJugador2 += 1
                    ResetPoints()
                    Marcador()         
                elif PuntosJugador2 == 40 and PuntosJugador1 < 40:
                    print ("\nPunto Jugador 2! Game jugador 2")
                    GamesJugador2 += 1
                    ResetPoints()
                    Marcador()
                elif PuntosJugador2 == 0 or PuntosJugador2 == 15:
                    print("\nPunto jugador 2!")
                    PuntosJugador2 += 15
                    Marcador()
                elif PuntosJugador2 == 30:
                    print("\nPunto jugador 2!")
                    PuntosJugador2 += 10
                    Marcador()

Game()