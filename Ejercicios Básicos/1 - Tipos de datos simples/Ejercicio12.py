precioPan = 3.49
descuento = 0.60

numBarrasVendidas = int(input("Cuantas barras que no son del día se vendieron hoy? "))

costeFinal = (numBarrasVendidas * precioPan) * (1 - descuento)

print(f"El precio habitual de la barra de pan es de ${precioPan}, el descuento que se aplica por no ser del dia es del {descuento * 100}%, por lo que el coste total es de {round(costeFinal, 2)}.")