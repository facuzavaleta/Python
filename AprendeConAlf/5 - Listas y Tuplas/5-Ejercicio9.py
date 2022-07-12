palabra = input("Ingrese una palabra: ").lower()
vocalesAcentuadas = ["á", "é", "í", "ó", "ú"]; vocales = ["a", "e", "i", "o", "u"]
contadorA = 0; contadorE = 0; contadorI = 0; contadorO = 0; contadorU = 0

for char in palabra:
    for i in range(5):
        if char in vocalesAcentuadas:
            palabra = palabra.replace(vocalesAcentuadas[i], vocales[i])
    if char == "a":
        contadorA += 1
    elif char == "e":
        contadorE += 1
    elif char == "i":
        contadorI += 1
    elif char == "o":
        contadorO += 1
    elif char == "u":
        contadorU += 1

print(f"""
La vocal {vocales[0]} aparece {contadorA} veces.
La vocal {vocales[1]} aparece {contadorE} veces.
La vocal {vocales[2]} aparece {contadorI} veces.
La vocal {vocales[3]} aparece {contadorO} veces.
La vocal {vocales[4]} aparece {contadorU} veces.""")

# word = input("Introduce una palabra: ")
# vocals = ['a', 'e', 'i', 'o', 'u']
# for vocal in vocals: 
#     times = 0
#     for letter in word: 
#         if letter == vocal:
#             times += 1
#     print("La vocal " + vocal + " aparece " + str(times) + " veces")