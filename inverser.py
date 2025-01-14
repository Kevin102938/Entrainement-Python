def inverserChaineCaracRec(chaine): 
    if len(chaine) == 0:
        return ""
    return chaine[-1] + inverserChaineCaracRec(chaine[:-1])

chaine = "Python"
print(f"Le résultat de l'inversion de la chaine {chaine} est : {inverserChaineCaracRec(chaine)}")

# --------------------------------------------------------------

def verifierPalindrome(chaine):
    if len(chaine) <= 1:
        return True
    if chaine[0] != chaine[-1]:
        return False
    return verifierPalindrome(chaine[1:-1])

chaine = "radar"
print(f"Le résultat de la vérification de la chaine {chaine} est : {verifierPalindrome(chaine)}")

#  --------------------------------------------------------------

def trouverPlusGrandElement (liste):
    if len(liste) == 1:
        return liste[0]
    return max(liste[0], trouverPlusGrandElement(liste[1:]))

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Le plus grand élément de la liste {liste} est : {trouverPlusGrandElement(liste)}")

# --------------------------------------------------------------

def tri_bulle(liste):
    n = len(liste)
    for i in range(n):
        # On parcourt la liste jusqu'à n-i-1 (les derniers éléments sont déjà triés)
        for j in range(0, n-i-1):
            if liste[j] > liste[j + 1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]

liste = [64, 34, 25, 12, 22, 11, 90]
print(f"la liste avant le tri est : {liste}")
tri_bulle(liste)
print(f"la liste après le tri est : {liste}")

    
# --------------------------------------------------------------

def tri_insertion(liste):
    # Parcours tous les éléments de la liste à partir du deuxième élément
    for i in range(1, len(liste)):
        # l'élement à insérer
        element = liste[i]
        j = i - 1 
        
        while j >= 0 and liste[j] > element:
            liste[j + 1] = liste[j]
            j -= 1
        
        # Insère la valeur actuelle à la bonne position
        liste[j + 1] = element

liste = [4, 6, 9, 0, 25, 1]
print(f"la liste avant le tri est : {liste}")
tri_insertion(liste)
print(f"la liste après le tri est : {liste}")