ingredientes = ["mozzarella", "tomate", "pimiento", "tofu", "peperoni", "jamón", "salmón"];main = input("""Bienvenidos a la pizzería Bella Napoli. ¿Quiere una pizza vegetiarana?\nIngrese "si" o "no": """).lower()
if main == "si":
    menuVeg = input(f"""\nIngredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - \n \nIngrese el número del ingrediente extra que desea: \n1 - {ingredientes[2]}\n2 - {ingredientes[3]}\n-> """)
    if menuVeg == "1":
        print(f"""\nPizza Vegetariana. Ingredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - {ingredientes[2]}\n""")
    elif menuVeg == "2":
        print(f"""\nPizza Vegetariana. Ingredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - {ingredientes[3]}""")
elif main == "no":
    menuNoVeg = input(f"""\nIngredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - \n    \nIngrese el número del ingrediente extra que desea: \n1 - {ingredientes[4]}\n2 - {ingredientes[5]}\n3 - {ingredientes[6]}\n-> """)
    if menuNoVeg == "1":
        print(f"""\nPizza No Vegetariana. Ingredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - {ingredientes[4]}""")
    elif menuNoVeg == "2":
        print(f"""\nPizza No Vegetariana. Ingredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - {ingredientes[5]}""")
    elif menuNoVeg == "3":
        print(f"""\nPizza No Vegetariana. Ingredientes:\n1 - {ingredientes[0]}\n2 - {ingredientes[1]}\n3 - {ingredientes[6]}""")