txt = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".lower()

for char in txt:
    if char == "," or char == ".":
        txt = txt.replace(char, "")

lista = txt.split(" ")
caracteres = {}

for elem in lista:
    for char in elem:
        if char in caracteres:
            caracteres[char] += 1
        else:
            caracteres[char] = 1

frec_max = max(caracteres.values())
pos_max = list(caracteres.values()).index(frec_max)
caracter_max = list(caracteres.keys())[pos_max]

palabras = {}

for i in lista:
    if caracter_max in i and not i in palabras:
        freq = 0
        for j in i:
            if j == caracter_max:
                freq += 1
        palabras[i] = freq

print(caracteres)
print(f"Caracter mas repetido: {caracter_max}: {frec_max}")
print(palabras)