########################################################################################
#Ce fichier contient l'ordinateur difficile du jeu des devinettes
########################################################################################

import sys
sys.path.append("./")

from ordi.ordi_struct import JoueursDevinette

def ordi_cherche_difficile(ordi : JoueursDevinette, borne_min: int, borne_max: int, limite: int, reponse: int,  proposition: int ) -> tuple[int, int, int]:
    """
    Cette fonction permet de jouer au jeu de la devinette avec l'ordinateur en mode difficile.

    Args:
        ordi (JoueursDevinette): L'ordinateur qui joue.
        borne_min (int): La borne inférieure de l'intervalle. (par défaut : 1)
        borne_max (int): La borne supérieure de l'intervalle. (par défaut : None, sera initialisé à limite)
        limite (int): La limite supérieure du jeu.
        réponse (int): La réponse donnée par l'utilisateur (1 = trop petit, 2 = trop grand, 3 = trouvé).
        proposition (int): Dernière proposition du bot.



    Returns:
        tuple: (proposition (int), borne_min (int), borne_max (int)) - La nouvelle proposition et les bornes mises à jour.
    """

    # Mise à jour des bornes en fonction de la réponse
    if reponse == 1:  # Trop petit
        borne_min = max(borne_min, proposition + 1)
    elif reponse == 2:  # Trop grand
        borne_max = min(borne_max, proposition - 1)

    # Proposition basée sur la recherche dichotomique
    proposition = (borne_min + borne_max) // 2

    return proposition, borne_min, borne_max

