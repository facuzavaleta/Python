palabra = input("Escriba una palabra: ")
n = int(input("Escriba un numero para el n-grama: "))

if n <= len(palabra):
    for i in range(len(palabra) - n + 1):
        print(palabra[i:i+n])