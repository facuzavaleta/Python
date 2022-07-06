pesoPayaso = 0.112
pesoMuñeca = 0.075
payasos = int(input("Cantidad de payasos: "))
muñecas = int(input("Cantidad de muñecas: "))
pesoTotal = round(payasos * pesoPayaso + muñecas * pesoMuñeca, 3)

print(pesoTotal, "kg")