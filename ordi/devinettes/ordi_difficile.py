########################################################################################
#Ce fichier contient l'ordinateur difficile du jeu des devinettes
########################################################################################

import sys, random
sys.path.append("./")

from ordi.ordi_struct import JoueursDevinette

def ordi_cherche_difficile(limite: int, proposition: int, borne_min: int, borne_max: int, reponse: int) -> tuple[int, int, int]:
    """
    Cette fonction permet de jouer au jeu de la devinette avec l'ordinateur en mode difficile.

Args:
        limite (int): La limite supérieure du jeu.
        proposition (int): Dernière proposition du bot.
        borne_min (int): La borne inférieure de l'intervalle. (par défaut : 1)
        borne_max (int): La borne supérieure de l'intervalle. (par défaut : None, sera initialisé à limite)
        réponse (int): La réponse donnée par l'utilisateur (1 = trop petit, 2 = trop grand, 3 = trouvé).

    Returns:
        tuple: (proposition (int), borne_min (int), borne_max (int)) - La nouvelle proposition et les bornes mises à jour.
    """

    # Mise à jour des bornes en fonction de la réponse
    if reponse == 1:  # Trop petit
        borne_min = max(borne_min, proposition + 1)
    elif reponse == 2:  # Trop grand
        borne_max = min(borne_max, proposition - 1)

    # Nouvelle proposition basée sur la recherche dichotomique
    proposition = (borne_min + borne_max) // 2

    return proposition, borne_min, borne_max

