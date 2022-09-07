def contador(frase):
    fraseNueva = ""
    for char in frase:
        if char.isalnum() or char.isspace():
            fraseNueva += char
    fraseNueva = fraseNueva.split(" ")

    for elem in fraseNueva:
        if elem == '':
            fraseNueva.remove(elem)
    for elem in fraseNueva:
        if elem == '':
            fraseNueva.remove(elem)
    for elem in fraseNueva:
        if elem == '':
            fraseNueva.remove(elem)
    for elem in fraseNueva:
        if elem == '':
            fraseNueva.remove(elem)
    for elem in fraseNueva:
        if elem == '':
            fraseNueva.remove(elem)

    return fraseNueva

print(contador("hola que tal?. ,  , ,, , , ,    , , ,        como le va?"))