# compute card score

from .weights import (
    W_DAMAGE,
    W_BLOCK,
    W_DRAW,
    W_COST,
)

from .effects import compute_effect_bonus

from .types import TYPE_BONUS


def compute_absolute_card_score(card):
    '''
    Calcul le score absolu d'une carte en fonction de ses effets, stats et de son coût.
    '''

    damage = card.get('damage', 0)
    block = card.get('block', 0)
    draw = card.get('draw', 0)
    cost = card.get('cost', 1)

    raw_score = (
        W_DAMAGE * damage +
        W_BLOCK * block +
        W_DRAW * draw 
    )

    raw_score += compute_effect_bonus(card)

    raw_score += TYPE_BONUS.get(card['type'], 0)

    score = raw_score / (1 + cost * W_COST)

    return round(score, 2)

def compute_synergy_bonus(card, deck_stats):
    '''
    Calcule le bonus de synergie d'une carte en fonction des statistiques du deck (types de cartes, énergies, etc.).
    '''
    synergy_bonus = 0

    # Bonus pour les cartes qui bénéficient des types de cartes majoritaires dans le deck
    if card['type'] in deck_stats['type_distribution']:
        synergy_bonus += deck_stats['type_distribution'][card['type']] * 0.1

    # Bonus pour les cartes qui bénéficient des énergies majoritaires dans le deck
    for energy in card.get('energy_cost', []):
        if energy in deck_stats['energy_distribution']:
            synergy_bonus += deck_stats['energy_distribution'][energy] * 0.05

    return round(synergy_bonus, 2)