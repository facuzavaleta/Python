asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]; notas = []

for i in asignaturas:
    nota = input(f"Ingrese la nota que ha obtenido en {i}: ")
    notas.append(nota)

for i in range(len(asignaturas)):
    print(f"Usted ha sacado {notas[i]} en la asignatura {asignaturas[i]}.")