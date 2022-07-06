productos = input("Ingrse los productos, separados por comas: ")
listaProductos =  productos.split(", ")
i=0
for producto in listaProductos:
    i+=1
    print(i, producto)