import sys
sys.path.append("./")

import random



def ordi_allumettes_facile(nbrAllumettes: int) -> int:
    """
    Cette fonction permet à l'ordinateur de jouer un tour de jeu en mode facile.

    Args:
        nbrAllumettes (int): Le nombre d'allumettes restantes.

    Returns:
        nbrAllumettes (int): Le nombre d'allumettes restantes après le tour de jeu.
    """

    #Déclaration des variables
    choix: int

    #Choix aléatoire du nombre d'allumettes à retirer
    choix = random.randint(1, 3)

    #Vérification du choix
    while choix > nbrAllumettes:
        choix = random.randint(1, nbrAllumettes)

    return choix