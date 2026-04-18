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

def get_cards_scores(cards):
    '''
    retourne les donées sous forme:
    {
        "card_name_1": 42.0,
        "card_name_2": 36.5,
        ...
    }
    '''
    response = requests.get(f"{BASE_URL}/cards/scores", json=cards)
    if response.status_code != 200:
        return None
    return response.json()