"""Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales 
y muestre por pantalla el número de euros y el número de céntimos del precio introducido."""

eur = input("Ingresa el precio en euros con 2 decimales: ")
euro = eur[:eur.index(".")]
cent = eur[eur.index(".") + 1:]
print(f"Euro: {euro}.")
print(f"Centimos: {cent}.")