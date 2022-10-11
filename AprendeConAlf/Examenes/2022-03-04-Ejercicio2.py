meses = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre", "noviembre", "diciembre"]
dias = {"enero":31, "febrero":28, "marzo":31, "abril":30, "mayo":31, "junio":30, "julio":31, "agosto":31, "septiembre":30, "octubre":31, "noviembre":30, "diciembre":31}

print("CALENDARIO LUNAR")
print("Este programa convierte una fecha de un año NO bisiesto a un calendario lunar.")

dia = int(input("Indique el dia: "))
mes = input("Indique el mes: ")

if mes not in meses:
    print(f"El mes {mes} no existe.")
elif dia < 1 or dia > dias[mes]:
    print(f"El dia {dia} del mes {mes} no existe.")
else:
    numdias = 0
    for i in meses:
        if i != mes:
            numdias += dias[i]
        else:
            numdias += dia
            break

print("El día", dia, "de", mes, "es el día", numdias, "del año.")
print("Habrán pasado", round(numdias / 29.53, 2), "meses lunares.")