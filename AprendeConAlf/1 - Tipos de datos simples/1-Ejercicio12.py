precioPan = 3.49
descuento = 0.6
barrasVendidas = int(input("Barras vendidas: "))
print(f"""
Precio habitual: {precioPan}€
Descuento: {descuento * 100}%
Coste final: {round((barrasVendidas * precioPan) * (1 - descuento), 2)}€
""")