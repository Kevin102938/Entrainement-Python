import requests

# URL de l'endpoint de l'API
url = "https://jsonplaceholder.typicode.com/posts"

# Envoyer une requête GET
response = requests.get(url)

# Vérifier le statut de la réponse
if response.status_code == 200:  # 200 = Succès
    data = response.json()  # Convertir la réponse en format JSON
    # Afficher les 3 premiers posts
    for post in data[:3]:
        print(f"ID: {post['id']}, Title: {post['title']}")
else:
    print("Erreur lors de la requête :", response.status_code)
