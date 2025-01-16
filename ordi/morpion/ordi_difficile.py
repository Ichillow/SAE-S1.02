import sys
sys.path.append("./")

from ordi.ordi_struct import JoueurMorpion

def ordi_morpion_difficile(ordi: JoueurMorpion, grille: list[list[str]]) -> list[list[str]]:
    """
    Fonction qui permet à l'ordinateur de jouer au morpion en mode difficile
    
    Args:
        ordi (JoueurMorpion): L'ordinateur qui joue
        grille (list[list[str]]): La grille de jeu

    Returns:
        list[list[str]]: La grille de jeu après le tour de l'ordinateur
    """

    #Déclaration des variables
    signe_adversaire: str

    signe_adversaire = "X" if ordi.signe == "O" else "O"


    #On vérifie si l'ordinateur joue en premier
    if grille == [[" " for _ in range(3)] for _ in range(3)]:
        #On met un signe au milieu
        grille[1][1] = ordi.signe
    else:
        #On vérifie si l'adversaire peut gagner en jouant




def jouer_coup_gagnant(ordi: JoueurMorpion, grille: list[list[str]]) -> list[list[str]]:
    """
    Fonction qui permet à l'ordinateur de jouer un coup gagnant
    
    Args:
        ordi (JoueurMorpion): L'ordinateur qui joue
        grille (list[list[str]]): La grille de jeu

    Returns:
        list[list[str]]: La grille de jeu après le coup gagnant
    """

    #On vérifie si l'ordinateur peut gagner en jouant
    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = ordi.signe
                if verification_gagnant(ordi, grille):
                    return grille
                grille[i][j] = " "

    return grille




def verification_gagnant(ordi: JoueurMorpion, grille: list[list[str]]) -> bool:
    """
    Fonction qui permet de vérifier si l'ordinateur a gagné
    
    Args:
        ordi (JoueurMorpion): L'ordinateur qui joue
        grille (list[list[str]]): La grille de jeu

    Returns:
        bool: True si l'ordinateur a gagné, False sinon
    """

    #On vérifie si l'ordinateur a gagné
    for i in range(3):
        if grille[i].count(ordi.signe) == 3:
            return True

    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] == ordi.signe:
            return True

    if grille[0][0] == grille[1][1] == grille[2][2] == ordi.signe:
        return True

    if grille[0][2] == grille[1][1] == grille[2][0] == ordi.signe:
        return True

    return False