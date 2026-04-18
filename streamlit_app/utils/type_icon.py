def get_type_icon(type_card):
    return {
        "attack": "⚔️",
        "skill": "🛡️",
        "power": "✨",
        "curse": "💀",
        "status": "🔥",
    }.get(type_card, "❓")