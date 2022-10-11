import random

def main():
    sumas = [random.choice([x + 1 for x in range(50)]) for i in range(6)]; aciertos = 0; suma = 0
    print("\nSUMAR Y GANAR\nVaya sumando todos los numeros que le ire diciendo. Empezamos por 0: ")
    for i in sumas:
        suma += i
        resp = int(input(f"Más {i}: "))
        if resp == suma:
            aciertos += 1
        else:
            print(f"Te has equivocado, pero has acertado {aciertos} veces seguidas.")
            exit()
    print("Enhorabuena, ganaste.")

main()