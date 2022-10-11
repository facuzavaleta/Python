def ordenador(lista):
    pares = []
    impares = []

    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()

    return f"Pares: {pares}\nImpares: {impares}"

print(ordenador([4, 6, 8, 4, 1, 3424, 2543, 776, 45435, 625, 2, 324, 54]))