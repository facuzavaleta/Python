"""Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. 
Escribir un programa que comience leyendo el número de barras vendidas que no son del día. 
Después el programa debe mostrar el precio habitual de una barra de pan, el descuento 
que se le hace por no ser fresca y el coste final total."""

precioPan = 3.49
descuento = 0.60

numBarrasVendidas = int(input("Cuantas barras que no son del día se vendieron hoy? "))

costeFinal = (numBarrasVendidas * precioPan) * (1 - descuento)

print(f"El precio habitual de la barra de pan es de ${precioPan}, el descuento que se aplica por no ser del dia es del {descuento * 100}%, por lo que el coste total es de {round(costeFinal, 2)}.")