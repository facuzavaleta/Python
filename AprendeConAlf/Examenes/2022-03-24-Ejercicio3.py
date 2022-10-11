# Número de filas
nfil = 4
# Número de columnas
ncol = 5
# Creamos una lista para las filas del cine
cine = []
# Bucle iterativo para recorrer las filas del cine
for i in range(nfil):
    # Creamos una lista para las butacas de una fila
    fila = []
    for j in range(ncol):
        # Ponemos el caracter X en la fila i y la columna j del cine
        fila.append("X")
    # Añadimos la fila al cine
    cine.append(fila)
# Bucle para preguntar al usuario por la reserva
while True:
    print("\nRESERVA DE BUTACAS")
    # Bucle para recorrer las filas del cine y mostrarlas por pantalla
    for i in cine:
        #Unimos todas las butacas de la fila i en una cadena y la mostramos por pantalla
        print("".join(i))
    # Preguntamos al usuario por la fila que quiere
    fila = int(input("Introduce la fila que quieres: "))
    # Preguntamos al usuario por la columna que quiere
    columna = int(input("Introduce la columna que quieres: "))
    # Si el número de fila o columna son mayores de los disponibles avisamos al usuario
    if fila > nfil or columna > ncol:
        print("La fila y columna elegidas no son válidas.")
    # Si la fila y la columna que quiere el usuario está ocupada, le avisamos
    elif cine[fila-1][columna-1] == "O":
        print("La butaca elegida está ocupada.")
    # En caso contrario, reservamos la butaca escribiendo un "O" en la posición de la fila y la columna
    else:
        cine[fila-1][columna-1] = "O" 
        print("Reserva realizada.")
    # Preguntamos al usuario si quiere hacer otra reserva y si no salimos del bucle
    if input("¿Desea realizar otra reserva? (S/N): ") != "S":
        break
print("¡Gracias!")