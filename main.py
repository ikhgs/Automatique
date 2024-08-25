import requests

# Fonction pour interagir avec l'API Llama
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

# Fonction pour interagir avec Facebook en utilisant les cookies
def interact_with_facebook(cookies, action_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    
    # Construire le champ Cookie pour la requête
    cookies_header = '; '.join([f"{cookie['key']}={cookie['value']}" for cookie in cookies])
    headers['Cookie'] = cookies_header

    try:
        # Envoyer une requête GET à Facebook en utilisant les cookies
        response = requests.get(action_url, headers=headers)
        
        if response.status_code == 200:
            return response.text
        else:
            return f"Failed to perform Facebook action. Status code: {response.status_code}"
    
    except Exception as e:
        return f"An error occurred while interacting with Facebook: {str(e)}"

# Exemple d'utilisation combinée
if __name__ == "__main__":
    # Cookies Facebook (assurez-vous de les garder sécurisés et privés)
    cookies = [
        {"key": "dbln", "value": "%7B%22100029553424992%22%3A%22KzkiEt2X%22%7D", "domain": "facebook.com", "path": "/login/device-based/", "hostOnly": False},
        {"key": "datr", "value": "oeO8ZvmLSKkzwUU4WU99_0hW", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "sb", "value": "oeO8ZnwVcTyLfyJYBVb61qu8", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "ps_l", "value": "1", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "ps_n", "value": "1", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "locale", "value": "fr_FR", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "vpd", "value": "v1%3B675x360x2", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "c_user", "value": "100029553424992", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "xs", "value": "8%3AnNSAkz-nqv1HrQ%3A2%3A1724531539%3A-1%3A9694", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "oo", "value": "v1", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "m_page_voice", "value": "100029553424992", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "m_pixel_ratio", "value": "2", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "x-referer", "value": "eyJyIjoiLyIsImgiOiIvIiwicyI6Im0ifQ%3D%3D", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "wd", "value": "360x675", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "fbl_st", "value": "100731513%3BT%3A28742615", "domain": "facebook.com", "path": "/", "hostOnly": False},
        {"key": "wl_cbv", "value": "v2%3Bclient_version%3A2602%3Btimestamp%3A1724556919", "domain": "facebook.com", "path": "/", "hostOnly": False}
    ]

    # URL de l'action Facebook (exemple pour vérifier le profil)
    facebook_url = "https://www.facebook.com/me"

    # Interagir avec Facebook
    facebook_response = interact_with_facebook(cookies, facebook_url)
    print("Facebook Response:", facebook_response)

    # Saisir un prompt pour l'API Llama
    prompt = input("Enter your prompt: ")
    chatgpt_response = interact_with_llama_api(prompt)
    print("API Response:", chatgpt_response)
