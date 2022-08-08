print("\nBienvenidos al gestor de base de datos de la empresa.")
opcion = ""
clientes = {}
prefBool = False
contraseña = "abc123"
while opcion != "6":
    opcion = input("\n(1) Añadir cliente\n(2) Eliminar cliente\n(3) Mostrar cliente\n(4) Listar todos los clientes\n(5) Listar clientes preferentes\n(6) Terminar\n-> ")

    if opcion == "1":
        nif = input("\nIngrese el NIF: ")
        nombre = input("Ingrese su nombre completo: ")
        direccion = input("Ingrese su direccion: ")
        telefono = input("Ingrese su telefono: ")
        correo = input("Ingrese su correo: ")
        preferente = input("Es cliente preferente (si/no): ").lower()
        if preferente == "si":
            prefBool = True
        elif preferente == "no":
            prefBool = False
        
        clientes[nif] = {"Nombre":nombre, "Direccion":direccion, "Telefono":telefono, "Correo":correo, "Preferente":prefBool}
    
    elif opcion == "2":
        check = input("\nIngrese la contraseña: ")

        if check == contraseña:
            nif = input("\nIngrese el NIF: ")

            if nif in clientes:
                print(f"\nEl cliente {nif} - {clientes[nif]['Nombre']} ha sido eliminado con exito.")
                del clientes[nif]
            else:
                print("\nNIF inexistente.")
        else:
            print("\nContraseña inválida")
        
    elif opcion == "3":
        nif = input("\nIngrese el NIF: ")

        if nif in clientes:
            print("\nNIF:", nif)
            for clave, valor in clientes[nif].items():
                print(clave + ":", valor)
        else:
            print("\nNIF inexistente.")
    
    elif opcion == "4":
        print()
        for cliente in clientes:
            print(f"""{cliente} - {clientes[cliente]["Nombre"]}""")

    elif opcion == "5":
        print()
        for cliente in clientes:
            if clientes[cliente]["Preferente"] == True:
                print(f"""{cliente} - {clientes[cliente]["Nombre"]}""")