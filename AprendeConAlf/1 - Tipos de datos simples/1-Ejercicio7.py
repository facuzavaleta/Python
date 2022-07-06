peso = float(input("\nIngrese su peso en kg: "))
estatura = float(input("Ingrese su estatura en mts: "))
imc = round(peso / estatura ** 2, 1)
print(f"\nTu índice de masa corporal es: {imc}\n")