import qrcode

def generer_qr_code(texte, nom_fichier):
    # Créer le QR Code
    qr = qrcode.QRCode(
        version=1,  # Taille du QR Code (1 à 40, 1 est le plus petit)
        error_correction=qrcode.constants.ERROR_CORRECT_L,  # Niveau de correction d'erreur
        box_size=10,  # Taille des boîtes du QR Code
        border=4,  # Taille de la bordure (minimum 4)
    )
    qr.add_data(texte)  # Ajouter les données (texte, URL, etc.)
    qr.make(fit=True)

    # Générer l'image du QR Code
    image = qr.make_image(fill_color="black", back_color="white")
    
    # Sauvegarder le fichier
    image.save(nom_fichier)
    print(f"QR Code enregistré sous le nom : {nom_fichier}")

# Demander à l'utilisateur un texte ou une URL
texte = input("Entrez le texte ou l'URL à convertir en QR Code : ")

# Nom du fichier à sauvegarder
nom_fichier = input("Entrez le nom du fichier (avec extension .png) : ")

# Générer le QR Code
generer_qr_code(texte, nom_fichier)
