nivel = float(input("Ingrese su nivel de rendimiento (0.0, 0.4, 0.6 o +0.6): "))
if nivel == 0.0:
    print("Su nivel de rendimiento es Inaceptable y recibirá una bonificación de $", 2400 * nivel, sep="")
elif nivel == 0.4:
    print("Su nivel de rendimiento es Aceptable y recibirá una bonificación de $", 2400 * nivel, sep="")
elif nivel >= 0.6:
    print("Su nivel de rendimiento es Meritorio y recibirá una bonificación de $", 2400 * nivel, sep="")