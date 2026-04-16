import requests

BASE_URL = "http://localhost:8000"

def get_all_cards():
    return requests.get(f"{BASE_URL}/cards").json()

def get_card(name):
    return requests.get(f"{BASE_URL}/cards/{name}").json()

def analyze_deck(deck):
    return requests.post(f"{BASE_URL}/deck/analyze", json=deck).json()