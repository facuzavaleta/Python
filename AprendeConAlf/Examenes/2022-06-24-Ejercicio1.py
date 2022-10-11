capital = float(input("Introduce un capital: "))
interes = float(input("Introduce un tipo de interes: "))
años = int(input("Introduce un numero de años: "))

def valor_futuro(capital, interes, años):
    for i in range(años):
        vf = capital * (1 + interes / 100) ** (i + 1)
        print(f"Año {i} : {vf}")
    return

def valor_actual(capital, interes, años):
    for i in range(años):
        va = capital / (1 + interes / 100) ** (i + 1)
        print(f"Año {-i} : {va}")
    return

valor_actual(capital, interes, años)