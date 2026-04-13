# Ici que l'on défini les routes de notre API, c'est à dire les différentes URL que notre API va exposer et les fonctions qui vont être appelées lorsque ces URL sont accédées.
from fastapi import APIRouter
from app.services.card_service.card_api import (
    get_all_cards, 
    get_card_by_name,
)
from app.services.deck_service import analyze_deck

router = APIRouter()

@router.get("/cards")
def get_cards():
    return get_all_cards()

@router.get("/cards/{name}")
def get_card(name: str):
    return get_card_by_name(name)

@router.post("/deck/analyze")
def analyze_deck(deck: list[str]):
    return analyze_deck(deck)