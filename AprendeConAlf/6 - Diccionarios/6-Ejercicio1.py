monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
moneda = input("Introduce una divisa: ")
print(monedas.get(moneda.title(), "La divisa no está."))

# divisas = {'Euro':'€', 'Dolar':'$', 'Yen':'¥'}
# user = input("Ingrese el nombre de alguna divisa: ")

# for i in divisas:
#     if user == i:
#         print(divisas[i])
#     elif user not in divisas:
#         print("No esta en el diccionario.")
#         break