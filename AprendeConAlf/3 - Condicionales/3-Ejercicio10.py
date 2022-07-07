ingredientes = ["mozzarella", "tomate", "pimiento", "tofu", "peperoni", "jamón", "salmón"]

main = input("""Bienvenidos a la pizzería Bella Napoli. ¿Quiere una pizza vegetiarana?
Ingrese "si" o "no": """).lower()

if main == "si":
    menuVeg = input(f"""
Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - 
 
Ingrese el número del ingrediente extra que desea: 
1 - {ingredientes[2]}
2 - {ingredientes[3]}
-> """)

    if menuVeg == "1":
        print(f"""\nPizza Vegetariana. Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - {ingredientes[2]}
        """)
    elif menuVeg == "2":
        print(f"""\nPizza Vegetariana. Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - {ingredientes[3]}""")

elif main == "no":
    menuNoVeg = input(f"""
Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - 
    
Ingrese el número del ingrediente extra que desea: 
1 - {ingredientes[4]}
2 - {ingredientes[5]}
3 - {ingredientes[6]}
-> """)

    if menuNoVeg == "1":
        print(f"""\nPizza No Vegetariana. Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - {ingredientes[4]}
        """)
    elif menuNoVeg == "2":
        print(f"""\nPizza No Vegetariana. Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - {ingredientes[5]}""")
    elif menuNoVeg == "3":
        print(f"""\nPizza No Vegetariana. Ingredientes:
1 - {ingredientes[0]}
2 - {ingredientes[1]}
3 - {ingredientes[6]}""")