import random

def doublons(nb):
    liste = [random.randint(0, 100) for i in range(10)]
    print(liste)
    if nb in liste:
        print("Le nombre est présent dans la liste.")
    else:
        print("Le nombre n'est pas présent dans la liste.")



if __name__ == "__main__":
    try:
        # Demander à l'utilisateur de saisir un nombre et gérer les erreurs
        choix = int(input("Entrez un nombre : "))
        doublons(choix)
    except ValueError:
        # Afficher un message clair si l'utilisateur entre une valeur incorrecte
        print("Erreur : Veuillez entrer un nombre entier valide.")


