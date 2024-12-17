import sys
sys.path.append("./")

from ordi.ordi_struct import OrdiDevinette1, OrdiDevinette2

def ordi_cherche_devinettes_facile(ordi: OrdiDevinette1, limite: int, réponse: int) -> None:
    """
    Cette fonction permet de jouer au jeu de la devinette avec l'ordinateur en mode facile.

    Args:
        ordi (OrdiDevinette1): L'ordinateur qui joue.
        limite (int): La limite de la devinette.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    #Déclaration des variables
    proposition: int
    gagne: bool

    #Initialisation des variables
    gagne = False

    #Début du jeu
    while not gagne:
        proposition = ordi.proposer_nombre(limite)
        print(f"L'ordinateur propose : {proposition}")
        gagne = ordi.verifier_nombre(proposition)

    return