import requests

BASE_URL = "http://localhost:8000"

def get_all_cards():
    return requests.get(f"{BASE_URL}/cards").json()

def get_card(name):
    return requests.get(f"{BASE_URL}/cards/{name}").json()

def analyze_deck(deck):
    return requests.post(f"{BASE_URL}/deck/analyze", json=deck).json()

def get_card_score(name):
    '''
    retourne les donées sous forme:
    {
        "score": 42.0
    }
    '''
    response = requests.get(f"{BASE_URL}/cards/{name}/score")
    if response.status_code != 200:
        return None
    return response.json()