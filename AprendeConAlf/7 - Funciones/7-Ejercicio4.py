def impuesto(factura, iva = 21):
    return factura + (factura*iva) / 100
    #total = factura + (factura*iva) / 100
    #print(f"La factura de ${factura} con el IVA de %{iva} nos da un total de {total}")

print(impuesto(100, 12))