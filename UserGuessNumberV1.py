from random import randint

numOculto = randint(1,50)

num = int(input("Adivine un numero entre el 1 y el 50, o ingrese 0 para terminar: "))
while num != 0:
    if num == numOculto:
        print(num, " es Correcto, adivinaste")
        numOculto = randint(1,50)
        num = int(input("Adivine otro numero entre el 1 y el 50, o ingrese 0 para terminar: "))
    elif num > numOculto:
        num = int(input("Un poco mas abajo, intentalo nuevamente: "))
    elif num < numOculto:
        num = int(input("Un poco mas arriba, intentalo nuevamente: "))
if num == 0:
    exit()
        
