class Parent:
    def __init__(self, nom):
        self.nom = nom

    def afficher_nom(self):
        print(f"Je suis {self.nom}.")

# Classe enfant qui hérite de la classe Parent
class Enfant(Parent):

    def jouer(self):
        print(f"{self.nom} est en train de jouer.")


class Animal:
    def parler(self):
        pass  # Méthode abstraite ou générique

class Chien(Animal):
    def parler(self):
        return "Woof woof !"

class Chat(Animal):
    def parler(self):
        return "Miaou !"

class Canard(Animal):
    def parler(self):
        return "Coin coin !"

animaux = [Chien(), Chat(), Canard()]

for animal in animaux:
    print(animal.parler())
