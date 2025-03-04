def convertir_unites():
    print("Bienvenue dans le convertisseur d'unités.")
    print("1 : Kilomètres -> Miles")
    print("2 : Miles -> Kilomètres")
    print("3 : Kilogrammes -> Livres")
    print("4 : Livres -> Kilogrammes")

    choix = int(input("Quel type souhaitez-vous convertir : "))

    match choix:
        case 1:
            km = float(input("Entrez la distance en km : "))
            miles = km * 0.621371
            print(f"{km} km = {miles:2f} miles")
        case 2:
            miles = float(input("Entrez la distance en miles : "))
            km = miles * 1.60934
            print(f"{miles} miles = {km:2f} km")
        case 3:
            kg = float(input("Entrez le poids en kg : "))
            lbs = kg * 2.20462
            print(f"{kg} kg = {lbs:2f} lbs")
        case 4:
            lbs = float(input("Entrez le poids en livres : "))
            kg = lbs * 0.453592
            print(f"{lbs} livres = {kg:2f} Kg")
        case _:
            print("Choix non valide.\n Veuillez entrer un nombre entre 1 et 4.")
            convertir_unites()
            print("\n\n\n")
    
convertir_unites()


