def get_card_stat(card, stat, use_upgraded):
    '''
    Pour une carte donnée, retourne la valeur d'un stat (damage, block, draw) en prenant en compte si l'on veut utiliser la version améliorée de la carte ou non.
    '''
    if use_upgraded and card.get("upgraded") and stat in card["upgraded"]:
        return card["upgraded"][stat]
    return card.get(stat, 0)