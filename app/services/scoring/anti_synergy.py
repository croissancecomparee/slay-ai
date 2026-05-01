from domain.models.card import Card

def compute_anti_synergy_penalty(card: Card, deck_stats: dict) -> float:
    '''
    Calcule la pénalité d'anti-synergie d'une carte en fonction des statistiques du deck (types de cartes, énergies, etc.).
    '''
    anti_synergy_penalty = 0
    if deck_stats is None:
        return 0
    
    tags = card.tags or []

    # Clash
    if "clash" in tags:
        if deck_stats:
            attack_ratio = deck_stats["attack_count"] / deck_stats["size"] if deck_stats["size"] else 0
            anti_synergy_penalty += (1 - attack_ratio) * 5  # Pénalité plus élevée si le ratio d'attaques est faible
        else:
            anti_synergy_penalty += 2.5  # Pénalité par défaut si les statistiques du deck ne sont pas disponibles

    if "exhaust" in tags:
        if deck_stats["size"] > 20:
            anti_synergy_penalty += (deck_stats["size"] - 20) * 0.1  # Pénalité qui augmente avec la taille du deck

    if "self_damage" in tags:
        if deck_stats["attack_count"] < 5:
            anti_synergy_penalty += (5 - deck_stats["attack_count"]) * 0.2  # Pénalité plus élevée si le nombre d'attaques est faible
            sustain = deck_stats.get("heal", 0)
            if sustain < 5:
                anti_synergy_penalty += (5 - sustain) * 0.1  # Pénalité plus élevée si le sustain est faible

    return round(anti_synergy_penalty, 2)