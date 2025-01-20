import sys
sys.path.append("./")

from ordi.ordi_struct import JoueurMorpion
from ordi.morpion.ordi_facile import ordi_morpion_facile





def ordi_morpion_difficile(ordi: JoueurMorpion, grille: list[list[str]], adversaire: JoueurMorpion) -> list[list[str]]:
    """
    Fonction qui permet à l'ordinateur de jouer au morpion en mode difficile
    
    Args:
        ordi (JoueurMorpion): L'ordinateur qui joue
        grille (list[list[str]]): La grille de jeu

    Returns:
        list[list[str]]: La grille de jeu après le tour de l'ordinateur
    """

    #Déclaration des variables
    grille_temps: list[list[str]]

    grille_temps = []
    grille_temps.append(grille[0].copy())
    grille_temps.append(grille[1].copy())
    grille_temps.append(grille[2].copy())


    #Si on peut, on met un signe au milieu
    if grille_temps[1][1] == " ":
        grille_temps[1][1] = ordi.signe

    #Sinon, on essaye de jouer un coups gagnant (si possible)
    else:
        grille_temps = jouer_coup_gagnant(ordi, grille_temps)

        #Sinon, on essaye de bloquer le joueur adverse
        if grille_temps == grille:

            grille_temps = jouer_bloquer(ordi, adversaire, grille_temps)

            #Sinon, on rempli un coin
            if grille_temps == grille:

                if grille_temps[0][0] == " ":
                    grille_temps[0][0] = ordi.signe

                elif grille_temps[0][2] == " ":
                    grille_temps[0][2] = ordi.signe

                elif grille_temps[2][0] == " ":
                    grille_temps[2][0] = ordi.signe

                elif grille_temps[2][2] == " ":
                    grille_temps[2][2] = ordi.signe

                #Sinon, on joue un coups aléatoire
                else:
                    grille_temps = ordi_morpion_facile(ordi, grille_temps)
    
    grille = grille_temps

    return grille




def jouer_coup_gagnant(ordi: JoueurMorpion, grille: list[list[str]]) -> list[list[str]]:
    """
    Fonction qui permet à l'ordinateur de jouer un coup gagnant
    
    Args:
        ordi (JoueurMorpion): L'ordinateur qui joue
        grille (list[list[str]]): La grille de jeu

    Returns:
        list[list[str]]: La grille de jeu après le coup gagnant
    """

    #Déclaration des variables
    grille_temps: list[list[str]]
    i_gagnant: int = -1
    j_gagnant: int = -1

    grille_temps = []
    grille_temps.append(grille[0].copy())
    grille_temps.append(grille[1].copy())
    grille_temps.append(grille[2].copy())


    #On vérifie si l'ordinateur peut gagner en jouant
    for i in range(3):
        for j in range(3):
            if grille_temps[i][j] == " ":
                grille_temps[i][j] = ordi.signe
                if verification_gagnant(ordi, grille_temps):
                    i_gagnant = i
                    j_gagnant = j
                grille_temps[i][j] = " "
    
    #Si l'ordinateur peut gagner, on joue
    if i_gagnant != -1:
        grille[i_gagnant][j_gagnant] = ordi.signe

    return grille



def jouer_bloquer(ordi: JoueurMorpion, adversaire: JoueurMorpion, grille: list[list[str]]) -> list[list[str]]:
    """
    Fonction qui permet à l'ordinateur de bloquer le joueur adverse
    
    Args:
        adversaire (JoueurMorpion): Le joueur adverse
        grille (list[list[str]]): La grille de jeu

    Returns:
        list[list[str]]: La grille de jeu après le blocage
    """

    #Déclaration des variables
    grille_temps: list[list[str]]
    i_gagant: int = -1
    j_gagant: int = -1


    grille_temps = []
    grille_temps.append(grille[0].copy())
    grille_temps.append(grille[1].copy())
    grille_temps.append(grille[2].copy())

    #Vérification du joueur adverse
    for i in range(3):
        for j in range(3):
            if grille_temps[i][j] == " ":
                grille_temps[i][j] = adversaire.signe
                if verification_gagnant(adversaire, grille_temps):
                    i_gagant = i
                    j_gagant = j
                grille_temps[i][j] = " "

    #Si le joueur adverse peut gagner, on bloque
    if i_gagant != -1:
        grille[i_gagant][j_gagant] = ordi.signe

    return grille


def verification_gagnant(joueur: JoueurMorpion, grille: list[list[str]]) -> bool:
    """
    Fonction qui permet de vérifier si le joueur a gagné
    
    Args:
        ordi (JoueurMorpion): Le joueur que l'on veut tester
        grille (list[list[str]]): La grille de jeu

    Returns:
        bool: True si le joueur a gagné, False sinon
    """

    #Déclaration des variables
    a_gagne: bool = False

    #On vérifie si l'ordinateur a gagné
    for i in range(3):
        if grille[i].count(joueur.signe) == 3:
            a_gagne = True

    for i in range(3):
        if grille[0][i] == grille[1][i] == grille[2][i] == joueur.signe:
            a_gagne = True

    if grille[0][0] == grille[1][1] == grille[2][2] == joueur.signe:
        a_gagne = True

    if grille[0][2] == grille[1][1] == grille[2][0] == joueur.signe:
        a_gagne = True

    return a_gagne