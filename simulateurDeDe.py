import random

def lancer_de():
    return random.randint(1, 6)

while True:
    # Lancer le dé
    resultat = lancer_de()
    print(f"Le dé affiche : {resultat}")
    
    # Proposer une relance
    rejouer = input("Voulez-vous relancer le dé ? (oui/non) : ").strip().lower()
    if rejouer != "oui":
        print("Merci d'avoir joué !")
        break
