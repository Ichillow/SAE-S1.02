########################################################################################
#Ce fichier contient le jeu de la devinette
########################################################################################

#Importation des fonctions
import sys
sys.path.append("./")
from utilitaires.utils import input_entier, login_joueur, clear_console, sauvegarde_score_joueur



def devinette() ->None:
    """
    Cette fonction est la fonction principale du jeu de la devinette. Elle permet de jouer à ce jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    clear_console()

    #Déclaration des variables utilisées
    joueur1 : str
    joueur2 : str

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

    #Initialisation des variables
    gagné = False
    coup = 0    
    nbTriche = 0
    tricheGagn = False
    triche_detecte = False
    #Login des joueurs
    joueur1, joueur2 = login_joueur()

    #Début du jeu
    limite = int(input("Joueur 1 entrez la limite maximum : "))
    while limite<=0 or limite==1 :
        limite = int(input("Erreur veuillez entrer une limite valide : "))

    nombre = input_entier(0, limite, f"{joueur1} entrez votre nombre et souvenez vous en : ", "Erreur, votre nombre est supérieur à la limite, veuillez saisir un nombre valide : ") 

    clear_console()
    #Affichage de la limite
    print(f"La limite est : {limite}")

    #Tant que le joueur 2 n'a pas trouvé le nombre
    while gagné == False :

        #Proposition du joueur 2
        proposition = input_entier(0, limite, f"{joueur2}, faites une proposition : ", "Erreur, le nombre rentré n'est pas compris dans la limite : ")
        coup = coup+1


        #Initialisation du tour du joueur 1
        tourJ1 = True
        clear_console()

        #Tour du joueur 1
        while tourJ1 == True :
            print(f"Le nombre de {joueur2} est {proposition}")

            #Le joueur 1 donne sa réponse
            choix=réponse(joueur1, joueur2)
            #Choix 1
            if choix == 1:
                if nombre > proposition:
                    clear_console()
                    rappel(limite, proposition) 
                    print(f"{joueur2}, votre nombre est trop petit")
                    triche_detecte = False 
                    tourJ1 = False
                else:
                    triche_detecte = True

            #Choix 2
            elif choix == 2:
                if nombre < proposition:
                    clear_console()
                    rappel(limite, proposition)
                    print(f"{joueur2} votre nombre est trop grand")
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
                print(f"Attention {joueur1} vous avez triché")
                nbTriche += 1
                




    #Fin de la partie
    print(f"Bravo {joueur2} le nombre était {nombre}, vous l'avez trouvez en {coup} coups")
    print(f"{joueur1} vous avez trichez {nbTriche} fois")

    #Assignation des scores
    scoreJ1 = Calcul_scoreJ1(coup, nbTriche, limite)
    scoreJ2 = Calcul_ScoreJ2(coup, limite)

    if tricheGagn == True :
        scoreJ1 = round(scoreJ1/2)

    #Gain de score
    print(f"{joueur1} : {scoreJ1} points")
    print(f"{joueur2} : {scoreJ2} points")

    #Sauvegarde des scores
    sauvegarde_score_joueur("devinettes", joueur1, scoreJ1)
    sauvegarde_score_joueur("devinettes", joueur2, scoreJ2)



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
    score = 58

    score = score- nbtriche*10
    score = score + coups*3
    score = score - round(40/100*limite)

    return score



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
    score = 150

    score = score + round(40/100*limite)
    score =  int(score * 1/coups)
    return score