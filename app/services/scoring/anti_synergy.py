from domain.models.card import Card

def compute_anti_synergy_penalty(card: Card, deck_stats: dict) -> float:
    '''
    Calcule la pénalité d'anti-synergie d'une carte en fonction des statistiques du deck (types de cartes, énergies, etc.).
    '''
    anti_synergy_penalty = 0
    if deck_stats is None or len(deck_stats) == 0:
        return 0
    
    tags = card.tags or []

    attack_count = deck_stats.get("attack_count", 0)
    size = deck_stats.get("size", 0)
    # Clash
    if "clash" in tags:
        if len(deck_stats) > 0:
            attack_ratio = attack_count / size if size else 0
            anti_synergy_penalty += (1 - attack_ratio) * 5  # Pénalité plus élevée si le ratio d'attaques est faible
        else:
            anti_synergy_penalty += 2.5  # Pénalité par défaut si les statistiques du deck ne sont pas disponibles

    if "exhaust" in tags:
        if size > 20:
            anti_synergy_penalty += (size - 20) * 0.1  # Pénalité qui augmente avec la taille du deck

    if "self_damage" in tags:
        if attack_count < 5:
            anti_synergy_penalty += (5 - attack_count) * 0.2  # Pénalité plus élevée si le nombre d'attaques est faible
            sustain = deck_stats.get("heal", 0)
            if sustain < 5:
                anti_synergy_penalty += (5 - sustain) * 0.1  # Pénalité plus élevée si le sustain est faible

    return round(anti_synergy_penalty, 2)