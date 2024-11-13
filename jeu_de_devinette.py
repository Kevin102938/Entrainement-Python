import random

def devinette():
    nb_alea = random.randint(1, 100)  # Génère un nombre aléatoire entre 1 et 100
    nb_user = -1 

    while(nb_user != nb_alea):
        nb_user = int(input("Entrez un nombre entre 1 et 100 : "))
        if nb_user < nb_alea: 
            print(f"Le nombre choisi est plus grand que {nb_user}")
        elif nb_user > nb_alea:
            print(f"Le nombre choisi est plus petit que {nb_user}")
        else:
            print("Bravo !!")


print("\n\nEssayer de trouver le bon nombre ")
devinette()