frutas = {"platano":1.35, "manzana":0.8, "pera":0.85, "naranja":0.7}

user = input("Ingrese una fruta: ")
kilos = float(input("Ingrese la cantidad de kilos: "))


if user in frutas:
    print(f"El precio es de {frutas[user] * kilos}")
else:
    print("La fruta no esta en el diccionario.")