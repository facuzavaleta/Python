# Declaro las variables y las listas
palabra = input("Ingrese una palabra o frase: ").lower(); palabraNueva = ""
abc = [letter for letter in "abcdefghijklmnñrstuvwyz"]
vocalesAcentuadas = ["á", "é", "í", "ó", "ú"]; vocales = ["a", "e", "i", "o", "u"]

# Por cada caracter de la palabra
for char in palabra:
    # De 0 a 4
    for i in range(len(vocales)):
        # Si el caracter esta en vocalesAcentuadas
        if char in vocalesAcentuadas:
            # Reemplazarlo por su caracter no acentuado
            palabra = palabra.replace(vocalesAcentuadas[i], vocales[i])
    # Si el caracter esta en el abecedario en minusculas
    if char in abc:
        # Sumarlo a palabraNueva
        palabraNueva += char

# # Por cada caracter en palabra
# for char in palabra:
#     # Si el caracter esta en el abecedario en minusculas
#     if char in abc:
#         # Sumarlo a palabraNueva
#         palabraNueva += char

def esPalindromo(palabra):
    # Imprimo la palabra, y su inversion (como control)  
    print(palabra, palabra[::-1])
    # Si son iguales:
    if palabra == palabra[::-1]:
        return True
    else:
        return False

if esPalindromo(palabraNueva):
    print("Es palindromo.")
else:
    print("No es palindromo.")