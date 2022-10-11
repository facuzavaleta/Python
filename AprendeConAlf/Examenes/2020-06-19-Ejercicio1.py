materias = ["matematicas", "lengua", "historia", "quimica", "fisica", "programacion"]
notas = {}; reprobadas = []

for i in materias:
    nota = int(input(f"Introduce la nota de {i}: "))
    if nota < 0:
        print(f"Las materias reprobadas son {reprobadas}.")
        exit()
    elif nota < 6:
        reprobadas.append(i)
    else:
        notas[i] = nota

for materia, nota in notas.items():
    print(f"La nota de {materia} es de {nota}.")
print(f"Las materias reprobadas son {reprobadas}")