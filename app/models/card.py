class Card:
    '''
    Classe de base pour les cartes du jeu Slay the Spire. Chaque carte a un nom, un coût en énergie, des dégâts, du bloc, des cartes à piocher et un type de carte (attaque, compétence, pouvoir).
    Les cartes peuvent être utilisées par le joueur pour infliger des dégâts aux ennemis, se protéger contre les attaques ennemies, ou piocher des cartes supplémentaires.
    Les cartes peuvent également avoir des effets spéciaux, comme infliger des dégâts supplémentaires si le joueur a déjà joué une carte d'attaque ce tour-ci, ou donner un bonus de bloc si le joueur a déjà joué une carte de compétence ce tour-ci.
    '''
    def __init__(
        self,
        name:str,
        cost: int,
        damage: int=0, 
        block:int=0,
        draw:int=0,
        type_card:str=None, #attack, skill, power
        tags:list[str]=None, # peut-être doublon. permet d'ajouter des tags pour les synergies et archétype (ex: strength_scaling, poison, etc.)
        effects: dict=None, #pour les effets spéciaux comme strength_scaling, poison, etc.  
        character:str=None, #ironclad, silent, defect...
        rarity:str=None, #starter,common, uncommon, rare
        description:str=None,
        upgraded: dict=None,
    ):
        '''
        Initialise une carte avec les paramètres donnés.
        '''
        self.name = name
        self.cost = cost
        self.damage = damage
        self.block = block
        self.draw = draw
        self.type_card = type_card
        self.tags = tags
        self.effects = effects
        self.character = character
        self.rarity = rarity
        self.description = description
        self.upgraded = upgraded

   