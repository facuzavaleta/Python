rentaAnual = float(input("Ingrese su renta anual: "))

if rentaAnual < 10000:
    tipoImpositivo = 5
elif rentaAnual > 10000 and rentaAnual < 20000:
    tipoImpositivo = 15
elif rentaAnual > 20000 and rentaAnual < 35000:
    tipoImpositivo = 20
elif rentaAnual > 35000 and rentaAnual < 60000:
    tipoImpositivo = 30
else:
    tipoImpositivo = 45

print(f"Le corresponde el tipo impositivo de {tipoImpositivo}%.")