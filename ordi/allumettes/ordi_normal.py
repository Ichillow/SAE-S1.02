import sys
sys.path.append("./")

from ordi.ordi_struct import JoueurAllumettes
from ordi.allumettes.ordi_facile import ordi_allumettes_facile
from ordi.allumettes.ordi_difficile import ordi_allumettes_difficile



def ordi_allumettes_normal(ordi: JoueurAllumettes, nbrAllumettes: int) -> int:
    """
    Cette fonction permet à l'ordinateur de jouer un tour de jeu en mode normal.

    Args:
        ordi (JoueurAllumettes): L'ordinateur qui joue.
        nbrAllumettes (int): Le nombre d'allumettes restantes.

    Returns:
        nbrAllumettes (int): Le nombre d'allumettes restantes après le tour de jeu.
    """

    if ordi.nbCoups % 2 == 0:
        choix = ordi_allumettes_facile(nbrAllumettes)
    else:
        choix = ordi_allumettes_difficile(nbrAllumettes)

    return choix