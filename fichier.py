import json
import os

fichier_path = "fichier/donnees.json"

# Lire le contenu du fichier avec gestion d'erreur
try:
    with open(fichier_path, "r") as fichier:
        contenu = json.load(fichier)  # Charge les données dans un dictionnaire
        print("Contenu du fichier :", contenu)
except json.JSONDecodeError as e:
    print(f"Erreur de décodage JSON : {e}")
except FileNotFoundError:
    print(f"Le fichier {fichier_path} n'existe pas.")
except Exception as e:
    print(f"Une erreur est survenue : {e}")

