nombre = input("Ingrese su nombre: ")
sexo = input("Ingrese su sexo (m) o (f): ")

if sexo == "f" and nombre < "m" or sexo == "m" and nombre > "n":
    print("Perteneces al Grupo A.")
else:
    print("Perteneces al Grupo B.")