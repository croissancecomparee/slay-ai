from app.services.card_service.card_api import get_card_by_name
from app.services.scoring.engine import compute_absolute_card_score
from domain.models.card import Card

def analyze_deck_service(deck: list[Card]):
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
    # print("analyze_deck_service - deck", [card.name for card in deck])
    # print("len(deck)", len(deck))
    stats = {
        "size": len(deck),
        "attack_count": 0,
        "skill_count": 0,
        "power_count": 0,
        "avg_cost": 0,
        "total_damage": 0,
        "total_block": 0,
        "draw_count": 0,
        "tags": {},
        "card_scores": [],
        "avg_score": 0,
        "type_distribution": {},
        "energy_distribution": {},
    }

    total_cost = 0

    for card in deck:
        # type
        if card.type_card == "attack":
            stats["attack_count"] += 1
        elif card.type_card == "skill":
            stats["skill_count"] += 1
        elif card.type_card == "power":
            stats["power_count"] += 1

        # stats
        stats["total_damage"] += card.damage or 0
        stats["total_block"] += card.block or 0
        stats["draw_count"] += card.draw or 0

        total_cost += card.cost or 0

        # tags (synergies)
        for tag in card.tags or []:
            stats["tags"][tag] = stats["tags"].get(tag, 0) + 1

        # score
        score = compute_absolute_card_score(card)
        # stats["tags"]["score"] = stats["tags"].get("score", 0) + score
        # stats["score"] = stats["tags"]["score"] / stats["size"] if stats["size"] > 0 else 0 
        stats["card_scores"].append({
            "name": card.name,
            "score": score
        })

    # moyenne coût
    if stats["size"] > 0:
        stats["avg_cost"] = round(total_cost / stats["size"], 2)

    # score moyen
    if stats["card_scores"]:
        avg_score = round(
            sum(c["score"] for c in stats["card_scores"]) / len(stats["card_scores"]),
            2
        )
        stats["avg_score"] = avg_score

    best_card = max(stats["card_scores"], key=lambda c: c["score"], default=None)
    stats["best_card"] = best_card

    worst_card = min(stats["card_scores"], key=lambda c: c["score"], default=None)
    stats["worst_card"] = worst_card

    return stats