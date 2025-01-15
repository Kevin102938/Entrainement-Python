mots = ["un", "chat", "mange", "le", "poisson"]
sortie = ["chat", "mange", "poisson"]

garder = [x for x in mots if len(x)>3]
print(garder)