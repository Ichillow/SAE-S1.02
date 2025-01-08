import sys, os
sys.path.append("./")
from utilitaires.utils import input_entier, clear_console
from utilitaires.gestion_db import charger_joueurs_jeu, charger_ordi_jeu

#Menu des choix principaux

def menu_principale() -> int:
    """
    Affiche le menu principal et renvoie le choix fait par l'utilisateur.
    
    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        choix (int): Le choix de l'utilisateur.

    """
    #Déclaration des variables
    choix: int
    
    print()
    print("/-----------------------------------------------------------\\")
    print("                   Bienvenu dans le jeu")
    print()
    print("Veuillez faire un choix :")
    print()
    print("1. Jeu des devinettes")
    print("2. Jeu des allumettes")
    print("3. Jeu du morpion")
    print()
    print("4. Voir les scores")
    print("5. Voir les règles")
    print()
    print("6. Quitter")
    print("\\-----------------------------------------------------------/")
    print()
    #Récupération du choix de l'utilisateur
    choix = input_entier(0, 6, "Votre choix : ", "Veuillez choisir l'un des choix possibles")

    return choix




#Menu du choix des scores

def menu_score() -> int:
    """
    Affiche le menu des scores et renvoie le choix fait par l'utilisateur.
    
    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        choix (int): Le choix de l'utilisateur.
    """

    #Déclaration des variables
    choix: int


    #Affichage du menu
    clear_console()
    print("/------------------------------\\")
    print("           Les scores")
    print()
    print("Veuillez faire un choix :")
    print()
    print("1. Scores Devinette")
    print("2. Scores Allumettes")
    print("3. Scores Morpion")
    print()
    print("4. Retour au menu principal")
    print()
    print("\\------------------------------/")
    print()


    #Récupération du choix de l'utilisateur et test de validité
    choix = input_entier(1, 4, "Votre choix : ", "Veuillez choisir l'un des choix possibles")
    print()
    
    return choix



#Menu des règles

def menu_regle() -> int:
    """
    Affiche le menu des règles et renvoie le choix fait par l'utilisateur.
    
    Args:
        (None): Aucun argument n'est nécessaire pour cette preocédure.

    Returns:
        choix (int): Le choix de l'utilisateur.
    """

    #Déclaration des variables
    choix: int


    #Affichage du menu
    clear_console()
    print("/------------------------------\\")
    print("           Les règles")
    print()
    print("Veuillez faire un choix :")
    print()
    print("1. Règles Devinette")
    print("2. Règles Allumettes")
    print("3. Règles Morpion")
    print()
    print("4. Retour au menu principal")
    print()
    print("\\------------------------------/")
    print()


    #Récupération du choix de l'utilisateur et test de validité
    choix = input_entier(1, 4, "Votre choix : ", "Veuillez choisir l'un des choix possibles")
    print()
    
    return choix



#Fonction pour affiché les scores d'un jeu

def affichage_score(jeu: str):
    """
    Affiche les scores d'un jeu en particulier

    Args:
        jeu(str): Nom du jeu.

    Returns:
        (None) : Ne retourne rien.
    """
    #Déclaration des variables
    scoresJoueurs: list[tuple[int, str, int, int, int, int]] = []
    scoreOrdis: list[tuple[int, str, int, int, int]]
    i: int
    indexScoreJoueur: int

    #Charchement des scores
    scoresJoueurs = charger_joueurs_jeu(jeu)
    scoreOrdis = charger_ordi_jeu(jeu)


    #Attribution de l'index du jeu
    if jeu == "devinettes":
        indexScoreJoueur = 2
    elif jeu == "allumettes":
        indexScoreJoueur = 3
    else:
        indexScoreJoueur = 4





    #Affichage des scores
    clear_console()

    print("/------------------------------\\")
    print("Scores du jeu :", jeu)
    print()

    if len(scoresJoueurs) == 0:
        print("Aucun score pour les joueurs")
    else:
        print("Scores des joueurs :")
        for i in range(len(scoresJoueurs)):
            print(f"{i+1}. {scoresJoueurs[i][1]} : {scoresJoueurs[i][indexScoreJoueur]} points, {scoresJoueurs[i][5]} parties jouées au total")
    
    print()
    print("Scores des ordinateurs :")
    for i in range(len(scoreOrdis)):
        print(f"{i+1}. {scoreOrdis[i][1]} : {scoreOrdis[i][2]} points, {scoreOrdis[i][3]} parties jouées au total")

    print()
    print("\\------------------------------/")
    print()
    print("Appuyez sur Entrée pour continuer", end="")
    input() #Pause pour laisser le temps à l'utilisateur de lire les scores



#Fonction pour affiché les règles d'un jeu

def affichage_regles(jeu: str):
    """
    Affiche les règles d'un jeu en particulier

    Args:
        jeu(str): Nom du jeu.

    Returns:
        (None) : Ne retourne rien.
    """

    #Déclaration des variables
    chemin: str
    fichier: list[str]
    line: str


    #Chargement du fichier
    chemin = os.getcwd() + "/regles/" + jeu + ".txt"
    if os.path.exists(chemin):
        with open(chemin, "r", encoding="utf-8") as f:
            fichier = f.readlines()
    else:
        fichier = ["Le fichier de règles n'existe pas"]

    #Affichage des règles
    clear_console()
    print("/------------------------------\\")
    print("Règles du jeu :", jeu)
    print()
    for line in fichier:
        print(line)
    print("\\------------------------------/")
    print()
    print("Appuyez sur Entrée pour continuer", end="")
    input() #Pause pour laisser le temps à l'utilisateur de lire les règles


