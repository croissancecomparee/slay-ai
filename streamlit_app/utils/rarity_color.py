def get_rarity_color(rarity):
    return {
        "starter": "#ffffff",   # blanc
        "common": "#9e9e9e",    # gris
        "uncommon": "#88bfec",      # bleu
        "rare": "#f3bb21",      # orange
        "curse": "#9c27b0",      # violet
        "quest": "#ec9513",      # orange foncé
    }.get(rarity, "white")