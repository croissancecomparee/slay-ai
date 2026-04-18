# règles spéciales (poison, exhaust...)

from .weights import (
    W_EXHAUST,
    W_FRAILTY,
    W_SELF_DAMAGE,
    W_ENERGY_GAIN,
    W_COST_REDUCTION,
    W_VULNERABILITY,
    W_WEAKNESS,
    W_STRENGTH,
    W_DMG_ALL,
)

def compute_effect_bonus(card):
    '''
    Calcule les bonus/malus de la carte en fonction de ses effets spéciaux (poison, exhaust...).
    il faudra le déplacer dans effects ainsi que le poids
    '''
    bonus = 0

    if "exhaust" in card["tags"]:
        bonus += W_EXHAUST  # léger bonus pour les cartes qui s'épuisent

    if "self_damage" in card["tags"]:
        bonus += W_SELF_DAMAGE  # malus pour les cartes qui infligent des dégâts à soi-même

    if "energy_gain" in card["tags"]:
        bonus += W_ENERGY_GAIN  # bonus pour les cartes qui génèrent de l'énergie

    if "cost_reduction" in card["tags"]:
        bonus += W_COST_REDUCTION  # bonus pour les cartes qui réduisent le coût d'autres cartes

    if "vulnerability" in card["tags"]:
        bonus += W_VULNERABILITY  # bonus pour les cartes qui appliquent la vulnérabilité

    if "weakness" in card["tags"]:
        bonus += W_WEAKNESS  # bonus pour les cartes qui appliquent la faiblesse

    if "strength" in card["tags"]:
        bonus += W_STRENGTH  # bonus pour les cartes qui appliquent la force

    if "frailty" in card["tags"]:
        bonus += W_FRAILTY  # bonus pour les cartes qui appliquent la fragilité

    if "damage_all" in card["tags"]:
        bonus += W_DMG_ALL  # bonus pour les cartes qui infligent des dégâts à tous les ennemis

    return bonus
