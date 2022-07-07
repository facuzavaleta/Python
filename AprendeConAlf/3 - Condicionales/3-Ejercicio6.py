nombre = input("Ingrese su nombre: ").lower()
sexo = input("Ingrese M si es masculino o F si es femenino: ").lower()
if nombre < "m" and sexo == "f":
    print ("Grupo A")
elif nombre > "n" and sexo == "m":
    print("Grupo A")
else:
    print("Grupo B")