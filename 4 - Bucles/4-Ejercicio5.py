inversion = float(input("Cantidad a invertir: "))
interes = float(input("Interes anual: ")) / 100
años = int(input("Cantidad de años de inversion: "))

for i in range (1, años + 1):
    ganancia = inversion * interes
    inversion = inversion + inversion * interes
    if i == 1:
        print (f"""Capital tras {i} año: {round(inversion, 2)}, habiendo ganado {round(ganancia, 2)} ese año.
        """)
    if i > 1:
        print (f"""Capital tras {i} años: {round(inversion, 2)}, habiendo ganado {round(ganancia, 2)} ese año.
        """)