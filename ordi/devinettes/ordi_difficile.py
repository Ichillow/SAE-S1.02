import sys
sys.path.append("./")

from ordi.ordi_struct import JoueursDevinette

from ordi.ordi_struct import JoueursDevinette

def ordi_cherche_difficile(ordi: JoueursDevinette, limite: int, réponse: int, proposition : int) -> int:
    """
    Cette fonction permet de jouer au jeu de la devinette avec l'ordinateur en mode difficile.

    Args:
        ordi (OrdiDevinette1): L'ordinateur qui joue.
        limite (int): La limite de la devinette.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    # Déclaration des variables
    trop_grand: bool
    trop_petit: bool
    borne_inf: int
    borne_sup: int

    # Initialisation des variables
    trop_grand = False
    trop_petit = False
    borne_inf = 1
    borne_sup = limite


    elif réponse == 1 :
        trop_petit = True
    else:
        trop_grand = True


    # Calcul de la nouvelle proposition
    proposition = (borne_inf + borne_sup) // 2

    return proposition

