def areaCirculo(radio):
    return 3.14 * radio**2

def volCilindro(radio, altura):
    return areaCirculo(radio)*altura

print(volCilindro(3, 5))