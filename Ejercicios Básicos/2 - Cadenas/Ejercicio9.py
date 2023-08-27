"""Ejercicio 9
Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa 
y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también 
funcione cuando el día o el mes se introduzcan con un solo carácter."""

fecha = input("Ingrese la fecha con el formato DD/MM/AAAA: ")
print(f"""
{fecha.split("/")[0]} dias,
{fecha.split("/")[1]} meses, 
{fecha.split("/")[2]} años.""")