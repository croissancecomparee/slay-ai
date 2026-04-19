# Ici que l'on défini les routes de notre API, c'est à dire les différentes URL que notre API va exposer et les fonctions qui vont être appelées lorsque ces URL sont accédées.
from fastapi import APIRouter
from app.services.card_service.card_api import (
    get_all_cards, 
    get_card_by_name,
)
from app.services.scoring.engine import compute_absolute_card_score
from app.services.deck_service import analyze_deck_service

from app.models.card_dto import CardDTO
from domain.models.card import Card


router = APIRouter()

@router.get("/cards")
def get_cards():
    return get_all_cards()

@router.get("/cards/{name}")
def get_card(name: str):
    return get_card_by_name(name)

@router.post("/deck/analyze")
def analyze_deck_route(deck: list[str]):
    return analyze_deck_service(deck)

@router.post("/cards/scores")
def get_cards_scores(cards: list[CardDTO]):
    results = {}
    print("get_cards_scores - cards", cards)
    for card in cards:
        card_domain = card.to_domain()
        print("CARD DOMAIN:", card_domain.__dict__)
        results[card.name] = compute_absolute_card_score(card_domain)
    print("get_cards_scores - results", results)
    return results

@router.get("/cards/{name}/score")
def get_card_score(name: str):
    card = get_card_by_name(name)
    score = compute_absolute_card_score(card)
    return {"score": score}