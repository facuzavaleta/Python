def alCuadrado(num):
    return num ** 2

def raizCuadrada(num):
    return num ** 0.5

def aplica(funcion, lista):
    resultados = []
    for elem in lista:
        resultados.append(round(funcion(elem), 2))
    return resultados

print(aplica(raizCuadrada, [10, 25, 50, 75, 100]))