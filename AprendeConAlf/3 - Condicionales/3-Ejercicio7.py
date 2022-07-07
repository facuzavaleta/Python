renta_anual = float(input("Ingrese su renta anual: "))
if renta_anual < 10000:
    print("Su impuesto es del 5%")
elif renta_anual >= 10000 and renta_anual < 20000:
    print("Su impuesto es del 15%")
elif renta_anual >= 20000 and renta_anual < 35000:
    print("Su impuesto es del 20%")
elif renta_anual >= 35000 and renta_anual < 60000:
    print("Su impuesto es del 30%")
else:
    print("Su impuesto es del 45%")