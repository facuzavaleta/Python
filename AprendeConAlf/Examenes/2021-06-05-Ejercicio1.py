tupla = (5, 20, 3, 7, 6, 8); listaMinMax = []; listaTupla = list(tupla)
n = int(input("Ingrese un numero: "))

for i in range(n):

    listaMinMax.append(min(listaTupla))
    listaTupla.remove(min(listaTupla))
    listaMinMax.append(max(listaTupla))
    listaTupla.remove(max(listaTupla))

listaMinMax.sort()
tuplaMinMax = tuple(listaMinMax)

print(f"La tupla original es: {tupla}\nLa tupla con los n = {n} maximos y minimos es: {tuplaMinMax}")
