import os

path_fichier = "fichier/taches.txt"

def afficher_taches():
    if os.path.exists(path_fichier):
        with open(path_fichier, "r") as fichier:
            taches = fichier.readlines()
            if taches:
                print("\nListe des taches :")
                for i, tache in enumerate(taches, 1):
                    print(f"{i}.{tache.strip()}")
            else:
                print("Aucune tache à afficher")

    else:
        print("Le fichier n'existe pas !!")


def ajouter_tache():
    tache = input("Ajouter une nouvelle tache : ")
    with open(path_fichier, "a") as fichier:
        fichier.write(tache + "\n")
    print("Tache ajoutée avec succès.")
 

def supprimer_tache():
    afficher_taches()
    
    try:
        num_taches = int(input("Entrez le numéro de la tache à supprimer : "))
        with open(path_fichier, "r") as fichier:
            taches = fichier.readlines()
        
        if 0 < num_taches <= len(taches):
            del taches[num_taches - 1]
        
            with open(path_fichier, "w") as fichier:
                fichier.writelines(taches)
        
            print("Tache supprimée avec succès !")

        else:
            print("Numéro de tache invalide.")

    except ValueError:
        print("Veuillez rentrer un numéro valide !")


def menu():
    while True:
        print("\n\n\nMenu")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Quitter")

        choix = input("Choississez une option : (1/2/3/4) : \n")

        if choix == "1":
            afficher_taches()
        elif choix == "2":
            ajouter_tache()
        elif choix == "3":
            supprimer_tache()
        elif choix == "4":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Essayez à nouveau.")

menu()