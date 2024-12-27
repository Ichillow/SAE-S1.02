########################################################################################
#Ce fichier contient le jeu du morpion
########################################################################################

#Importation des fonctions
import sys
sys.path.append("./")
from utilitaires.utils import input_entier, login_joueur, clear_console, input_choix
from utilitaires.gestion_db import sauvegarde_score_joueur

#Structure du joueur
class Joueur:
    nom: str
    score: float = 0
    nbCoups: int = 0
    signe: str = ""

#Programme principal du jeu
def morpion() -> None:
    """
    Cette fonction est la fonction principale du jeu du morpion. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    
    #Déclaration des variables à utilisé
    boucle: bool = True

    joueur1: Joueur = Joueur()
    joueur2: Joueur = Joueur()

    joueur1.nom, joueur2.nom = login_joueur()

    dernierJoueur: str = ""
    vainqueur: str = ""

    grille = [[" " for _ in range(3)] for _ in range(3)]


    #Initialisation du jeu

    joueur1.signe = input_choix(["X", "O"], f"Veuillez choisir un signe pour {joueur1.nom} (X, O) : ", f"Veuillez choisir un signe pour {joueur1.nom} (X, O) : ")
    joueur2.signe = "X" if joueur1.signe == "O" else "O"

    #Début du jeu


    #Tant que la grille n'est pas pleine
    while (joueur1.nbCoups + joueur2.nbCoups) < 9 and boucle:

        clear_console()
        print("/-----------------------------------------------------------\\")
        print("                      Jeu du morpion")

        dernierJoueur = joueur1.nom if (joueur1.nbCoups + joueur2.nbCoups) % 2 == 0 else joueur2.nom

        if dernierJoueur == joueur1.nom:
            grille = tour(joueur1, grille)
            joueur1.nbCoups += 1
        else:
            grille = tour(joueur2, grille)
            joueur2.nbCoups += 1
        
        boucle = verification_jeu_continue(grille)


    #Détermination du vainqueur
    if not boucle:
        vainqueur = dernierJoueur
    else:
        vainqueur = "Personne"


    #Calcul du score
    joueur1.score = calcul_score(vainqueur, joueur1.nom, joueur1.nbCoups)
    joueur2.score = calcul_score(vainqueur, joueur2.nom, joueur2.nbCoups)


    #Sauvegarde du score
    sauvegarde_score_joueur("morpion", joueur1.nom, joueur1.score)
    sauvegarde_score_joueur("morpion", joueur2.nom, joueur2.score)





    #Fin du jeu
    clear_console()
    affichage_grille(grille)
    print()
    print("/-----------------------------------------------------------\\")
    print("                        Fin du jeu")
    print()
    if vainqueur == joueur1.nom:
        print(f"Bravo {joueur1.nom} vous avez gagné en {joueur1.nbCoups} coups.")
        print(f"{joueur2.nom} vous avez perdu en {joueur2.nbCoups} coups.")
    elif vainqueur == joueur2.nom:
        print(f"Bravo {joueur2.nom} vous avez gagné en {joueur2.nbCoups} coups.")
        print(f"{joueur1.nom} vous avez perdu en {joueur1.nbCoups} coups.")
    else:
        print("Match nul")
        print(f"{joueur1.nom} a joué {joueur1.nbCoups} coups et à gagné {joueur1.score} points.")
        print(f"{joueur2.nom} a joué {joueur2.nbCoups} coups et à gagné {joueur2.score} points.")
    print()
    print(f"Score de {joueur1.nom} : {joueur1.score}")
    print(f"Score de {joueur2.nom} : {joueur2.score}")
    print()
    print("\\-----------------------------------------------------------/")




def calcul_score(vainqueur: str, nomJoueur: str, nbrCoups: int) -> float:
    """
    Cette fonction permet de calculer le score d'un joueur.

    Args:
        vainqueur (str): Nom du joueur vainqueur.
        nomJoueur (str): Nom du joueur.
        nbrCoups (int): Nombre de coups du joueur.


    Returns:
        (float): Le score du joueur.
    """

    #Déclaration des variables
    score: float = 0


    #Calcul du score
    if vainqueur == nomJoueur:
        score = 5*(nbrCoups - 1/nbrCoups)
    else:
        score = 2.5*(nbrCoups - 1/nbrCoups)


    return round(score, 2)



def affichage_grille(grille: list[list[str]]) -> None:
    """
    Cette fonction permet d'afficher la grille du jeu.

    Args:
        grille (list[list[str]]): Grille du jeu.

    Returns:
        (None): Cette fonction ne retourne rien.
    """

    #Déclaration des variables
    i: int

    #Affichage de la grille
    print(f"|-  1  -|-  2  -|-  3  -|")
    for i in range(3):
        print(f"        |       |       |")
        print(f"{i+1}   {grille[i][0]}   |   {grille[i][1]}   |   {grille[i][2]}   |")
        print(f"        |       |       |")
        print(f"|-------|-------|-------|")


    return




#Fonction pour afficher le tour du joueur
def tour(joueur:Joueur, grille: list[list[str]]) -> list[list[str]]:
    """
    Cette fonction permet d'afficher le tour du joueur et le nombre d'allumettes restantes.

    Args:
        joueur (str): Nom du joueur.
        signe (str): Signe du joueur.
        grille (list[list[str]]): Grille du jeu.

    Returns:
        grille (list[list[str]]): Grille du jeu.
    """

    #Déclaration des variables
    ligne: int
    colonne: int

    #Affichage du tour du joueur
    print(f"Tour de {joueur.nom}")
    print()
    affichage_grille(grille)
    print()
    print("Veuillez choisir une case")
    print()
    ligne, colonne = input_entier(1, 3, "Veuillez choisir une ligne (1, 2, 3) : ", "Veuillez choisir une ligne (1, 2, 3) : "), input_entier(1, 3, "Veuillez choisir une colonne (1, 2, 3) : ", "Veuillez choisir une colonne (1, 2, 3) : ")

    #Vérification de la case
    while grille[ligne-1][colonne-1] != " ":
        print("Case déjà occupée")
        ligne, colonne = input_entier(1, 3, "Veuillez choisir une ligne (1, 2, 3) : ", "Veuillez choisir une ligne (1, 2, 3) : "), input_entier(1, 3, "Veuillez choisir une colonne (1, 2, 3) : ", "Veuillez choisir une colonne (1, 2, 3) : ")

    #Modification de la grille
    grille[ligne-1][colonne-1] = joueur.signe

    return grille


def verification_jeu_continue(grille: list[list[str]]) -> bool:
    """
    Cette fonction permet de vérifier si le jeu doit continuer ou non.
    
    Args:
        grille: List[List[str]]: La grille du jeu
        
    Returns:
        bool: True si le jeu doit continuer, False sinon
    """

    #Déclaration des variables
    lignes: list[str]
    boucle: bool = True
    taille: int = 3
    i: int

    #Vérification de la grille
    #Vérification des lignes 
    for lignes in grille:
        if lignes.count(lignes[0]) == taille and lignes[0] != " ":
            boucle = False

    #Vérification des colonnes
    for i in range(taille):
        if grille[0][i] == grille[1][i] == grille[2][i] and grille[0][i] != " ":
            boucle = False

    #Vérification des diagonales
    if grille[0][0] == grille[1][1] == grille[2][2] and grille[0][0] != " ":
        boucle = False

    if grille[0][2] == grille[1][1] == grille[2][0] and grille[0][2] != " ":
        boucle = False

    return boucle