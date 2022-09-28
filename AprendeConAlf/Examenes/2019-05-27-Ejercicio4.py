def numeros(n):
    unidades = {0:'', 1:'uno', 2:'dos', 3:'tres', 4:'cuatro', 5:'cinco', 6:'seis', 7:'siete', 8:'ocho', 9:'nueve'}
    decenas = {0:'', 1:'diez', 2:'veinte', 3:'treinta', 4:'cuarenta', 5:'cincuenta', 6:'sesenta', 7:'setenta', 8:'ochenta', 9:'noventa'}
    centenas = {0:'', 1:'ciento', 2:'doscientos', 3:'trescientos', 4:'cuatrocientos', 5:'quinientos', 6:'seiscientos', 7:'setecientos', 8:'ochocientos', 9:'novencientos'}

    cen = n // 100
    dec = (n // 10) % 10
    uni = n % 10

    if not uni:
        nexo = ""
    elif not dec:
        nexo = ""
    else:
        nexo = " y "

    return centenas[cen] + " " + decenas[dec] + nexo + unidades[uni]

print(numeros(990))
