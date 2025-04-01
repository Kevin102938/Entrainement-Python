n = int(input("Entrez un nombre : "))
i = 1 
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = 3 * n + 1
    print(f"Étape {i} : {n}")
    i+=1

print("Fin de la suite de Syracuse.")