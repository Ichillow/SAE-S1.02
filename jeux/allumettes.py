########################################################################################
#Ce fichier contient le jeu des allumettes
########################################################################################

#Importation des fonctions
import sys
sys.path.append("./")
from typing import Union
from time import sleep
from utilitaires.utils import input_entier, login_joueur, clear_console
from utilitaires.gestion_db import sauvegarde_score_joueur, sauvegarde_score_ordi
from ordi.ordi_struct import Ordi, JoueurAllumettes
from ordi.allumettes.ordi_facile import ordi_allumettes_facile
from ordi.allumettes.ordi_normal import ordi_allumettes_normal
from ordi.allumettes.ordi_difficile import ordi_allumettes_difficile



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
    joueur1: JoueurAllumettes = JoueurAllumettes()
    joueur2: JoueurAllumettes = JoueurAllumettes()

    recupInfo: tuple[Union[str, Ordi], Union[str, Ordi]]

    #Récupération des informations des joueurs
    recupInfo = login_joueur("allumettes")

    #Vérification du type de joueur et initialisation
    if isinstance(recupInfo[0], str):
        joueur1.nom = recupInfo[0]
    else:
        joueur1.nom = recupInfo[0].nom
        joueur1.difficultee = recupInfo[0].difficultee

    if isinstance(recupInfo[1], str):
        joueur2.nom = recupInfo[1]
    else:
        joueur2.nom = recupInfo[1].nom
        joueur2.difficultee = recupInfo[1].difficultee


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
            if joueur1.difficultee == -1:
                nbrAllumettes -= tour(joueur1.nom, nbrAllumettes)
            else:
                nbrAllumettes -= tour_ordi(joueur1, nbrAllumettes)
            joueur1.nbCoups += 1
        
        #Tour du joueur 2
        if nbrAllumettes > 0:
            avantDernierJoueur = joueur1.nom
            if joueur2.difficultee == -1:
                nbrAllumettes -= tour(joueur2.nom, nbrAllumettes)
            else:
                nbrAllumettes -= tour_ordi(joueur2, nbrAllumettes)
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
    if vainqueur == joueur1.nom:
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
    if joueur1.difficultee == -1:
        sauvegarde_score_joueur("allumettes", joueur1.nom, joueur1.score)
    else:
        sauvegarde_score_ordi("allumettes", joueur1.nom, joueur1.score)
    
    if joueur2.difficultee == -1:
        sauvegarde_score_joueur("allumettes", joueur2.nom, joueur2.score)
    else:
        sauvegarde_score_ordi("allumettes", joueur2.nom, joueur2.score)




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



def tour_ordi(joueur:JoueurAllumettes, nbrAllumettes:int) -> int:
    """
    Cette fonction permet d'afficher le tour de l'ordinateur et le nombre d'allumettes restantes.

    Args:
        joueur (JoueurAllumettes): Le joueur qui joue.
        nbrAllumettes (int): Le nombre d'allumettes restantes.

    Returns:
        (int): Le nombre d'allumettes retirées par l'ordinateur
    """

    #Déclaration des variables
    choix: int = 0

    print()
    print(f"{joueur.nom} c'est à votre tour.")
    print(f"Il reste {nbrAllumettes} allumettes.")
    print("L'ordinateur réfléchit...")
    sleep(2)
    if joueur.difficultee == 1:
        choix = ordi_allumettes_facile(nbrAllumettes)
    elif joueur.difficultee == 2:
        choix = ordi_allumettes_normal(joueur, nbrAllumettes)
    else:
        choix = ordi_allumettes_difficile(nbrAllumettes)

    return choix

allumettes()