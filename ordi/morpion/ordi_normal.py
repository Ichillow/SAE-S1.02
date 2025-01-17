import sys
sys.path.append("./")

from ordi.ordi_struct import JoueurMorpion
from ordi.morpion.ordi_facile import ordi_morpion_facile
from ordi.morpion.ordi_difficile import ordi_morpion_difficile


def ordi_morpion_normal(ordi: JoueurMorpion, grille: list[list[str]], adversaire: JoueurMorpion) -> list[list[str]]:
    """
    Cette fonction permet de jouer un tour de jeu pour l'ordinateur en mode normal.

    Args:
        ordi (OrdiMorpion): L'ordinateur qui joue.
        grille (list): La grille de jeu.

    Returns:
        grille (list): La grille de jeu après le tour de jeu.
    """

    #Un coup sur deux, l'ordinateur joue facile, sinon il joue difficile
    if ordi.nbCoups % 2 == 0:
        grille = ordi_morpion_facile(ordi, grille)
    else:
        grille = ordi_morpion_difficile(ordi, grille, adversaire)
    
    return grille