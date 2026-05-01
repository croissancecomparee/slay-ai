from domain.models.card import Card

from app.services.scoring.synergy_weights import SYNERGY_WEIGHTS

def compute_synergy_bonus(card: Card, deck_stats: dict):
    '''
    Calcule le bonus de synergie d'une carte en fonction des statistiques du deck (types de cartes, énergies, etc.).
    '''
    synergy_bonus = 0
    if deck_stats is None:
        return 0
    
    deck_tags  = deck_stats.get('tags', {})

    for tag in card.tags or []:
        if tag not in SYNERGY_WEIGHTS:
            continue
        if tag in SYNERGY_WEIGHTS:
            for synergy_type, weight in SYNERGY_WEIGHTS[tag].items():
                # basé sur les types de cartes dans le deck
                if synergy_type in deck_stats:
                    value = deck_stats[synergy_type]
                    synergy_bonus += weight * value
                
                # basé sur les tags présents dans le deck
                elif synergy_type in deck_tags:
                    value = deck_tags[synergy_type]
                    synergy_bonus += weight * value

    # on s'en occupera après
    # # Bonus pour les cartes qui bénéficient des types de cartes majoritaires dans le deck
    # if card.type_card in deck_stats['type_distribution']:
    #     synergy_bonus += deck_stats['type_distribution'][card.type_card] * 0.1

    # # Bonus pour les cartes qui bénéficient des énergies majoritaires dans le deck
    # # on voudrait avoir une distribution de type gaussienne centrée sur la moyenne des énergies du deck
    # for energy in card.get('energy_cost', []):
    #     if energy in deck_stats['energy_distribution']:
    #         synergy_bonus += deck_stats['energy_distribution'][energy] * 0.05

    return round(synergy_bonus, 2)