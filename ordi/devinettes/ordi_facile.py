import sys, random
sys.path.append("./")

from ordi.ordi_struct import JoueursDevinette

def ordi_cherche_facile(ordi: JoueursDevinette, limite: int, réponse: int, proposition : int) -> int:
    """
    Cette fonction permet de jouer au jeu de la devinette avec l'ordinateur en mode facile.

    Args:
        ordi (OrdiDevinette1): L'ordinateur qui joue.
        limite (int): La limite de la devinette.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    #Déclaration des variables
    trop_grand: bool
    trop_petit: bool

    #Initialisation des variables
    trop_grand = False
    trop_petit = False

    if réponse == 0:
        proposition = random.randint(1, limite)
    elif réponse == 1 :
        trop_petit = True
    else:
        trop_grand = True


    if trop_petit :
        proposition = random.randint(proposition, limite)
    elif trop_grand :
        proposition = random.randint(1, proposition)

    return proposition

