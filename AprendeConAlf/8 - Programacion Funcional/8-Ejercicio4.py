def esPar(num):
    if num % 2 == 0:
        return True

def aplica(funcion, lista):
    resultado = []
    for elem in lista:
        if funcion(elem):
            resultado.append(elem)
    return resultado

print(aplica(esPar, [1, 2, 3, 4, 5, 6]))