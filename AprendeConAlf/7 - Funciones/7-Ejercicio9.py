def maximoComunDivisor(num1, num2):
    listaNums = []
    for i in range(1, max(num1, num2)):
        if num1 % i == 0 and num2 % i == 0:
            listaNums.append(i)
    return max(listaNums)

def minimoComunMultiplo(num1, num2):
    multiplosNum1 = []
    multiplosNum2 = []
    multiplosComunes = []
    for i in range (1, 10):
        multiplosNum1.append(num1 * i)
        multiplosNum2.append(num2 * i)
    
    for i in range(max(num1, num2) * 9):
        if i in multiplosNum1 and i in multiplosNum2:
            multiplosComunes.append(i)
    
    return min(multiplosComunes)