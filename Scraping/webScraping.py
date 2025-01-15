import requests
from bs4 import BeautifulSoup
import pandas as pd

# En-têtes pour simuler un navigateur
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

# Initialisation d'une liste pour stocker les données
data = []

keywords = ["ordinateur"]  # Liste des produits à scraper

# Parcourir plusieurs pages (exemple avec une structure fictive)
for keyword in keywords:
    for page in range(1, 5):  # Pages 1 à 4
        url = f"https://www.amazon.fr/s?k={keyword}&page={page}"
        response = requests.get(url, headers=headers)  # Utilisation de `headers`
        
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            products = soup.find_all("div", class_="s-result-item")
            
            for product in products:
                title = product.find("span", class_="a-size-medium")
                price = product.find("span", class_="a-price-whole")
                
                if title and price:
                    data.append({
                        "Mot-clé": keyword,
                        "Titre": title.get_text(strip=True),
                        "Prix": price.get_text(strip=True),
                    })
        else:
            print(f"Erreur: {response.status_code}")

# Sauvegarde dans un fichier CSV
if data:  # Vérifie qu'il y a des données à sauvegarder
    df = pd.DataFrame(data)
    df.to_csv("produits_amazon.csv", index=False)
    print("Données sauvegardées dans 'produits_amazon.csv'")
else:
    print("Aucune donnée extraite.")
