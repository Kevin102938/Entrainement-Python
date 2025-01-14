def facto(n):
    if n == 0:
        return 1
    else:
        return n * facto(n - 1)
n= 5
print(f"Le factorielle de {n} est : {facto(n)}")


def puissanceNombre(x,n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    return x * puissanceNombre(x,n-1)

nombre = 5
puissance = 3
print(f"Le résulat de {nombre} à la puissance {puissance} est : {puissanceNombre(nombre,puissance)}")