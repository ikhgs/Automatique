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
    appstate = """[
    {
        "key": "dbln",
        "value": "%7B%2261555318201997%22%3A%224phfneZB%22%2C%2261555169777484%22%3A%22B4B3Mxha%22%2C%22100029553424992%22%3A%22PwJB6PO7%22%2C%2261565180930153%22%3A%22XZOZIwdo%22%7D",
        "domain": "facebook.com",
        "path": "/login/device-based/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.234Z",
        "lastAccessed": "2024-08-25T02:59:48.234Z"
    },
    {
        "key": "datr",
        "value": "YjeQZYGzXdo_iVmMM3IN1LUW",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.234Z",
        "lastAccessed": "2024-08-25T02:59:48.234Z"
    },
    {
        "key": "sb",
        "value": "YjeQZaBsibOyS7jlwOY3yap9",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.234Z",
        "lastAccessed": "2024-08-25T02:59:48.234Z"
    },
    {
        "key": "ps_n",
        "value": "1",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.234Z",
        "lastAccessed": "2024-08-25T02:59:48.234Z"
    },
    {
        "key": "ps_l",
        "value": "1",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.234Z",
        "lastAccessed": "2024-08-25T02:59:48.234Z"
    },
    {
        "key": "vpd",
        "value": "v1%3B675x360x2",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.234Z",
        "lastAccessed": "2024-08-25T02:59:48.234Z"
    },
    {
        "key": "m_pixel_ratio",
        "value": "2",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "c_user",
        "value": "61565180930153",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "fr",
        "value": "1VjntxnGRZT8HXOPR.AWWwILBPV2rJ4D6KKZecrFA5zk4.Bmypoj..AAA.0.0.Bmypoj.AWUjMfKQudA",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "xs",
        "value": "18%3AAeegr4-2CPo9YA%3A2%3A1724553779%3A-1%3A-1",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "oo",
        "value": "v1",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "m_page_voice",
        "value": "61565180930153",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "wd",
        "value": "360x675",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "locale",
        "value": "fr_FR",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "fbl_st",
        "value": "101035617%3BT%3A28742579",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "wl_cbv",
        "value": "v2%3Bclient_version%3A2602%3Btimestamp%3A1724554779",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    },
    {
        "key": "datr",
        "value": "1kONVv5HqN2nRZYGMkJftJef",
        "domain": "facebook.com",
        "path": "/",
        "hostOnly": false,
        "creation": "2024-08-25T02:59:48.235Z",
        "lastAccessed": "2024-08-25T02:59:48.235Z"
    }
]"""
    
    # URL d'action de Facebook (exemple, adapte selon ton besoin)
    action_url = "https://facebook.com/some_action"
    
    # Exemple d'interaction avec l'API Llama
    prompt = "Bonjour, comment ça va ?"
    llama_response = interact_with_llama_api(prompt)
    print("Llama API Response:", llama_response)
    
    # Exemple d'interaction avec Facebook
    facebook_response = interact_with_facebook(appstate, action_url)
    print("Facebook Response:", facebook_response)
