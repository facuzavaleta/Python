edad = int(input("Ingrese su edad: "))
ingreso = float(input("Ingrese sus ingresos mensuales en euros: "))

if edad >= 16 and ingreso >= 1000:
    print("Debe tributar.")
else:
    print("No debe tributar.")