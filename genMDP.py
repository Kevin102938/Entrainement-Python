import random
import string


def generateur(nombre):


    return nombre


caracteres = string.ascii_letters + string.digits + string.punctuation
longueur = int(input("Entrez la longueur souhaitée pour le mot de passe : "))
mot_de_passe = "".join(random.choice(caracteres) for _ in range(longueur))
print(f"Votre mot de passe généré est : " + mot_de_passe)