def isPrime(num):
    divisor = 2
    while divisor < num:
        if num % divisor == 0:
            return False
        divisor += 1
    return True

num = int(input("Ingrese un numero para saber si es primo: "))
if isPrime(num):
    print("Es primo.")
else:
    print("No es primo.")