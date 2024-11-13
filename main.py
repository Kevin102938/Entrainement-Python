
nom = "Kevin"

# Méthode numéro 1
print ("Mon nom est " + nom)

# Méthode numéro 2
print (f"Mon nom est {nom}")

print("------------------")

a= 100
b=9

c=a/b
print(c)

print("------------------")

# def est_premier_ (nombre):
#     if nombre <= 1 or nombre == 0: print ("Le nombre " + nombre + " n'est pas premier")


#     return nombre


def est_premier(nombre):
    # Si le nombre est inférieur ou égal à 1, il n'est pas premier
    if nombre <= 1:
        return False

    # Cas particuliers : 2 et 3 sont des nombres premiers
    if nombre == 2 or nombre == 3:
        return True

    # Vérifie si le nombre est divisible par un nombre entre 2 et sa racine carrée
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False  # Le nombre n'est pas premier, un diviseur a été trouvé

    # Si aucun diviseur n'a été trouvé, le nombre est premier
    return True

# Exemple d'utilisation
nombre = int(input("Entrez un nombre: "))
if est_premier(nombre):
    print(f"{nombre} est un nombre premier.")
else:
    print(f"{nombre} n'est pas un nombre premier.")