from domain.models.card import Card

def compute_synergy_bonus(card: Card, deck_stats: dict):
    '''
    Calcule le bonus de synergie d'une carte en fonction des statistiques du deck (types de cartes, énergies, etc.).
    '''
    synergy_bonus = 0
    if deck_stats is None:
        return 0
    # Bonus pour les cartes qui bénéficient des types de cartes majoritaires dans le deck
    if card.type_card in deck_stats['type_distribution']:
        synergy_bonus += deck_stats['type_distribution'][card.type_card] * 0.1

    # Bonus pour les cartes qui bénéficient des énergies majoritaires dans le deck
    for energy in card.get('energy_cost', []):
        if energy in deck_stats['energy_distribution']:
            synergy_bonus += deck_stats['energy_distribution'][energy] * 0.05

    return round(synergy_bonus, 2)