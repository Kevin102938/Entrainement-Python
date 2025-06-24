from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Insérez votre clé API OpenWeatherMap ici
API_KEY = 'eb22fb7f8520ebbe006b6e88e6075d79'

@app.route('/api/weather', methods=['GET'])
def get_weather():
    # Obtenir le paramètre de requête 'city' (par ex., ?city=Paris)
    city = request.args.get('Paris')
    if not city:
        return jsonify({"error": "Veuillez fournir le paramètre 'city' dans la requête."}), 400

    # URL de l'API OpenWeatherMap
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric&lang=fr"

    # Faire une requête GET vers OpenWeatherMap
    response = requests.get(weather_url)
    if response.status_code == 200:  # Succès
        weather_data = response.json()
        city_name = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]
        
        # Construire une réponse simple
        return jsonify({
            "ville": city_name,
            "température": f"{temperature}°C",
            "condition": weather_description
        })
    elif response.status_code == 404:  # Ville non trouvée
        return jsonify({"error": "Ville non trouvée. Merci de vérifier le nom de la ville."}), 404
    else:  # Autres erreurs
        return jsonify({"error": "Erreur lors de la récupération des données météo."}), 500

# Démarrer le serveur
if __name__ == '__main__':
    app.run(debug=True)