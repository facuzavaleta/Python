palabra = input("Ingrese una palabra: "); palabraReverse = palabra[::-1]

for i in range(len(palabraReverse) - 1):
    print (palabraReverse[i], end=", ")
print(palabraReverse[-1] + ".")