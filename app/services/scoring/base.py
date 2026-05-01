from domain.models.card import Card

from app.services.scoring.engine import compute_absolute_card_score
from app.services.scoring.synergy import compute_synergy_bonus
from app.services.scoring.playability import compute_playability

def compute_card_score(card: Card, deck_stats: dict) -> float:
    '''
    Calcule le score d'une carte en fonction de ses caractéristiques et des statistiques du deck.
    '''
    base_score = card.rarity * 10  # Score de base basé sur la rareté
    base_score = compute_absolute_card_score(card)  # Score absolu basé sur les stats et effets
    synergy_bonus = compute_synergy_bonus(card, deck_stats)  # Bonus de synergie
    playability_score = compute_playability(card, deck_stats)  # Score de jouabilité

    total_score = base_score * playability_score + synergy_bonus
    return round(total_score, 2)