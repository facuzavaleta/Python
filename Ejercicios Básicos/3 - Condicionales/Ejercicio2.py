key = "contraseña"

contraseña = input("Ingrese con su contraseña: ").lower()

if contraseña == key:
    print("Contraseña correcta, bienvenido.")
else:
    print("Contraseña incorrecta, intentelo nuevamente.")