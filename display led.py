pattern = [[[" ","*"," "],
            [" ","*"," "],
            [" ","*"," "],
            [" ","*"," "],
            [" ","*"," "]],

           [["*","*","*"],
            [" "," ","*"],
            ["*","*","*"],
            ["*"," "," "],
            ["*","*","*"]],

           [["*","*","*"],
            [" "," ","*"],
            ["*","*","*"],
            [" "," ","*"],
            ["*","*","*"]],

           [["*"," ","*"],
            ["*"," ","*"],
            ["*","*","*"],
            [" "," ","*"],
            [" "," ","*"]],

           [["*","*","*"],
            ["*"," "," "],
            ["*","*","*"],
            [" "," ","*"],
            ["*","*","*"]],

           [["*","*","*"],
            ["*"," "," "],
            ["*","*","*"],
            ["*"," ","*"],
            ["*","*","*"]],

           [["*","*","*"],
            [" "," ","*"],
            [" "," ","*"],
            [" "," ","*"],
            [" "," ","*"]],

           [["*","*","*"],
            ["*"," ","*"],
            ["*","*","*"],
            ["*"," ","*"],
            ["*","*","*"]],

           [["*","*","*"],
            ["*"," ","*"],
            ["*","*","*"],
            [" "," ","*"],
            [" "," ","*"]],

           [["*","*","*"],
            ["*"," ","*"],
            ["*"," ","*"],
            ["*"," ","*"],
            ["*","*","*"]]]

def displayLED():
    num = "-1"

    while int(num) < 0:
        num = input("Ingrese un numero entero positivo: ")

        if num.isnumeric() == False:
            num = "-1"

    for x in range(5):
        for digit in num:
            for y in range (3):
                if digit == "1":
                    print(pattern[0][x][y], end="")
                elif digit == "2":
                    print(pattern[1][x][y], end="")
                elif digit == "3":
                    print(pattern[2][x][y], end="")
                elif digit == "4":
                    print(pattern[3][x][y], end="")
                elif digit == "5":
                    print(pattern[4][x][y], end="")
                elif digit == "6":
                    print(pattern[5][x][y], end="")
                elif digit == "7":
                    print(pattern[6][x][y], end="")
                elif digit == "8":
                    print(pattern[7][x][y], end="")
                elif digit == "9":
                    print(pattern[8][x][y], end="")
                else:
                    print(pattern[9][x][y], end="")
            if y == 2:
                print(end=" ")
        print()

displayLED()