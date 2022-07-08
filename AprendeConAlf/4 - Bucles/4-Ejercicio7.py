num = int(input("Ingrese un numero para ver su tabla de multiplicar del 1 al 10: "))

for i in range(10):
    print(f"{num} x {i + 1} = {num * (i + 1)}")