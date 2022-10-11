lista = [1, 2, 2, 3, 4, 4, 5, 5, 5, 6]

repeticiones = {}

for n in lista:
    repeticiones[n] = lista.count(n)
for n in lista:
    if lista.count(n) > 1:
        lista.remove(n)

print(lista)
print(repeticiones)