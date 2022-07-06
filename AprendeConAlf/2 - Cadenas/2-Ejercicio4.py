num = input("Ingrese su numero de teléfono con el siguiente formato: prefijo-número-extension: ")
numSin = num[num.index("-")+1:]
numSin = numSin[:numSin.index("-")]
print("El número sin prefijo ni extensión es:", numSin)

# num = input("Ingrese su numero de teléfono con el siguiente formato: prefijo-número-extension: ")
# print(num.split("-")[1])