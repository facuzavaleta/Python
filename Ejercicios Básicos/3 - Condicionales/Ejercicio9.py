edad = int(input("Ingrese su edad: "))
if edad < 4:
    print("La entrada es gratis")
elif edad >= 4 and edad < 18:
    print("La entrada es de 5€")
else:
    print("La entrada es de 10€")