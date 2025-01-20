def puissance(x,n):
    if n < 0 :
        return n
    if n == 0:
        return 1
    else:
        return x * puissance(x,n-1)
    
print(puissance(2,3)) # 8


def puissanceRec(x,n):
    if n == 0:
        return 1
    return puissanceRec(x,n-1) * x

print(puissanceRec(2,5)) # 32


def factorielle_iterative(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(factorielle_iterative(5)) # 120


def factorielle_recursive(n):
    if n == 0:
        return 1
    return n * factorielle_recursive(n-1)

print(factorielle_recursive(5)) # 120