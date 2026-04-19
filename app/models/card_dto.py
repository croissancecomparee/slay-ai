from pydantic import BaseModel

from domain.models.card import Card
from typing import Optional


class CardDTO(BaseModel):
    '''
    Classe Data Transfer Object pour les cartes du jeu Slay the Spire. Cette classe est utilisée pour transférer les données des cartes entre les différentes couches de l'application, comme entre la base de données et l'API, ou entre l'API et le frontend.
    '''
    name: str
    cost: int
    damage: int
    block: int
    draw: int
    type_card: str
    tags: list[str]
    character: str
    rarity: str
    description: str
    effects: Optional[dict] = None
    upgraded: Optional[dict] = None

    def to_domain(self):
        return Card(**self.model_dump())