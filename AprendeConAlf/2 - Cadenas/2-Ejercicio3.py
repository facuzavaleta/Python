nombre = input("Ingrese su nombre completo: ")
cantidadLetras = len(nombre)
for letter in nombre:
    if letter == " ":
        cantidadLetras -= 1
print(nombre.upper() + " tiene " + str(cantidadLetras) + " letras.")