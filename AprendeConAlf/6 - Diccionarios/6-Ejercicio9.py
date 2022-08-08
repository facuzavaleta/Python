facturas={}
respuesta = ""
pagada = 0
pendiente = 0
print("\nBienvenidos al gestor de facturas pendientes de la empresa.")

while respuesta != "t":
    respuesta = input("Desea [A]-Añadir una nueva factura, [P]-Pagar una existente, o [T]-Terminar: ").lower()

    if respuesta == "a":
        num = input("Ingrese el numero de la factura: ")
        coste = float(input("Ingrese el coste: "))
        facturas[num] = coste
        pendiente += coste
        print(f"Pendiente: ${round(pendiente, 2)} - Pagada: ${round(pagada, 2)}")

    elif respuesta == "p":
        num = input("Ingrese el numero de la factura: ")
        if num in facturas:
            pagada += facturas[num]
            pendiente -= facturas[num]
            del facturas[num]
            print(f"Pendiente: ${round(pendiente, 2)} - Pagada: ${round(pagada, 2)}")
        else:
            print("Numero de factura inexistente.")

print(f"Pendiente: ${round(pendiente, 2)} - Pagada: ${round(pagada, 2)}")