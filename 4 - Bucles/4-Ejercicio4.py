num = int(input("Ingrese un numero entero positivo: "))
numList = [i for i in range(1, num + 1)]; numList.reverse()
for i in numList:
    print(i, end=", ")
print("0.")