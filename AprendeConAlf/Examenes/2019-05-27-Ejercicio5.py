def limpiar(cifra):
    """
    Función que elimina los puntos de separación de miles y cambia las comas de separación de decimales por puntos.
    Parámetros:
        - cifra: Es una cadena con una cifra
    Devuelve:
        Un real con la cifra de la cadena después de eliminar el separador de miles y cambiar el separador de decimales por punto.
    """
    cifra = cifra.replace('.', '')
    cifra = cifra.replace(',','.')
    return float(cifra) 

def preprocesado(ruta):
    """
    Función que preprocesa los datos contenidos en un fichero con formato csv y devuelve un diccionario con los nombres de las columnas como claves y las listas de valores asociados a ellas.
    Parámetros:
        - ruta: Es una cadena con la ruta del fichero.
    Devuelve:
        Un diccionario con pares formados por los nombres de las columnas y las listas de valores en las columnas.
    """
    try:
        # Abrimos el fichero en modo lectura
        f = open(ruta, 'r')
    except FileNotFoundError:
        print('El fichero no existe.')
        return
    # Leemos el fichero por líneas en una lista
    lines = f.readlines()
    # Cerramos el fichero
    f.close()
    # Leemos las claves del primer elemento de la lista y eliminamos el cambio de línea que aparece al final
    claves = lines[0]
    # Eliminamos el cambio de línea que aparece al final y dividimos la cadena por el punto y coma
    claves = claves[:-1].split(';')
    # Creamos el diccionario
    cotizaciones = {}
    # Inicializamos el diccionario con listas vacías
    for i in claves:
        cotizaciones[i] = []
    # Recorremos la lista línea a línea
    for linea in lines[1:]:
        # Eliminamos el cambio de línea que aparece al final y dividimos la cadena por el punto y coma
        linea = linea[:-1].split(';')
        cotizaciones[claves[0]].append(linea[0])
        # Añadimos cada dato a la lista correspondiente del diccionario
        for i in range(1, len(cotizaciones)):
            cotizaciones[claves[i]].append(limpiar(linea[i]))
    return cotizaciones


def resumen_cotizacion(cotizaciones, ruta):
    """
    Función que recibe un diccionario con los valores de cotización y crear un fichero con un resumen con el mínimo, el máximo y la media.
    Parámetros:
        - cotizaciones: Es un diccionario con pares cuyas claves son los nombres de la variables medidas y cuyos valores son las listas de valores de cada variable.
        - ruta: Es una cadena con la ruta del fichero.
    """
    # Eliminamos el primer par del diccionario que contiene los nombres de las empresas
    del(cotizaciones['Nombre'])
    # Abrimos el fichero en modo escritura
    f = open(ruta, 'w')
    # Escribimos en la primera línea los nombres de las columnas
    f.write('Nombre')
    for clave in cotizaciones.keys():
        f.write(';' + clave)
    # Calculamos los mínimos de cada lista y los escribimos en las columnas correspondientes
    f.write('\nMínimo')
    for valores in cotizaciones.values():
        f.write(';' + str(min(valores)))
    # Calculamos los máximos de cada lista y los escribimos en las columnas correspondientes
    f.write('\nMáximo')
    for valores in cotizaciones.values():
        f.write(';' + str(max(valores)))
    # Calculamos las medias de cada lista y las escribimos en las columnas correspondientes
    f.write('\nMedia')
    for valores in cotizaciones.values():
        f.write(';' + str(sum(valores)/len(valores)))
    f.close()
    return


# Llamada a las funciones de prueba
cotizaciones = preprocesado('/home/facuzavaleta89/dev/AprendeConAlf/Examenes/cotizacion.csv')
resumen_cotizacion(cotizaciones, '/home/facuzavaleta89/dev/AprendeConAlf/Examenes/resumen-cotizacion.csv')