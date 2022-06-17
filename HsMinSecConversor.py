#Aquí se da la bienvenida y se le piden los datos al usuario

print ("Bienvenidos al Conversor de Horas, Minutos y Segundos.\nProgramado por Facundo Zavaleta en Python 3.")
print ("Por favor, ingrese la cantidad de horas para convertir en minutos y segundos:")
horas = int(input())
print ("Muchas gracias, ahora por favor ingrese la cantidad de minutos para convertir en horas y segundos:")
minutos = int(input())
print ("Muchas gracias, por último ingrese la cantidad de segundos para convertir en horas y minutos:")
segundos = int(input())

#Aquí se realizan las operaciones matemáticas

hs_a_min = horas * 60
hs_a_seg = horas * 3600
min_a_hs = minutos / 60
min_a_seg = minutos * 60
seg_a_hs = segundos / 3600
seg_a_min = segundos / 60

#Aquí se entregan los datos de salida y se finaliza el programa

print ("Muchas gracias, el resultado es:")
print (horas, "hora/s es igual a", (round(hs_a_min, 2)), "minutos y", round(hs_a_seg, 2), "segundos.")
print (minutos, "minuto/s es igual a", round(min_a_hs, 2), "horas y", round(min_a_seg, 2), "segundos.")
print (segundos, "segundo/s es igual a", round(seg_a_hs, 2), "horas y", round(seg_a_min,2), "minutos.")
print ("Muchas gracias por utilizar mi conversor.", end="\n", sep=" ")