# diccionarioStr = ""
# diccionario = {}
# palabra = ""

# while palabra != "salir":
#     palabra = input("Ingrese las palabras en español e inglés separadas por dos puntos, y cada par <palabra>:<traducción> separados por comas, o ingrese <salir> para salir: ")
#     if palabra != "salir":
#         diccionarioStr += palabra

# diccionarioList = diccionarioStr.split(", ")

# for item in diccionarioList:
#     itemList = item.split(":")
#     diccionario[itemList[0]] = itemList[1]

# frase = input("Ingrese una frase: ")
# fraseList = frase.split(" ")

# for word in fraseList:
#     if word in diccionario:
#         fraseR = frase.replace(word, diccionario[word])

# print(fraseR)

diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
    clave, valor = i.split(':')
    diccionario[clave] = valor
frase = input('Introduce una frase en español: ')
for i in frase.split():
    if i in diccionario:
        print(diccionario[i], end=' ')
    else:
        print(i, end=' ')