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

    damage = card.damage or 0
    block = card.block or 0
    draw = card.draw or 0
    cost = card.cost or 1

    raw_score = (
        W_DAMAGE * damage +
        W_BLOCK * block +
        W_DRAW * draw 
    )

    raw_score += compute_effect_bonus(card)

    raw_score += TYPE_BONUS.get(card.type_card, 0)

    score = raw_score / (1 + cost * W_COST)

    return round(score, 2)
