temps = int(input("Entez un temps en secondes : "))
 
heures =  temps // 3600
minutes = (temps % 3600) // 60
secondes = temps % 60

print(f"{temps} secondes correspond à {heures}h, {minutes}min et {secondes}s.")



# def convertir_secondes(secondes):
#     heures = secondes // 3600  # Diviser par 3600 pour obtenir les heures
#     minutes = (secondes % 3600) // 60  # Récupérer le reste pour les minutes
#     secondes_restantes = secondes % 60  # Récupérer les secondes restantes
#     return heures, minutes, secondes_restantes

# secondes = int(input("Entrez un nombre de secondes : "))

# heures, minutes, secondes_restantes = convertir_secondes(secondes)

# print(f"{secondes} secondes correspondent à {heures} heures, {minutes} minutes et {secondes_restantes} secondes.")
