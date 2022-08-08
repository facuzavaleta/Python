materias = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
suma = 0
for materia in materias:
    print(f"{materia} tiene {materias[materia]} créditos.")
    suma += materias[materia]
print(f"El número total de créditos es de {suma} créditos.")