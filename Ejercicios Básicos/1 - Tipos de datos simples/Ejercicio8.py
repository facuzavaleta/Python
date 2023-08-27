"""Ejercicio 8
Escribir un programa que pida al usuario dos números enteros y muestre por pantalla la <n> entre <m> 
da un cociente <c> y un resto <r> donde <n> y <m> son los números introducidos por el usuario, 
y <c> y <r> son el cociente y el resto de la división entera respectivamente."""

n1 = int(input("Ingrese un numero entero: "))
n2 = int(input("Ingrese otro numero entero: "))
cociente = n1 // n2
resto = n1 % n2

print (f"El cociente de {n1} entre {n2} es de {cociente} y el resto es de {resto}.")