from math import sin, cos, tan, exp, log

def apply_function(f, n):
    
    functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
    result = {}
    for i in range(1, n+1):
        result[i] = functions[f](i)
    return result

def calculator():

    f = input('Introduce la función a aplicar (sin, cos, tan, exp, log): ')
    n = int(input('Introduce un entero positivo: '))
    for i, j in apply_function(f, n).items():
        print (i, '\t', j)
    return

calculator()