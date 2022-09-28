notaParcial1 = int(input("Ingrese la nota obtenida en su primer parcial: "))
notaParcial2 = int(input("Ingrese la nota obtenida en su segundo parcial: "))
media = (notaParcial1 + notaParcial2) / 2

if notaParcial1 < 4 and notaParcial2 < 4:
    print("Desaprobado, debe repetir los 2 parciales.")
elif notaParcial1 < 4 and notaParcial2 >= 4:
    print("Desaprobado, debe repetir el primer parcial.")
elif notaParcial2 < 4 and notaParcial1 >= 4:
    print("Desaprobado, debe repetir el segundo parcial.")
else:
    print(f"Aprobado con {media}.")