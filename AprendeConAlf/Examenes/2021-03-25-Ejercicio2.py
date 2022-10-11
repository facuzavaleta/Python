import random

juan = [7, 13, 21, 37, 46, 49]; numeros = [x + 1 for x in range(49)]; ganadores = []; fallos = []

manualoauto = input("Desea ingresar los numeros ganadores manualmente [m] o aleatoriamente [a]: ")

if manualoauto == "m":
    while len(ganadores) <= 5:
        num = int(input("Ingrese un numero: "))
        while num in ganadores or num < 1 or num > 49:
            num = int(input("El numero ingresado ya esta en la lista, es inferior a 1, o superior a 49, ingrese otro: "))
        if not num in juan:
            fallos.append(num)
        ganadores.append(num)
        
elif manualoauto == "a":
    while len(ganadores) <= 5:
        num = random.choice(numeros)
        while num in ganadores or num < 1 or num > 49:
            num = random.choice(numeros)
        if not num in juan:
            fallos.append(num)
        ganadores.append(num)

if len(fallos) == 0:
    print("Juan gano.")
else:
    print(f"Juan perdio. Los numeros ganadores son {ganadores}, no acertaste los siguientes numeros: {fallos}")