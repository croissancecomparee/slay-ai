# compute card score

from .weights import W_DAMAGE, W_BLOCK, W_DRAW, W_COST


def compute_effect_bonus(card):
    '''
    Calcule les bonus/malus de la carte en fonction de ses effets spéciaux (poison, exhaust...).
    '''
    bonus = 0

    if "exhaust" in card["tags"]:
        bonus += 0.2  # léger bonus pour les cartes qui s'épuisent

    if "self_damage" in card["tags"]:
        bonus -= 1.5  # malus pour les cartes qui infligent des dégâts à soi-même

    if "energy_gain" in card["tags"]:
        bonus += 2.0  # bonus pour les cartes qui génèrent de l'énergie

    if "cost_reduction" in card["tags"]:
        bonus += 1.0  # bonus pour les cartes qui réduisent le coût d'autres cartes

    return bonus

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