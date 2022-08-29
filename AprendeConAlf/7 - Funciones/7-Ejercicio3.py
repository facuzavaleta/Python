def factorial():
    factorial = 1
    num = int(input("Ingrese un numero entero positivo: "))
    for i in range(1, num + 1):
        factorial *= i
    print(factorial)

factorial()