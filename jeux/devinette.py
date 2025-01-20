########################################################################################
#Ce fichier contient le jeu de la devinette
########################################################################################

#Importation des fonctions
import sys
sys.path.append("./")
from utilitaires.utils import input_entier, login_joueur, clear_console
from utilitaires.gestion_db import sauvegarde_score_joueur, sauvegarde_score_ordi
from typing import Union
from ordi.ordi_struct import Ordi, JoueursDevinette
#importation des ordinateurs
from ordi.devinettes.ordi_facile import ordi_cherche_facile
from ordi.devinettes.ordi_normal import ordi_cherche_normal
from ordi.devinettes.ordi_difficile import ordi_cherche_difficile
from ordi.devinettes.ordi_réponse import ordi_réponse

def devinette():
    """
    Cette fonction est la fonction principale du jeu de la devinette. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    clear_console()

    #Déclaration des variables utilisées
    joueur1: JoueursDevinette = JoueursDevinette()
    joueur2: JoueursDevinette = JoueursDevinette()

    coup : int
    nombre : int
    choix : int
    limite : int
    choix : int
    proposition : int
    gagné : bool

    scoreJ1 : int
    scoreJ2 : int

    nbTriche : int
    triche_detecte : bool
    tricheGagn : bool

    tourJ1 : bool

    borne_inf : int
    borne_sup : int
    
    #Initialisation des variables
    gagné = False
    coup = 0    
    nbTriche = 0
    tricheGagn = False
    triche_detecte = False
    choix = 0
    proposition = 0
    nombre = -1

    recupInfo: tuple[Union[str, Ordi], Union[str, Ordi]]

    #Récupération des informations des joueurs
    recupInfo = login_joueur("devinettes")


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




    #Début du jeu
    if joueur1.difficultee == -1 :
        limite = int(input(f"{joueur1.nom} entrez la limite maximum : "))
    elif joueur1.difficultee != -1 and joueur2.difficultee != -1 :
        limite = int(input("Entrez la limite maximum : "))
    else :
        limite = int(input(f"{joueur2.nom} entrez la limite maximum : "))

    while limite<=0 or limite==1 :
        limite = int(input("Erreur veuillez entrer une limite valide : "))
    
    #Initialisation des bornes
    borne_inf = 1
    borne_sup = limite

    #Initialisation du nombre à trouver
    if joueur1.difficultee == -1 :
        nombre = input_entier(0, limite, f"{joueur1.nom} entrez votre nombre et souvenez vous en : ", "Erreur, votre nombre est supérieur à la limite, veuillez saisir un nombre valide : ")
    else :
        _, nombre = ordi_réponse(joueur1, limite, proposition, nombre, joueur2)    
    
    clear_console()


    #Affichage de la limite
    print(f"La limite est : {limite}")


    #Tant que le joueur 2 n'a pas trouvé le nombre 
    while gagné == False :


        #Proposition du joueur 2
        if joueur2.difficultee == -1 :
            proposition = input_entier(0, limite, f"{joueur2.nom}, faites une proposition : ", "Erreur, le nombre rentré n'est pas compris dans la limite : ")
        #Proposition de l'ordi facile
        elif joueur2.difficultee == 1 :
            proposition, borne_inf, borne_sup = ordi_cherche_facile(joueur2, borne_inf, borne_sup, limite, choix, proposition)
        #Proposition de l'ordi normal
        elif joueur2.difficultee == 2 :
            proposition, borne_inf, borne_sup = ordi_cherche_normal(joueur2, borne_inf, borne_sup, limite, choix, proposition)
        #Proposition de l'ordi difficile
        else :
            proposition, borne_inf, borne_sup = ordi_cherche_difficile(joueur2, borne_inf, borne_sup, limite, choix,  proposition )

        #Incrémentation du nombre de coups
        coup = coup+1

        #Initialisation du tour du joueur 1
        tourJ1 = True
        clear_console()

        #Tour du joueur 1
        while tourJ1 == True :
            print(f"Le nombre de {joueur2.nom} est : {proposition}")
            #Le joueur 1 donne sa réponse
            if joueur1.difficultee == -1 :
                choix=réponse(joueur1.nom, joueur2.nom)
            else:
                choix, _ = ordi_réponse(joueur1, limite, proposition, nombre, joueur2)  
            #Choix 1
            if choix == 1:
                if nombre > proposition:
                    clear_console()
                    rappel(limite, proposition) 
                    print(f"{joueur2.nom}, votre nombre est trop petit")
                    triche_detecte = False 
                    tourJ1 = False
                else:
                    triche_detecte = True

            #Choix 2
            elif choix == 2:
                if nombre < proposition:
                    clear_console()
                    rappel(limite, proposition)
                    print(f"{joueur2.nom} votre nombre est trop grand")
                    triche_detecte = False
                    tourJ1 = False
                else:
                    triche_detecte = True

            #Choix 3
            elif choix == 3:
                if nombre == proposition:
                    tourJ1 = False
                    triche_detecte = False
                    gagné = True
                    clear_console()
                else:
                    triche_detecte = True
                    tricheGagn = True

            #Si le joueur 1 a triché
            if triche_detecte == True:
                clear_console()
                print(f"Attention {joueur1.nom} vous avez triché")
                nbTriche += 1
                





    #Fin de la partie
    print(f"Bravo {joueur2.nom} le nombre était {nombre}, vous l'avez trouvez en {coup} coups")
    print(f"{joueur1.nom} vous avez trichez {nbTriche} fois")

    #Assignation des scores
    scoreJ1 = Calcul_scoreJ1(coup, nbTriche, limite)
    scoreJ2 = Calcul_ScoreJ2(coup, limite)

    if tricheGagn == True :
        scoreJ1 = round(scoreJ1/2)

    #Gain de score
    print(f"{joueur1.nom} : {scoreJ1} points")
    print(f"{joueur2.nom} : {scoreJ2} points")

    #Sauvegarde des scores
    if joueur1.difficultee == -1 :
        sauvegarde_score_joueur("devinettes", joueur1.nom, scoreJ1)
    else:
        sauvegarde_score_ordi("devinettes", joueur1.nom, scoreJ1)

    if joueur2.difficultee == -1 :
        sauvegarde_score_joueur("devinettes", joueur2.nom, scoreJ2)
    else:
        sauvegarde_score_ordi("devinettes", joueur2.nom, scoreJ2)
    return None


def réponse(joueur1:str, joueur2:str) ->int :
    """
    Cette fonction permet au joueur 1 de donner une indication au joueur 2

    Args:
        joueur1(str): Le nom du joueur 1
        joueur2(str): Le nom du joueur 2
    
    Returns:
        choix(int): Cette fonction retourne le choix du joueur 1
    """
    choix : int

    print("---------------------------------------")
    print(f"{joueur1}, donnez une indication au Joueur 2 :")
    print("1. Trop petit")
    print("2. Trop grand")
    print("3. C'est gagné")
    
    choix = input_entier(1, 3, f"{joueur1}, comment est le nombre de {joueur2} ? : ", "Erreur votre choix n'existe pas")
    
    return choix



def rappel (limite:int, proposition:int)  ->None:
    """
    Cette fonction sert à rappeler les infos

    Args:
        limite(int): C'est le nombre max possible
        proposition(int):C'est la dernière proposition du joueur 2

    Returns:
        (None): Cette fonction ne retourne
    """
    print(f"La limite est de : {limite}")
    print(f"Le dernier nombre est {proposition}")



#calculs des scores
def Calcul_scoreJ1(coups:int,nbtriche:int, limite:int) ->int :
    """
    Cette fonction permet de calculer le score du joueur 1
    
    Args:
        coups(int): C'est le nombre de coups que le joueur 2 a mis pour trouver le nombre
        nbtriche(int): C'est le nombre de tricherie du joueur 1
        limite(int): C'est la limite du nombre que le joueur 1 a choisi
        
    Returns:
        score(int): Cette fonction retourne le score du joueur 1
    """
    score : int
    score = round(30+10/100*limite)

    score = score + coups * 3

    #Si le joueur a triché
    if nbtriche != 0:
        score = score - (nbtriche + round(2/100*limite))*5
        if score <=30 :
            score = 30
    return max(0, score)



def Calcul_ScoreJ2(coups:int, limite:int) ->int :
    """
    Cette fonction permet de calculer le score du joueur 2

    Args:   

        coups(int): C'est le nombre de coups que le joueur 2 a mis pour trouver le nombre
        limite(int): C'est la limite du nombre que le joueur 1 a choisi

    Returns:
        score(int): Cette fonction retourne le score du joueur 2
    """
    score : int

    score = round(50+50/100*limite)
    score = int(score - (2*coups))
    return max(0, score)


