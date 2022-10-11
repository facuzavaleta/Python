def esDivisible(n1, n2):
    if n1 % n2 == 0:
        return f"Es divisible, el resultado es {n1 / n2}, y el resto es de 0"
    else:
        return f"No es divisible, el resultado es {n1 // n2} y el resto es de {n1 % n2}"

def maxComDiv(n1, n2):
    divisores = []
    for i in range(1, min(n1, n2)):
        if n1 % i == 0 and n2 % i == 0:
            divisores.append(i)
    return max(divisores)

def minComMul(n1, n2):
    return (n1 * n2) / maxComDiv(n1, n2)