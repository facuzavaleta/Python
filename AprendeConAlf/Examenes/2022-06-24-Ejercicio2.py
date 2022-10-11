tablero = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def muestra_tablero():
    for linea in tablero:
        print(linea)

def ocupada(x, y):
    if tablero[x - 1][y - 1] != " ":
        print(f"La casilla [{x}, {y}] esta ocupada.")
        return True
    else:
        return False

def jugada():

    x1 = int(input("Jugador 1, ingrese la coordenada x del 1 al 3: "))
    y1 = int(input("Jugador 1, ingrese la coordenada x del 1 al 3: "))

    while ocupada(x1, y1):
        x1 = int(input("Jugador 1, ingrese la coordenada x del 1 al 3: "))
        y1 = int(input("Jugador 1, ingrese la coordenada x del 1 al 3: "))

    tablero[x1 - 1][y1 - 1] = "X"
    muestra_tablero()

    winner()

    x2 = int(input("Jugador 2, ingrese la coordenada x del 1 al 3: "))
    y2 = int(input("Jugador 2, ingrese la coordenada x del 1 al 3: "))

    while ocupada(x2, y2):
        x2 = int(input("Jugador 2, ingrese la coordenada x del 1 al 3: "))
        y2 = int(input("Jugador 2, ingrese la coordenada x del 1 al 3: "))

    tablero[x2 - 1][y2 - 1] = "0"
    muestra_tablero()
    
def winner():
    if tablero[0][0] == "X" and tablero[0][1] == "X" and tablero[0][2] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[1][0] == "X" and tablero[1][1] == "X" and tablero[1][2] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[2][0] == "X" and tablero[2][1] == "X" and tablero[2][2] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[0][0] == "X" and tablero[1][0] == "X" and tablero[2][0] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[0][1] == "X" and tablero[1][1] == "X" and tablero[2][1] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[0][2] == "X" and tablero[1][2] == "X" and tablero[2][2] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[0][0] == "X" and tablero[1][1] == "X" and tablero[2][2] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[2][0] == "X" and tablero[1][1] == "X" and tablero[0][2] == "X":
        print("Gana Jugador 1")
        exit()
    elif tablero[0][0] == "0" and tablero[0][1] == "0" and tablero[0][2] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[1][0] == "0" and tablero[1][1] == "0" and tablero[1][2] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[2][0] == "0" and tablero[2][1] == "0" and tablero[2][2] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[0][0] == "0" and tablero[1][0] == "0" and tablero[2][0] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[0][1] == "0" and tablero[1][1] == "0" and tablero[2][1] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[0][2] == "0" and tablero[1][2] == "0" and tablero[2][2] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[0][0] == "0" and tablero[1][1] == "0" and tablero[2][2] == "0":
        print("Gana Jugador 2")
        exit()
    elif tablero[2][0] == "0" and tablero[1][1] == "0" and tablero[0][2] == "0":
        print("Gana Jugador 2")
        exit()
    else:
        return False

def main():
    
    enter = input("""
---------------------------------------------------------------------------------
|BIENVENIDOS AL JUEGO DE TA-TE-TI, EL JUGADOR 1 SERA 'X' Y EL JUGADOR 2 SERA '0'|
|                         PRESIONE ENTER PARA COMENZAR                          |
---------------------------------------------------------------------------------
""")
    muestra_tablero()
    while winner() == False:
        jugada()

main()