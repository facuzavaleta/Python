#El validador contiene todas las demas funciones de verificacion
def validador(*args):
    return (isdigit(num)
        and tiene19(num)
        and empiezacon456(num)
        and gruposde4(num)
        and consecutivos(num))

#Se verifican que los datos ingresados sean solo digitos
def isdigit(*args):
    numSinSepa = num.replace("-", "")
    return numSinSepa.isdigit()

#Se verifican que la cantidad de caracteres ingresados sean 19
def tiene19(*args):
    return len(num) == 19

#Se verifica que la cadena ingresada comience con 4, 5 o 6
def empiezacon456(*args):
    return num.startswith ("4" or "5" or "6")

#Se verifica que la cadena pueda dividirse en 4 grupos de 4
def gruposde4(*args):                
    numSep = num.replace("-", " ")
    numsplit = numSep.split()
    return (len(numsplit)==4 
        and len(numsplit[0])==4 
        and len(numsplit[1])==4 
        and len(numsplit[2])==4 
        and len(numsplit[3])==4)

#Se verifica que no haya mas de 3 caracteres iguales consecutivos
def consecutivos(*args):
    numSinSep = num.replace("-", "")
    i = 0
    while i < len(numSinSep) - 3:
        if (numSinSep[i] == numSinSep[i + 1] 
        and numSinSep[i] == numSinSep[i + 2] 
        and numSinSep[i] == numSinSep[i + 3]):
            return False
        i += 1
    return True

#Se pide que ingrese el numero, ofreciendo 5 intentos
numeroIntentos = 5
print ("Tiene", numeroIntentos, "intentos.")
num = input("Ingrese el número de la tarjeta: ")

#Se verifican los numeros de intentos disponibles, y se ejecuta el validador
while numeroIntentos != 0:
    if validador(num):
        print ("Su número ingresado es válido.")
        exit()
    else:
        numeroIntentos -= 1
        if numeroIntentos > 0:
            print ("Su número ingresado no es válido, le quedan", numeroIntentos, "intentos.")
            num = input("Por favor ingreselo nuevamente: ")
print("Lo siento, se le acabaron los intentos, espere un momento y vuelva a intentarlo.")
