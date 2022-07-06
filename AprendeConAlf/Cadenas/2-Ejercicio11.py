producto = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
unidades = float(input("Ingrese la cantidad de unidades: "))

print(f"""
El producto {producto} cuesta {precio}, 
El número de unidades es de {unidades} 
con un coste total de {round(precio * unidades, 2)}
""")