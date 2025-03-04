def calculer_pourboires():
    print("Bienvenue dans le calculateur de pourboires !")
    print("\n")

    # Validation de l'addition
    while True:
        try:
            addition = float(input("Entrez le montant de l'addition : "))
            if addition <= 0:
                print("Le montant de l'addition doit être positif !!")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre valide pour l'addition.")

    # Validation du pourcentage
    while True:
        try:
            pourcentage = float(input("Entrez le pourcentage de pourboire souhaité (par exemple, 10, 15, 20, ...) : "))
            if pourcentage <= 0:
                print("Le pourcentage doit être un nombre positif !!")
                continue
            break
        except ValueError:
            print("Veuillez entrer un pourcentage valide.")

    # Validation du nombre de personnes
    while True:
        try:
            personne = int(input("Combien de personnes partagent l'addition ? "))
            if personne <= 0:
                print("Le nombre de personnes doit être supérieur à 0 !!")
                continue
            break
        except ValueError:
            print("Veuillez entrer un nombre entier valide pour les personnes.")

    # Calculs
    pourboire = (addition * pourcentage) / 100
    total = addition + pourboire
    totalParPersonne = total / personne

    # Résultats
    print(f"\nPourboire : {pourboire:.2f} €")
    print(f"Total à payer : {total:.2f} €")
    if personne > 1:
        print(f"Montant par personne : {totalParPersonne:.2f} €")

# Lancer le programme
calculer_pourboires()
