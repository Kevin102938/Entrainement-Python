import os
from datetime import datetime

# Récupérer le chemin du dossier où se trouve le script
folder_path = os.getcwd()

# Obtenir la date actuelle au format AAAA-MM-JJ
current_date = datetime.now().strftime("%Y-%m-%d")

# Parcourir tous les fichiers du dossier
for filename in os.listdir(folder_path):
    # Vérifier si c'est un fichier .txt (pour ne pas renommer d'autres fichiers par erreur)
    if filename.endswith(".txt") and os.path.isfile(os.path.join(folder_path, filename)):
        # Créer le nouveau nom en ajoutant la date au début
        new_name = f"{current_date}_{filename}"
        
        # Chemin complet pour l'ancien et le nouveau nom
        old_file = os.path.join(folder_path, filename)
        new_file = os.path.join(folder_path, new_name)
        
        # Renommer le fichier
        os.rename(old_file, new_file)

print("Les fichiers .txt ont été renommés avec succès.")
