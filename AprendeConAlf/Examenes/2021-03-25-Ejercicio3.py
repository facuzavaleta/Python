cadena = 'disco duro 500Gb;200;25;15\nmemoria ram 16Gb;500;30;20\nratón inalámbrico;800;12;10\ntarjeta wifi;150;20;12'
listaProductos = cadena.split("\n")
productos = {}

for i in listaProductos:
    info = i.split(";")
    productos[info[0]] = [info[1], info[2], info[3]]

for producto, info in productos.items():
    precio = float(info[1]) * (1 - float(info[2]) / 100)
    print(producto, "vale", "$", precio)