"""Ejercicio 5
Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. 
Después debe mostrar por pantalla la paga que le corresponde."""

horas = int(input("Ingrese la cantidad de horas trabajadas: "))
coste = int(input("Ingrese el coste por hora: "))

print(f"La paga que le corresponde es de ${horas * coste}")