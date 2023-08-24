kg = float(input("Ingrese su peso en kg: "))
mts = float(input("Ingrese su altura en metros: "))
imc = kg / mts ** 2

print(f"Su indice de masa corporal es de {round(imc, 2)}.")