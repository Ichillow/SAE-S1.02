import sys
sys.path.append("./")



def ordi_allumettes_difficile(allumettes: int) -> int:
    """
    Fonction qui permet à l'ordinateur de jouer aux allumettes en mode difficile
    
    Args:
        allumettes (int): Le nombre d'allumettes restantes

    Returns:
        int: Le nombre d'allumettes restantes après le tour de l'ordinateur
    """

    #Déclaration des variables
    choix: int

    #Calcul du nombre d'allumettes à retirer
    choix = (allumettes - 1) % 4

    #Vérification du choix
    if choix == 0:
        choix = 1

    return choix