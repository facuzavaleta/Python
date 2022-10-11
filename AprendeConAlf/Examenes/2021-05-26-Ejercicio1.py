x = [1, 2, 3, 4, 5, 6]
y = [20, 18, 12, 10, 9, 9]

def media(lista):
    
    return sum(lista) / len(lista)
    

def varianza(lista):
    varianza = 0
    medi = media(lista)
    for num in lista:
        varianza += (num - medi) ** 2
    
    return varianza / len(lista)

print(varianza(x))