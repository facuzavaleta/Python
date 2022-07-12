numList = []
numeros = int(input("Ingrese la cantidad de numeros que desea ingresar como ganadores: "))

for i in range(numeros):
    num = int(input("Ingrese el numero ganador: "))
    numList.append(num)

numList.sort()

print("Los numeros ganadores de la loteria son: ", end="")

for i in range(numeros - 1):
    print(f"{numList[i]}", end=", ")

print(f"{numList[-1]}.")