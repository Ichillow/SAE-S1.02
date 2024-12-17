import sys
sys.path.append("./")

import random

from ordi.ordi_struct import OrdiMorpion


def ordi_morpion_facile(ordi: OrdiMorpion, grille: list[list[str]]) -> list[list[str]]:
    """
    Cette fonction permet de jouer un tour de jeu pour l'ordinateur en mode facile.

    Args:
        ordi (OrdiMorpion): L'ordinateur qui joue.
        grille (list): La grille de jeu.

    Returns:
        grille (list): La grille de jeu après le tour de jeu.
    """

    #Déclaration des variables
    choixLigne: int
    choixColonne: int

    #Choix aléatoire de la ligne et de la colonne
    choixLigne = random.randint(0, 2)
    choixColonne = random.randint(0, 2)

    #Vérification de la case choisie
    while grille[choixLigne][choixColonne] != " ":
        choixLigne = random.randint(0, 2)
        choixColonne = random.randint(0, 2)
    
    #Mise à jour de la grille
    grille[choixLigne][choixColonne] = ordi.signe

    return grille