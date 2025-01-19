########################################################################################
#Ce fichier contient l'ordinateur qui va répondre au jeu des devinettes
########################################################################################

import sys, random
sys.path.append("./")

from ordi.ordi_struct import JoueursDevinette


def ordi_réponse(ordi:JoueursDevinette, limite : int, proposition : int, nombre : int, joueur2 : JoueursDevinette) ->tuple[int,int] :
    """
    Cette fonction permet à l'ordinateur de répondre à l'autre joueur dans le jeu de la devinette

    Args:
        ordi (JoueursDevinette): L'ordinateur qui joue.
        limite (int): La limite de la devinette.
        proposition (int): La proposition de l'autre joueur.
        nombre (int): Le nombre à deviner.
        joueur2 (JoueursDevinette): Le joueur qui joue.

    Returns:
        tuple[int,int]: Un tuple contenant le choix de l'ordinateur et le nombre
    """
    #Déclaration des variables
    choix : int 
    choix = 0

    #Choix de l'ordinateur
    if nombre > proposition:
        choix = 1
    elif nombre < proposition and nombre != -1:
        choix = 2
    elif nombre == proposition :
        choix = 3
    elif nombre == -1:
        nombre = random.randint(1,limite)
    else :
        print("Erreur de choix")

    return choix, nombre
