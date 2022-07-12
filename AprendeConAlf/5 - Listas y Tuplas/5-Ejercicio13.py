numeros = (input("Ingrese una muestra de numeros separados por coma-espacio: "))
numList = numeros.split(", "); numDesviaciones = []
media = 0; desviacion = 0

for i in range(len(numList)):
    numList[i] = int(numList[i])

for i in numList:
    media += i

media /= len(numList)

for i in range(len(numList)):
    numDesviaciones.append((numList[i] - media) ** 2)

for i in numDesviaciones:
    desviacion += i

desviacion = (desviacion / len(numDesviaciones)) ** 0.5

print(f"La media es de: {round(media, 2)}, y la variacion estandar es de: {round(desviacion, 2)}.")