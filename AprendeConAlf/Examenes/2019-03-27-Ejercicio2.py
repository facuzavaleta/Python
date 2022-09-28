def fcinco(euros):
    euros = euros // 5
    return euros

def fdos(euros):
    euros = euros // 2
    return euros

def funo(euros):
    euros = euros // 1
    return euros

def main():
    monedas = [1, 2, 5]; nMonedas = []
    euros = int(input("Ingrese una cantidad entera de Euros: "))

    cinco = fcinco(euros)
    euros = euros - cinco * monedas[2]
    nMonedas.append(cinco)

    dos = fdos(euros)
    euros = euros - dos * monedas[1]
    nMonedas.append(dos)

    uno = funo(euros)
    euros = euros - uno * monedas[0]
    nMonedas.append(uno)

    minMonedas = cinco + dos + uno

    print(f"Minimo de monedas: {minMonedas}\n$5: {nMonedas[0]}\n$2: {nMonedas[1]}\n$1: {nMonedas[2]}")

main()