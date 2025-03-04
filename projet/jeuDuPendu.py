import random

def jouer_pendu():
    mots = ["python", "ordinateur", "programmation", "pendu", "variable"]
    mot_a_deviner = random.choice(mots)
    mot_cache = ["_" for _ in mot_a_deviner]
    lettres_trouvees = []
    tentatives = 6  # Nombre maximal de tentatives

    print("Bienvenue dans le jeu du pendu !")

    while tentatives > 0 and "_" in mot_cache:
        print("\nMot à deviner :", " ".join(mot_cache))
        print("Lettres devinées :", " ".join(lettres_trouvees))
        print(f"Il vous reste {tentatives} tentatives.")

        lettre = input("Entrez une lettre : ").lower()

        # Vérifier que l'utilisateur n'a pas déjà deviné cette lettre
        if lettre in lettres_trouvees:
            print("Vous avez déjà deviné cette lettre.")
            continue

        lettres_trouvees.append(lettre)

        if lettre in mot_a_deviner:
            # Révéler toutes les occurrences de la lettre
            for index, char in enumerate(mot_a_deviner):
                if char == lettre:
                    mot_cache[index] = lettre
            print(f"Bien joué ! La lettre '{lettre}' est dans le mot.")
        else:
            tentatives -= 1
            print(f"Oops ! La lettre '{lettre}' n'est pas dans le mot.")

    # Vérifier la condition de victoire ou de défaite
    if "_" not in mot_cache:
        print("\nFélicitations ! Vous avez trouvé le mot :", mot_a_deviner)
    else:
        print("\nDommage ! Vous n'avez plus de tentatives.")
        print("Le mot à deviner était :", mot_a_deviner)

# Lancer le jeu
jouer_pendu()