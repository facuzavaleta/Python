clientes = {}
while True:
    cadena = input("\nIngrese la cadena o escriba [salir] para salir: ")

    if cadena == "salir":
        break

    datos = cadena.split("\\n")
    datos1 = datos[0].split(";")

    for elem in datos:
        elem = elem.split(";")
        
        for i in range(len(datos)):
            clientes[elem[0]] = {datos1[1]:elem[1], datos1[2]:elem[2], datos1[3]:elem[3], datos1[4]:elem[4]}
    
    del clientes["nif"]

print("\n", clientes)