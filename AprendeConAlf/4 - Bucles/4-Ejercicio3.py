num = int(input("Ingrese un número entero positivo: "))
listaNums = [i for i in range(1, num+1)]

if num % 2 == 0:
    ultimoNum = listaNums[-2]
    for i in range((len(listaNums) - 2)):
        if i % 2 != 0:
            print(i, end=", ")
    print(str(ultimoNum) + ".")

elif num % 2 != 0:
    ultimoNum = listaNums[-1]
    for i in range((len(listaNums) - 1)):
        if i % 2 != 0:
            print(i, end=", ")
    print(str(ultimoNum) + ".")
