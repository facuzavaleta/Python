cantidadAInvertir = float(input("Ingrese la cantidad a invertir: "))
interesAnual = float(input("Ingrese el interes anual: ")) / 100
años = int(input("Ingrese la cantidad de años: "))

print(f"El capital obtenido en la inversion es de", round(cantidadAInvertir * (interesAnual * años), 2))