# règles spéciales (poison, exhaust...)

from .weights import (
    W_EXHAUST,
    W_FRAILTY,
    W_SELF_DAMAGE,
    W_ENERGY_GAIN,
    W_COST_REDUCTION,
    W_VULNERABILITY,
    W_WEAK,
    W_STRENGTH,
    W_DMG_ALL,
    W_STRENGTH_SCALING,
    W_BLOCK_IF_ENEMY_ATTACKS,
    W_UPGRADE_BONUS
)

EFFECT_WEIGHTS = {
    "exhaust": W_EXHAUST,
    "self_damage": W_SELF_DAMAGE,
    "energy_gain": W_ENERGY_GAIN,
    "cost_reduction": W_COST_REDUCTION,
    "vulnerability": W_VULNERABILITY,
    "weak": W_WEAK,
    "strength": W_STRENGTH,
    "frailty": W_FRAILTY,
    "damage_all": W_DMG_ALL,
    "strength_scaling": W_STRENGTH_SCALING,
    "block_if_enemy_attacks": W_BLOCK_IF_ENEMY_ATTACKS,
    "upgrade_bonus": W_UPGRADE_BONUS
}

def compute_effect_bonus(card):
    '''
    Calcule les bonus/malus de la carte en fonction de ses effets spéciaux (poison, exhaust...).
    il faudra le déplacer dans effects ainsi que le poids
    '''
    bonus = 0

    effects = card.effects or {}
    # print("compute_effect_bonus - effects", effects)

    for effect_name, weight in EFFECT_WEIGHTS.items():
        if effect_name in effects:
            count = effects.get(effect_name, 0)
            bonus += weight * count

    return bonus
