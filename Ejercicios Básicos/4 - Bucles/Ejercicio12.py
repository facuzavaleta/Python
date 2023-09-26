frase = input("Ingrese una frase: ")
letra = input("Ingrese una letra para ver cuantas veces esta en la frase: ")
contador = 0

for i in frase:
    if letra == i:
        contador += 1

print(f"La letra {letra} se encuentra {contador} veces en la frase.")