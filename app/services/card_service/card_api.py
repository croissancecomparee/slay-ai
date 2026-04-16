import json

def get_all_cards():
    '''
    Cette fonction lit le fichier JSON contenant les cartes et retourne une liste de dictionnaires représentant les cartes.
    '''
    with open("app/data/cards.json") as f:
        return json.load(f)
    
def get_card_by_name(name: str):
    '''
    On récupère toutes les cartes, puis on parcourt la liste pour trouver la carte dont le nom correspond à celui donné en paramètre.
    Si on trouve la carte, on la retourne, 
    sinon on retourne None.
    '''
    cards = get_all_cards()
    for card in cards:
        if card["name"].lower() == name.lower():
            return card
    return None