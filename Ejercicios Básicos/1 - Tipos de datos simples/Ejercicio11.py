"""Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. 
Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance 
final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada 
en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por 
pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales."""

deposito = float(input("Ingrese la cantidad que desea depositar: "))
interes_anual = 4
balance1año = round(deposito + deposito * (interes_anual / 100), 2)
balance2año = round(balance1año + balance1año * (interes_anual / 100), 2)
balance3año = round(balance2año + balance2año * (interes_anual / 100), 2)
print (f"El balance tras el primer año es de {balance1año}, tras el 2do año es de {balance2año}, tras el 3er año es de {balance3año}.")