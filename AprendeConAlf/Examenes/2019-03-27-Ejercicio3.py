palabra = input("Ingrese la palabra a adivinar: ")
listaLetras = list(palabra);letrasAcertadas = []; fallos = 5

while fallos >= 1:
    letra = input("Ingrese una letra: ")

    if letra in letrasAcertadas:
        print("Ya acertaste esa letra.")

    elif letra in listaLetras:
        letrasAcertadas.append(letra)
        listaLetras.remove(letra)
        print(f"Acierto. Letras acertadas: {letrasAcertadas}")

        if len(listaLetras) == 0:
            print(f"Ganaste, la palabra es {palabra}.")
            exit()

    else:
        fallos -= 1
        print(f"Fallo, te quedan {fallos} intentos.")
        
print("Perdiste")
    