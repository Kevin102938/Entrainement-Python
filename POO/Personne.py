class Personne:

    def __init__(self,nom):
        self.nom = nom

    def dire_bonjour(self):
        print(f"Bonjour je m'appelle {self.nom}")
    
personne1 = Personne("Kevin")

personne1.dire_bonjour()


class Animal:

    def __init__(self,nom):
        self.nom = nom
    
    def crier(self):
        print(f"{self.nom} fait un bruit")

animal = Animal("Chien")

animal.crier()