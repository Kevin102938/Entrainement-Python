import random

def menu():
    print("\nBienvenue dans le jeu de Pierre-Papier-Ciseaux !")
    print("1 : Pierre")
    print("2: Papier")
    print("3: Ciseaux")
    print("4Quitter")

def obtenir_choix_utilisateur():
    choix = input("Entrez votre choix (1/2/3/4) : ")
    if  choix in ["1", "2", "3", "4"]:
        return int(choix)
    else:print("Choix invalide. Veuillez réessayer.")
    return obtenir_choix_utilisateur()

def obtenir_choix_ordinateur():
    return random.randint(1, 3)

def determiner_gagnant(choix_utilisateur, choix_ordinateur):
    resultats = {
        1:"Pierre",
        2:"Papier",
        3:"Ciseaux"
    }

    print(f"Vous avez choisi : {resultats[choix_utilisateur]}")
    print(f"L'ordinateur a choisi : {resultats[choix_ordinateur]}")

    if choix_utilisateur == choix_ordinateur:
        return "Egalité !"
    elif (choix_utilisateur == 1 and choix_ordinateur == 3) or \
        (choix_utilisateur == 2 and choix_ordinateur == 1) or \
        (choix_utilisateur == 3 and choix_ordinateur == 2):
        return "Vous gagnez!"
    else:
        return "L'ordinateur gagne!"
    

def main():
    while True:
        menu()
        choix_utilisateur = obtenir_choix_utilisateur()
        if choix_utilisateur == 4:
            print("Merci d'avoir joué !")
            break
        choix_ordinateur = obtenir_choix_ordinateur()
        resultat = determiner_gagnant(choix_utilisateur, choix_ordinateur)
        print(resultat)

if __name__ == "__main__":
    main()