def Contraseña():
    global contraseña
    contraseña = input("Defina su contraseña: ")
    confirmacion = input("Confirme su contraseña: ")
    while contraseña != confirmacion:
        confirmacion = input("Error. Confirme su contraseña: ")
        if contraseña == confirmacion:
            break

def Intento():
    intento = input("Ingrese su contraseña: ")
    while intento != contraseña:
        intento = input("Contraseña erronea. Ingrese nuevamente su contraseña: ")
        if intento == contraseña:
            break
    
    print("Contraseña correcta, bienvenido.")
    cambio = input("Para cambiar nuevamente de contraseña, ingrese [Y]: ").lower()
    if cambio == "y":
        Contraseña()
        Intento()

Contraseña()

Intento()