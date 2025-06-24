class Livre:
    def __init__(self, titre, auteur):
        self.titre = titre
        self.auteur = auteur

    def __str__(self):
        return f"{self.titre} par {self.auteur}"

class Bibliotheques:
    def __init__(self):
        self.livres = []
    
    def ajouter_livre(self, titre, auteur):
        livre = Livre(titre, auteur)
        self.livres.append(livre)

    def afficher_livres(self):
        if not self.livres:
            print("Aucun livre dans la bibliothèque.")
        else:
            for idx, livre in enumerate(self.livres, start=1):
                print(f"{idx}. {livre}")
    
    def rechercher_livres(self, critere):
        resultats = [livre for livre in self.livres if critere.lower() in livre.titre.lower() or critere.lower() in livre.auteur.lower()]
        if not resultats:
            print("Aucun livre trouvé")
        else:
            for livre in resultats:
                print(livre)
    
    def supprimer_livre(self, titre):
        for livre in self.livres:
            if livre.titre.lower() == titre.lower():
                self.livres.remove(livre)
                print(f"Le livre '{titre}' a été supprimé.")
                return
        print(f"Aucun livre trouvé avec le titre '{titre}'.")
    


def afficher_menu():
    print("\nSystème de gestion de bibliothèque")
    print("1 : Ajouter un livre")
    print("2 : Afficher les livres")
    print("3 : Rechercher un livre")
    print("4 : Supprimer un livre")
    print("5 : Quitter")

def main():
    bibliotheque = Bibliotheques()
    while True:
        afficher_menu()
        choix = input("Entrez votre choix :" )

        if choix == "1":
            titre = input("Entrez le titre du livre : ")
            auteur = input("Entrez l'auteur du livre : ")
            bibliotheque.ajouter_livre(titre, auteur)
        elif choix == "2":
            bibliotheque.afficher_livres()
        elif choix == "3":
            critere = input("Entrez le titre ou l'auteur à rechercher : ")
            bibliotheque.rechercher_livres(critere)
        elif choix == "4":
            titre = input("Entrez le titre du livre à supprimer : ")
            bibliotheque.supprimer_livre(titre)
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide. Veuillez réessayer.")
        
if __name__ == "__main__":
    main()
