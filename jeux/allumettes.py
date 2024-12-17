########################################################################################
#Ce fichier contient le jeu des allumettes
########################################################################################

#Importation des fonctions
import sys
sys.path.append("./")
from utilitaires.utils import input_entier, login_joueur, clear_console, sauvegarde_score_joueur

#Structure du joueur
class Joueur:
    nom: str
    score: float = 0
    nbAllumettes: int = 0
    nbCoups: int = 0

#Programme principal du jeu
def allumettes() -> None:
    """
    Cette fonction est la fonction principale du jeu des allumettes. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    
    #Déclaration des variables à utilisé

    joueur1: Joueur = Joueur()
    joueur2: Joueur = Joueur()

    nomJoueur1, nomJoueur2 = login_joueur()

    joueur1.nom = nomJoueur1
    joueur2.nom = nomJoueur2


    nbrAllumettesDepart: int = 20
    nbrAllumettes: int = 20

    avantDernierJoueur: str = ""
    vainqueur: str = ""





    #Début du jeu

    clear_console()

    print("/-----------------------------------------------------------\\")
    print("                     Jeu des allumettes")
    
    #Tant qu'il reste des allumettes le jeu continue
    while nbrAllumettes > 0:

        #Tour du joueur 1
        if nbrAllumettes > 0:
            avantDernierJoueur = joueur2.nom
            nbrAllumettes -= tour(joueur1.nom, nbrAllumettes)
            joueur1.nbCoups += 1
        
        #Tour du joueur 2
        if nbrAllumettes > 0:
            avantDernierJoueur = joueur1.nom
            nbrAllumettes -= tour(joueur2.nom, nbrAllumettes)
            joueur2.nbCoups += 1

        if nbrAllumettes == 0:
            vainqueur = avantDernierJoueur
    

    #Calcul du score

    if vainqueur == joueur1.nom:
        joueur1.score = calcul_score(nbrAllumettesDepart, joueur1.nbAllumettes, joueur1.nbCoups, 1)
        joueur2.score = calcul_score(nbrAllumettesDepart, joueur2.nbAllumettes, joueur2.nbCoups, 0)
    else:
        joueur1.score = calcul_score(nbrAllumettesDepart, joueur1.nbAllumettes, joueur1.nbCoups, 0)
        joueur2.score = calcul_score(nbrAllumettesDepart, joueur2.nbAllumettes, joueur2.nbCoups, 1)


    #Fin du jeu
    print()
    print("/-----------------------------------------------------------\\")
    print("                        Fin du jeu")
    print()
    if vainqueur == nomJoueur1:
        print(f"Bravo {joueur1.nom} vous avez gagné en {joueur1.nbCoups} coups.")
        print(f"{joueur2.nom} vous avez perdu en {joueur2.nbCoups} coups.")
    else:
        print(f"Bravo {joueur2.nom} vous avez gagné en {joueur2.nbCoups} coups.")
        print(f"{joueur1.nom} vous avez perdu en {joueur1.nbCoups} coups.")
    print()
    print(f"Score de {joueur1.nom} : {joueur1.score}")
    print(f"Score de {joueur2.nom} : {joueur2.score}")
    print()
    print("\\-----------------------------------------------------------/")

    #Sauvegarde des scores
    sauvegarde_score_joueur("allumettes", joueur1.nom, joueur1.score)
    sauvegarde_score_joueur("allumettes", joueur2.nom, joueur2.score)




def calcul_score(nbrAllumettes:int, nbrAllumettesJoueur:int, nbrCoups:int, victoir:int) -> float:
    """
    Cette fonction permet de calculer le score d'un joueur.

    Args:
        nbrAllumettes (int): Le nombre d'allumettes au début du jeu.
        nbrAllumettesJoueur (int): Le nombre d'allumettes retirées par le joueur.
        nbrCoups (int): Le nombre de coups joués par le joueur.

    Returns:
        (float): Le score du joueur.
    """

    #Déclaration des variables
    score: float = 0
    differenceScore: int = 0

    #Calcul du score
    differenceScore = nbrAllumettes - nbrAllumettesJoueur
    if nbrCoups != 0:
        score = (differenceScore / nbrCoups) + (victoir * 5)
    else:
        score = 0

    return round(score,2)


#Fonction pour afficher le tour du joueur
def tour(joueur:str, nbrAllumettes:int) -> int:
    """
    Cette fonction permet d'afficher le tour du joueur et le nombre d'allumettes restantes.

    Args:
        joueur (str): Le nom du joueur qui joue.
        nbrAllumettes (int): Le nombre d'allumettes restantes.

    Returns:
        (int): Le nombre d'allumettes retirées par le joueur
    """

    #Déclaration des variables
    nbrAllumettesRetirees: int = 0
    limite_allumettes: int = 3

    #Calcule du nombre d'allumettes restantes
    if nbrAllumettes < 3:
        limite_allumettes = nbrAllumettes

    print()
    print(f"{joueur} c'est à votre tour.")
    print(f"Il reste {nbrAllumettes} allumettes.")
    nbrAllumettesRetirees = input_entier(1, limite_allumettes, f"Combien d'allumettes voulez-vous retirer, 1, 2 ou {limite_allumettes} : ", f"Veillez saisir un nombre entre 1 et {limite_allumettes}.")

    return nbrAllumettesRetirees