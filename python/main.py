import requests
from requests.cookies import cookiejar_from_dict

# URL de l'API de Facebook pour envoyer des messages
SEND_MESSAGE_URL = 'https://www.facebook.com/messages/send/'

# Cookies de session
COOKIES = {
    'dbln': '%7B%22100029553424992%22%3A%22KzkiEt2X%22%7D',
    'datr': 'oeO8ZvmLSKkzwUU4WU99_0hW',
    'sb': 'oeO8ZnwVcTyLfyJYBVb61qu8',
    'ps_l': '1',
    'ps_n': '1',
    'locale': 'fr_FR',
    'vpd': 'v1%3B675x360x2',
    'c_user': '100029553424992',
    'xs': '8%3AnNSAkz-nqv1HrQ%3A2%3A1724531539%3A-1%3A9694',
    'oo': 'v1',
    'm_page_voice': '100029553424992',
    'm_pixel_ratio': '2',
    'x-referer': 'eyJyIjoiLyIsImgiOiIvIiwicyI6Im0ifQ%3D%3D',
    'wd': '360x675',
    'fbl_st': '100731513%3BT%3A28742615',
    'wl_cbv': 'v2%3Bclient_version%3A2602%3Btimestamp%3A1724556919'
}

# Fonction pour envoyer un message
def envoyer_message(destinataire_id, message_text):
    session = requests.Session()
    session.cookies = cookiejar_from_dict(COOKIES)

    # Préparer les données du message
    form_data = {
        'to': destinataire_id,
        'body': message_text
    }

    # Envoyer le message
    response = session.post(SEND_MESSAGE_URL, data=form_data)
    
    if response.status_code == 200:
        print(f"Message envoyé à {destinataire_id}: {message_text}")
    else:
        print(f"Erreur lors de l'envoi du message: {response.status_code} {response.text}")

# Exemple d'utilisation
def main():
    destinataire_id = '100029553424992'  # ID du destinataire
    message_text = "Bonjour, je suis un Chatbot."
    envoyer_message(destinataire_id, message_text)

if __name__ == "__main__":
    main()
