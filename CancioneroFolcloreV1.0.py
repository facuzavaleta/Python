artistas = {
    "1":"Peteco Carabajal",
    "2":"Vislumbre del Esteko",
    "3":"Presagio"}
cancionesPeteco = {
    "1":"Camino al Amor",
    "2":"Zamba para un Bohemio Guitarrero"}
cancionesVislumbre = {
    "1":"Ckeshu Sisa",
    "2":"Zamba del Llanural"}
cancionesPresagio = {
    "1":"Alma Maternal",
    "2":"Zamba de mi Universo"}

def eligeArtista():
    print (f"""Artistas disponibles:
    1 - {artistas["1"]}
    2 - {artistas["2"]}
    3 - {artistas["3"]}""")
    global numArtista
    numArtista=input("Escribe el numero del artista del cual deseas ver las canciones disponibles: ")
    
def eligeCancion(*args):
    if numArtista == "1":
        print(f"""\nCanciones disponibles:
    1 - {cancionesPeteco["1"]}
    2 - {cancionesPeteco["2"]}""")
    elif numArtista == "2":
        print(f"""\nCanciones disponibles:
    1 - {cancionesVislumbre["1"]}
    2 - {cancionesVislumbre["2"]}""")
    elif numArtista == "3":
        print(f"""\nCanciones disponibles:
    1 - {cancionesPresagio["1"]}
    2 - {cancionesPresagio["2"]}""")
    global numCancion
    numCancion=input("Escribe el numero de la cancion de la cual deseas ver la letra: ")

def muestraLetra(*args):
    if numArtista == "1" and numCancion == "1":
        print (f"""\nLetra de {cancionesPeteco["1"]}:""")
    elif numArtista == "1" and numCancion == "2":
        print (f"""\nLetra de {cancionesPeteco["2"]}:""")
    elif numArtista == "2" and numCancion == "1":
        print (f"""\nLetra de {cancionesVislumbre["1"]}:""")
    elif numArtista == "2" and numCancion == "2":
        print (f"""\nLetra de {cancionesVislumbre["2"]}:""")
    elif numArtista == "3" and numCancion == "1":
        print (f"""\nLetra de {cancionesPresagio["2"]}:""")
    elif numArtista == "3" and numCancion == "2":
        print (f"""\nLetra de {cancionesPresagio["2"]}:""")
    salida = input("\nPresione Enter para volver a la seleccion de Artistas:\n")
    if salida:
        main()

def main():
    eligeArtista()
    eligeCancion()
    muestraLetra()
    main()
# def main2():
#     eligeCancion()
#     muestraLetra()

main()
