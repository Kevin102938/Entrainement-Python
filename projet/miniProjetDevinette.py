import random

def generer_nombre():
    return random.randint(1,100)

def guess():
    while True:
        try:
            nombre = int(input("\nEntrez un nombre entre 1 et 100 : "))
            if 1 <= nombre <= 100:
                return nombre
            else:
                print("Veuillez rentrer un nombre entre 1 et 100 !!")
        except ValueError:
            print("Veuillez rentrer un nombre valide !!")

def jouer():
    essai = 0
    nombre_aleatoire = generer_nombre()

    while essai < 7:
        nombre_guess = guess()
        print(f"Essai {essai + 1} : {nombre_guess}")
        
        if nombre_guess < nombre_aleatoire:
            print("Le nombre choisi est plus grand que ", nombre_guess)
        elif nombre_guess > nombre_aleatoire:
            print("Le nombre choisi est plus petit que ", nombre_guess)
        else:
            print("Bravo !!")
            break
        essai += 1
    print(f"\n\n!!! Vous avez perdu! Le nombre était {nombre_aleatoire} !!!")

def main():
    while True:
        print(f"Bienvenue dans le jeu de devinette de nombre! Vous avez 7 tentatives pour deviner le nombre entre 1 et 100.\n")
        jouer()
        play_again = input("\nVoulez-vous rejouer? (Oui/Non) : ").lower()
        if play_again != "oui":
            print("\nMerci d'avoir joué! A bientôt!")
            break

if __name__ == "__main__":
    main()