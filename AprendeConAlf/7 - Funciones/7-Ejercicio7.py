def cuadrados(lista):
    squares = []
    for num in lista:
        squares.append(num**2)
    return(squares)

print(cuadrados([2, 3, 4, 5]))
