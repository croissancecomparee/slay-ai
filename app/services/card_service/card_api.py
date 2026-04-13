import json

def get_all_cards():
    with open("app/data/cards.json") as f:
        return json.load(f)