persona = {}
continuar = True
while continuar:
    clave  = input("Que dato quiere ingresar?: ")
    valor = input(f"{clave}: ")
    persona[clave] = valor
    print(persona)
    continuar = input("Desea añadir mas informacion? (Si/No): ") == "Si"