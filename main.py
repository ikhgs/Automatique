from flask import Flask, request, jsonify
import requests
from dotenv import load_dotenv
import os

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Clés API et URL de base
TEXTGEARS_KEY = os.getenv('TEXTGEARS_KEY')
GRAMMAR_URL = 'https://api.textgears.com/grammar'
SPELLING_URL = 'https://api.textgears.com/spelling'

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_text():
    # Récupérer le texte et la langue depuis le JSON de la requête
    data = request.json
    text = data.get('text', '')
    language = data.get('language', 'fr-FR')
    
    # Vérifier la grammaire
    grammar_params = {
        'key': TEXTGEARS_KEY,
        'text': text,
        'language': language
    }
    grammar_response = requests.get(GRAMMAR_URL, params=grammar_params)
    grammar_result = grammar_response.json()
    
    # Vérifier l'orthographe
    spelling_params = {
        'key': TEXTGEARS_KEY,
        'text': text,
        'language': language
    }
    spelling_response = requests.get(SPELLING_URL, params=spelling_params)
    spelling_result = spelling_response.json()
    
    # Combine les résultats et les retourner
    result = {
        'grammar': grammar_result,
        'spelling': spelling_result
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
  
