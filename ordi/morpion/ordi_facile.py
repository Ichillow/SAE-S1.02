import sys
sys.path.append("./")

import random

from ordi.ordi_struct import JoueurMorpion


def ordi_morpion_facile(ordi: JoueurMorpion, grille: list[list[str]]) -> list[list[str]]:
    """
    Cette fonction permet de jouer un tour de jeu pour l'ordinateur en mode normal.

    Args:
        ordi (OrdiMorpion): L'ordinateur qui joue.
        grille (list): La grille de jeu.

    Returns:
        grille (list): La grille de jeu après le tour de jeu.
    """

    #Déclaration des variables
    choixLigne: int
    choixColonne: int
    print("Test 1")

    #Choix aléatoire de la ligne et de la colonne
    choixLigne = random.randint(0, 2)
    choixColonne = random.randint(0, 2)

    print("Test 2")

    #Vérification de la case choisie
    while grille[choixLigne][choixColonne] != " ":
        print("Case déjà occupée")
        choixLigne = random.randint(0, 2)
        choixColonne = random.randint(0, 2)
    
    #Mise à jour de la grille
    grille[choixLigne][choixColonne] = ordi.signe
    print(f"L'ordinateur a joué en {choixLigne+1}, {choixColonne+1}")

    return grille