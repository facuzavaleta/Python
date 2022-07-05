cantidadDepositada = float(input("Cantidad depositada: "))
interesAnual = 0.04
primerAño = round(cantidadDepositada + cantidadDepositada * interesAnual, 2)
segundoAño = round(primerAño + primerAño * interesAnual, 2)
tercerAño = round(segundoAño + segundoAño * interesAnual, 2)

print(f"""
Primer año: {primerAño}
Segundo año: {segundoAño}
Tercer año: {tercerAño}
""")    