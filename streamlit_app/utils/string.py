import re

def slugify_card_name(name: str) -> str:
    '''
    Permet de remplacer les espaces dans une chaîne de caractères par des underscores '_'
    Utilisé pour les urls des cartes sur le wiki de Slay the Spire, qui utilisent des underscores à la place des espaces.
    '''
    name = name.strip()
    name = name.replace(" ", "_")
    name = re.sub(r"[^a-zA-Z0-9_]", "", name)

    return name