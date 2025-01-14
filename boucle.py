import math

print("Afficher les nombres de 0 à 10 : ")
for i in range(0, 11):
    print(i)

print("\n")

def pyramide(n):
    for i in range(1, n+1):
        print(f"{i} : " + ("*"*i))

pyramide(5)

print("\n")
def table_multi(n):
    for i in range(1,11):
        print(f"{i} x {n} = {i*n}")
    return n
choix = int(input("Entrez un nombre pour afficher sa table de multiplication : "))
table_multi(choix)

print("\n")

def nombre_impair(liste):
    impairs = []  # Créer une liste pour stocker les nombres impairs
    for i in liste:
        if i % 2 != 0:
            impairs.append(i)  # Ajouter le nombre impair à la liste
    print(f"Voici les nombres impairs de la liste : {impairs}")
    return impairs  # Retourner la liste des nombres impairs

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Voici la liste en entière : {liste}")
impairs = nombre_impair(liste)
print(f"Résultat sous forme de liste : {impairs}")

print("\n")

def detecter_mot(mot, lettre):
    trouve = False
    for char in mot:
        if char == lettre:
            trouve = True
            break
    
    if trouve:
        print(f"La lettre '{lettre}' est présente dans le mot.")
    else:
        print(f"La lettre '{lettre}' n'est pas présente dans le mot.")
    
    return trouve

mot = input("Entrez un mot : ")
lettre = input("Entrez une lettre : ")
detecter_mot(mot, lettre)