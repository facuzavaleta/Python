renta = int(input("Ingrese la renta: "))

if renta <= 12450:
    impuesto = renta * 0.19
elif renta > 12450 and renta <= 20200:
    impuesto = 12450 * 0.19 + (renta - 12450) * 0.24
elif renta > 20200 and renta <= 35200:
    impuesto = 12450 * 0.19 + (20200 - 12450) * 0.24 + (renta - 20200) * 0.3
else:
    impuesto = 12450 * 0.19 + (20200 - 12450) * 0.24 + (35200 - 20200) * 0.3 + (renta - 35200) * 0.37

print(f"Tienes que pagar ${impuesto} de impuestos.")