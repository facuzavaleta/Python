dicc = {'919654665':'Pedro', '917489210': 'Luis', '623543213':'Carmen', '674833721':'Luis'}
diccReverse = {}

for i in dicc.values():
    diccReverse[i] = {}

for clave, valor in dicc.items():
    if clave[0] != "6":
        diccReverse[valor]["fijo"] = clave

    elif clave[0] == "6":
        diccReverse[valor]["movil"] = clave

for i in sorted(diccReverse.keys()):
    print(f"Telefonos de {i}:")
    for k, v in diccReverse[i].items():
        print(f"\t{k}: {v}")