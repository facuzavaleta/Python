def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]

def dayOfYear(year, month, day):
    if month > 12 or month < 1:
        return None
    if day > daysInMonth(year, month) or day < 1:
        return None
    
    totalDays = day
    month = month -1
    while month > 0:
        totalDays += daysInMonth(year, month)
        month -= 1
    return totalDays

while True:
    yr = int(input("Ingrese el año: "))
    mo = int(input("Ingrese el mes: "))
    dy = int(input("Ingrese el dia: "))
    print ("El dia", dy, "del mes", mo, "del año", yr, "es el dia numero", dayOfYear(yr, mo, dy), "del año.")
