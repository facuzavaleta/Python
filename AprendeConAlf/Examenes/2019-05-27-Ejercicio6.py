def facturacion(facturas, nif, mes):
    """
    Función que recibe una lista de facturas y devuelve el número de facturas y el total facturado correspondiente a un nif y mes indicados.
    Parámetros:
        - facturas: Es una lista de facturas, donde cada factura es un diccionario con las claves nif, mes, cantidad e iva.
        - nif: Es una cadena con un nif.
        - mes: Es una cadena con el nombre de un mes.
    Devuelve:
        Un diccionario con el número de facturas y el total facturado (incluído el iva) al nif indicado en el mes indicado.
    """
    # Filtramos la lista para quedarnos con la lista de las cantidades de cada diccionario que tenga el nif y el mes indicados
    filtro = [factura['cantidad'] * (1 + factura['iva'] / 100) for factura in facturas if (factura['nif'] == nif and factura['mes'] == mes)]
    # Devolvemos un diccionario con la longitud de la lista (número de facturas) y la suma de sus valores (total facturado)
    return {'Num facturas': len(filtro), 'Total facturado': sum(filtro)}


# Lista de facturas de prueba
facturas = [{'nif': 'B12345678', 'mes': 'marzo', 'cantidad':1000, 'iva': 10},
            {'nif': 'A98765432', 'mes': 'julio', 'cantidad':500, 'iva': 21},
            {'nif': 'B12345678', 'mes': 'marzo', 'cantidad':2000, 'iva': 21},
            {'nif': 'C02040506', 'mes': 'enero', 'cantidad':200, 'iva': 4},
            {'nif': 'A98765432', 'mes': 'julio', 'cantidad':1500, 'iva': 10},
            {'nif': 'B12345678', 'mes': 'abril', 'cantidad':600, 'iva': 10},
            {'nif': 'B12345678', 'mes': 'marzo', 'cantidad':100, 'iva': 4}]

# Llamadas a la función de prueba
print(facturacion(facturas, 'B12345678', 'marzo'))
print(facturacion(facturas, 'B12345678', 'abril'))
print(facturacion(facturas, 'B12345678', 'agosto'))