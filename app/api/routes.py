# Ici que l'on défini les routes de notre API, c'est à dire les différentes URL que notre API va exposer et les fonctions qui vont être appelées lorsque ces URL sont accédées.
from fastapi import APIRouter
from app.models.card import Card
from app.services.card_service.card_api import get_all_cards

router = APIRouter()

@router.get("/cards")
def get_cards():
    return get_all_cards()