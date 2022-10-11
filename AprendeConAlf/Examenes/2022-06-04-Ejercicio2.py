def main():
    opcion = 0
    saldo = 0
    lista = []
    listaIngresos = []
    listaReintegros = []
    while opcion != 4:
        opcion = int(input("\n¿Que deseas hacer?\n1 - Ingreso\n2 - Reintegro\n3 - Ver saldo\n4 - Salir\n-> "))
        if opcion == 1:
            cantidad = float(input("Ingrese la cantidad: "))
            saldo += cantidad
            lista.append(cantidad)
            print(f"${cantidad} han sido ingresados correctamente, su saldo es de ${saldo}.")
        elif opcion == 2:
            cantidad = float(input("Ingrese la cantidad: "))
            if cantidad > saldo:
                print("Saldo insuficiente.")
            else:
                saldo -= cantidad
                lista.append(-cantidad)
                print(f"${cantidad} han sido extraidos correctamente, su saldo es de ${saldo}.")
        elif opcion == 3:
            print(f"Su saldo es de ${saldo}")

    for i in lista:
        if i >= 0:
            listaIngresos.append(i)
        else:
            listaReintegros.append(i)

    print(f"Ingresos: {listaIngresos}")
    print(f"Reintegros: {listaReintegros}")

main()