deposito = float(input("Ingrese la cantidad que desea depositar: "))
interes_anual = 4
balance1año = round(deposito + deposito * (interes_anual / 100), 2)
balance2año = round(balance1año + balance1año * (interes_anual / 100), 2)
balance3año = round(balance2año + balance2año * (interes_anual / 100), 2)
print (f"El balance tras el primer año es de {balance1año}, tras el 2do año es de {balance2año}, tras el 3er año es de {balance3año}.")