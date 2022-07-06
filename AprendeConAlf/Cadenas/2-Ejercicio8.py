precio = input("Escriba el precio del producto, con 2 decimales: ")
print(f"""El precio ingresado es de {precio[:precio.index('.')]} euros 
con {precio[precio.index('.')+1:]} centavos.""")