asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
asignaturasDesaprobadas = []

for i in asignaturas:
    nota = int(input(f"Que nota has sacado en {i}?: "))
    if nota < 6:
        asignaturasDesaprobadas.append(i)

if len(asignaturasDesaprobadas) >= 1:
    print("Debes repetir las siguientes asignaturas: ", end="")

    if len(asignaturasDesaprobadas) == 1:
        print(f"{asignaturasDesaprobadas[0]}.")

    elif len(asignaturasDesaprobadas) == 2:
        print(f"{asignaturasDesaprobadas[0]} y {asignaturasDesaprobadas[1]}.")

    else:
        for i in range(len(asignaturasDesaprobadas) - 2):
            print(f"{asignaturasDesaprobadas[i]}", end=", ")
        print(f"{asignaturasDesaprobadas[-2]}", end=" ")
        print(f"y {asignaturasDesaprobadas[-1]}.")

else:
    print("No debe repetir ninguna asignatura.")


