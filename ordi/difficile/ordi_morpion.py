import sys
sys.path.append("./")

import random

from ordi.ordi_struct import OrdiMorpion


def ordi_morpion_facile(ordi: OrdiMorpion, grille: list) -> list:
    """
    Cette fonction permet de jouer un tour de jeu pour l'ordinateur en mode facile.

    Args:
        ordi (OrdiMorpion): L'ordinateur qui joue.
        grille (list): La grille de jeu.

    Returns:
        grille (list): La grille de jeu après le tour de jeu.
    """

    random.rand