def med(lista):
    dic = {}
    media = sum(lista) / len(lista)
    varianza = 0
    for num in lista:
        varianza += (num - media) ** 2
    varianza /= 5

    dic["Media"] = media

    dic["Varianza"] = varianza

    dic["Desv. Tipica"] = round(varianza ** 0.5)

    return dic

print(med([1500, 1200, 1700, 1300, 1800]))