from random import choice
import string 

listaDePalabras = ["arbol", "baston", "cocina", "derecho", "dulces", "enigma", "faraon", "guerrilla",
                   "hijastro", "invitacion", "jardinero", "kilogramo", "laminas", "miradas", "navidad",
                   "musica", "orquidea", "pasillo", "queso", "rastrillo", "solucion", "tobillo", "unidad", 
                   "vacio", "waterpolo", "xilofono", "yacimiento", "zanja"]

palabraSecreta = choice(listaDePalabras).upper()

def ahorcado():
    letrasPalabra = set(palabraSecreta)
    alfabeto = set(string.ascii_uppercase)
    letrasUsadas = set()
    vidas = 5

    while len(letrasPalabra) > 0 and vidas > 0:
        print ("Tienes", vidas, "vidas y has usado estas letras, ", ', '.join(letrasUsadas))
        palabraLista = [ch if ch in letrasUsadas else '-' for ch in palabraSecreta]
        print("Palabra: ", ", ".join(palabraLista))

        letraUsuario = input("Ingresa una letra: ").upper()
        if letraUsuario in alfabeto - letrasUsadas:
            letrasUsadas.add(letraUsuario)
            if letraUsuario in letrasPalabra:
                letrasPalabra.remove(letraUsuario)
            else:
                vidas -= 1
                print("La letra no esta en la palabra")
        elif letraUsuario in letrasUsadas:
            print("Ya usaste esa letra")
        else:
            print("Caracter invalido")
    if vidas == 0:
        print(f"Te quedaste sin vidas, la palabra era {palabraSecreta}")
    else:
        print(f"Adivinaste la palabra {palabraSecreta}")

ahorcado()