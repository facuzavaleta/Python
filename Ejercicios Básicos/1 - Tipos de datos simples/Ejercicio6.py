"""Ejercicio 6
Escribir un programa que lea un entero positivo,
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n."""

n = int(input("Ingrese un entero positivo: "))
suma = (n * (n + 1)) // 2

print(f"La suma de todos los numeros desde 1 hasta {n} es de {suma}")