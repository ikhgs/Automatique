import requests

# Fonction pour interagir avec l'API ChatGPT
def interact_with_llama_api(prompt):
    # Encoder le prompt pour l'utiliser dans l'URL de l'API
    encoded_prompt = requests.utils.quote(prompt)
    
    # Construire l'URL avec le prompt encodé
    api_url = f"https://llama3-70b.vercel.app/api?ask={encoded_prompt}"
    
    try:
        # Envoyer la requête GET à l'API
        response = requests.get(api_url)
        
        # Vérifier si la réponse est valide
        if response.status_code == 200:
            data = response.json()
            if "response" in data:
                return data["response"]
            else:
                return "No response field found in API response."
        else:
            return f"Failed to fetch data from API. Status code: {response.status_code}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Fonction pour interagir avec Facebook en utilisant AppState
def interact_with_facebook(appstate, action_url):
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Cookie': appstate
    }

    try:
        # Envoyer une requête GET à Facebook en utilisant AppState
        response = requests.get(action_url, headers=headers)
        
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to perform Facebook action. Status code: {response.status_code}"
    
    except Exception as e:
        return f"An error occurred while interacting with Facebook: {str(e)}"

# Exemple d'utilisation combinée
if __name__ == "__main__":
    # Ton AppState ici (assure-toi de le garder sécurisé et privé)
    appstate = "TON_APPSTATE"

    # URL de l'action Facebook (par exemple, vérifier ton profil)
    facebook_url = "https://www.facebook.com/me"

    # Interagir avec Facebook
    facebook_response = interact_with_facebook(appstate, facebook_url)
    print("Facebook Response:", facebook_response)

    # Saisir un prompt pour l'API ChatGPT
    prompt = input("Enter your prompt: ")
    chatgpt_response = interact_with_llama_api(prompt)
    print("API Response:", chatgpt_response)
