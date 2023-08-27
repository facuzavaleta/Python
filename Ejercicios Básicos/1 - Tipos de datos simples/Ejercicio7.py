"""Ejercicio 7
Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), 
calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase 
Tu índice de masa corporal es <imc> donde <imc> es el índice de masa corporal calculado
 redondeado con dos decimales."""

kg = float(input("Ingrese su peso en kg: "))
mts = float(input("Ingrese su altura en metros: "))
imc = kg / mts ** 2

print(f"Su indice de masa corporal es de {round(imc, 2)}.")