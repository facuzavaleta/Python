compra = {}
respuesta = True
total = 0
while respuesta:
    articulo = input("Ingrese el articulo: ")
    precio = float(input(f"Ingrese el precio para {articulo}: "))
    compra[articulo] = precio
    total += compra[articulo]
    respuesta = input("Desea agregar otro producto? (Si/No): ") == "Si"
print()
for art, pre in compra.items():
    print(f"{art}: {pre}")
print(f"Total: {total}")