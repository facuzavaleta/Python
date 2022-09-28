añoInicial = int(input("Ingrese el año incial: "))
añoFinal = int(input("Ingrese el año final: "))
ingresos = []; gastos = []; beneficios = []; años = []; hay_beneficio = []; años_beneficios = []; años_perdidas = []

for i in range(añoInicial, añoFinal + 1):
    años.append(i)
    ingresos.append(int(input(f"Ingresos del año {i}: \n")))
    gastos.append(int(input(f"Gastos del año {i}: \n")))

for i in range(añoFinal - añoInicial + 1):
    beneficios.append(ingresos[i] - gastos[i])

for i in range(len(beneficios)):
    hay_beneficio.append(beneficios[i] > 0)

for i in range(len(hay_beneficio)):
    if hay_beneficio[i]:
        años_beneficios.append(años[i])
    else:
        años_perdidas.append(años[i])

print(f"Años con beneficios: {años_beneficios}")
print(f"Años con perdidas: {años_perdidas}")