from domain.models.card import Card

def compute_playability(card: Card, deck_stats: dict) -> float:
    if card.name == "Clash":
        if deck_stats:
            attack_ratio = deck_stats["attack_count"] / deck_stats["size"] if deck_stats["size"] else 0
            return attack_ratio
        else:
            return 0.5  # Valeur par défaut si les statistiques du deck ne sont pas disponibles

    return 1.0