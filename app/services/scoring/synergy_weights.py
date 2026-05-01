# à revoir, on pourrait faire une fonction qui calcule un score de synergie pour chaque carte en fonction des stats du deck, et ensuite utiliser ce score pour ajuster le score de chaque carte>

SYNERGY_WEIGHTS = {
    "strength_scaling": {
        "buff_power": 3,   # Inflame / Demon Form
        "strength": 0.5,   # cartes qui donnent de la force
        "strength_scaling": 0.1,   # cartes qui gagnent en puissance avec la force
    },
    "block_scaling": {
        "total_block": 0.05,
    },
    "damage_all": {
        "attack_count": 0.2,
    },
    "exhaust": {
        "exhaust": 0.5,
    },
    "vulnerable_scaling": {
        "vulnerability": 2,
        "vulnerable": 0.5,
    },
}