from pydantic import BaseModel, Field

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
    tags: list[str] = Field(default_factory=list)
    character: str | None = None
    rarity: str | None = None
    description: str | None = None
    effects: dict | None = None
    upgraded: dict | None = None

    # def to_domain(self):
    #     return Card(**self.model_dump())

    def to_domain(self):
        return Card(
            name=self.name,
            cost=self.cost,
            damage=self.damage,
            block=self.block,
            draw=self.draw,
            type_card=self.type_card,
            tags=self.tags or [],
            effects=self.effects or {},
            character=self.character,
            rarity=self.rarity,
            description=self.description,
            upgraded=self.upgraded or {},
        )