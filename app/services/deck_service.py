from app.services.card_service.card_api import get_card_by_name


def analyze_deck_service(deck: list[str]):
    '''
    Fonction qui prend en entrée une liste de noms de cartes (le deck du joueur) 
    et qui retourne un dictionnaire contenant des statistiques sur ce deck, 
    comme:
    - le nombre de cartes,
    - le nombre de cartes d'attaque, de compétence et de pouvoir,
    - la moyenne de coût en énergie,
    - les dégâts totaux,
    - le bloc total,
    - le nombre de cartes à piocher,
    - et les tags présents dans le deck.

    Attention à la virgule à la fin pour les fichiers json
    '''
    stats = {
        "size": len(deck),
        "attack_count": 0,
        "skill_count": 0,
        "power_count": 0,
        "avg_cost": 0,
        "total_damage": 0,
        "total_block": 0,
        "draw_count": 0,
        "tags": {}
    }

    total_cost = 0

    for card_name in deck:
        card = get_card_by_name(card_name)

        if not card:
            continue

        # type
        if card["type_card"] == "attack":
            stats["attack_count"] += 1
        elif card["type_card"] == "skill":
            stats["skill_count"] += 1
        elif card["type_card"] == "power":
            stats["power_count"] += 1

        # stats
        stats["total_damage"] += card.get("damage", 0)
        stats["total_block"] += card.get("block", 0)
        stats["draw_count"] += card.get("draw", 0)

        total_cost += card.get("cost", 0)

        # tags (synergies)
        for tag in card.get("tags", []):
            stats["tags"][tag] = stats["tags"].get(tag, 0) + 1

    # moyenne coût
    if stats["size"] > 0:
        stats["avg_cost"] = round(total_cost / stats["size"], 2)

    return stats