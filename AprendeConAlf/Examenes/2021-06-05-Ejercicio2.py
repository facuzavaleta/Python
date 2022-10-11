respuesta = ""
while respuesta != "salir":
    respuesta = input("Introduce la operación con el formato operando1 operador operando2: ")
    listaRespuesta = respuesta.split(" ")
    a = int(listaRespuesta[0])
    b = int(listaRespuesta[2])
    if respuesta == "salir":
        break

    elif listaRespuesta[1] == "+":
        print(f"{a} + {b} = {a + b}")

    elif listaRespuesta[1] == "-":
        print(f"{a} - {b} = {a - b}")

    elif listaRespuesta[1] == "*":
        print(f"{a} * {b} = {a * b}")

    elif listaRespuesta[1] == "/":
        print(f"{a} / {b} = {a / b}")

    elif listaRespuesta[1] == "**":
        print(f"{a} ** {b} = {a ** b}")
