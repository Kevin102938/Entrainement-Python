def table(nombre):
    for i in range(1, 11):
        resultat = nombre * i
        print(f"{nombre} x {i} = {resultat}")

nombre = int(input("Entrez un nombre pour voir sa table de multiplication : "))
table(nombre)