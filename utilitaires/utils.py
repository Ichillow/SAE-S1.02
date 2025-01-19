########################################################################################
# Ce fichier contient les fonctions utilitaires qui seront utilisées dans le programme #
########################################################################################

import sys
sys.path.append("./")
from typing import Union
from utilitaires.gestion_db import charger_joueurs_jeu, charger_ordi_jeu
from ordi.ordi_struct import Ordi

#Fonction pour demander le nom des joueurs
def login_joueur(jeu: str) -> tuple[Union[str, Ordi], Union[str, Ordi]]:
    """
    Fonction pour demander le nom des joueurs (cela peut être des joueurs humains ou des ordinateurs)
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (tuple[Union[str, Ordi], Union[str, Ordi]) : Tuple contenant les noms des joueurs.

    """
    
    #Déclaration des variables
    mode_jeu: int
    joueur1: Union[str, Ordi]
    joueur2: Union[str, Ordi]
    boucle: bool = True
    choix: int


    #Effacement de la console
    clear_console()


    #Choix du mode de jeu

    print("/---------------------------------------\\")
    print("       Choisissez le mode de jeu")
    print()
    print("1. Joueur contre Joueur")
    print("2. Joueur contre Ordinateur")
    print("3. Ordinateur contre Ordinateur")
    print()

    mode_jeu = input_entier(1, 3, "Saisir le numéro du mode de jeu : ", "Veuillez saisir un numéro valide : ")

    clear_console()

    #Saisie des noms des joueurs
    while boucle:

        if mode_jeu == 1:
            print("Mode de jeu : Joueur contre Joueur")
            print("/---------------------------------------\\")
            print("      Saisie des noms des joueurs")
            print()
            if jeu == "devinettes":
                print("Joueur qui veut faire deviner un nombre")
                joueur1= saisie_nom_joueur(jeu)
                print("Joueur qui veut deviner un nombre")
                joueur2 = saisie_nom_joueur(jeu)
            else:
                joueur1 = saisie_nom_joueur(jeu)
                joueur2 = saisie_nom_joueur(jeu)
            
            if joueur1 == joueur2:
                clear_console()
                print("Erreur : les noms des joueurs ne peuvent pas être identiques.")
            else:
                boucle = False

        elif mode_jeu == 2:
            print("Mode de jeu : Joueur contre Ordinateur")
            print("/---------------------------------------\\")
            if jeu == "devinettes":
                print("Joueur, vous voulez :")
                print("1. Deviner un nombre")
                print("2. Faire deviner un nombre")
                print()
                choix = input_entier(1, 2, "Saisir le numéro de votre choix : ", "Veuillez saisir un numéro valide : ")
                if choix == 1:
                    print("      Saisie des noms des joueurs")
                    print()
                    joueur1 = saisie_nom_ordi(jeu)
                    joueur2 = saisie_nom_joueur(jeu)
                elif choix == 2:
                    print("      Saisie des noms des joueurs")
                    print()
                    joueur1 = saisie_nom_joueur(jeu)
                    joueur2 = saisie_nom_ordi(jeu)
            else:
                print("      Saisie des noms des joueurs")
                print()
                joueur1 = saisie_nom_joueur(jeu)
                joueur2 = saisie_nom_ordi(jeu)

            boucle = False

        else:
            print("Mode de jeu : Ordinateur contre Ordinateur")
            print("/---------------------------------------\\")
            print("      Saisie des noms des ordinateurs")
            print()
            if jeu == "devinettes":
                print("Ordinateur qui va faire deviner un nombre")
                joueur1 = saisie_nom_ordi(jeu)
                print("Ordinateur qui va deviner un nombre")
                joueur2 = saisie_nom_ordi(jeu)
            else:
                joueur1 = saisie_nom_ordi(jeu)
                joueur2 = saisie_nom_ordi(jeu)

            if joueur1.nom == joueur2.nom:
                clear_console()
                print("Erreur : un ordinateur ne peux pas jouer contre lui-même.")
            else:
                boucle = False

    return joueur1, joueur2



def saisie_nom_joueur(jeu: str) -> str:
    """
    Fonction pour demander le nom d'un joueur
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (str) : Nom du joueur.

    """
    #Déclaration des variables
    nom_joueur: str
    boucle: bool = True
    lst_joueurs: list[tuple[int, str, float, float, float, int]] = charger_joueurs_jeu(jeu)
    i: int
    choix: str = "o"

    #Saisie du nom du joueur
    while boucle:
        i = 0
        nom_joueur = str(input("Saisir le nom du joueur : "))
        while nom_joueur == "":
            nom_joueur = str(input("Veuillez saisir un nom valide (non vide): "))
        
        #Vérification si le joueur existe déjà
        while i < len(lst_joueurs):
            if nom_joueur == lst_joueurs[i][1]:
                print("Ce joueur existe déjà : ")
                print(f"ID : {lst_joueurs[i][0]}")
                print(f"Nom : '{lst_joueurs[i][1]}'")
                print(f"Score aux allumettes : {lst_joueurs[i][2]}")
                print(f"Score au morpion : {lst_joueurs[i][3]}")
                print(f"Score aux devinettes : {lst_joueurs[i][4]}")
                print(f"Nombre de parties : {lst_joueurs[i][5]}")
                print()
                choix = input_choix(["o", "n"], "Voulez-vous continuer avec ce nom ? (o/n) : ", "Veuillez saisir un choix valide : ")
                i = len(lst_joueurs)
            else:
                i += 1

        #Sortie de la boucle si le joueur n'existe pas ou si le joueur veut continuer
        if choix == "o":
            boucle = False
    
    print()
    return nom_joueur


def saisie_nom_ordi(jeu: str) -> Ordi:
    """
    Fonction pour demander le nom d'un ordinateur
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (str) : Nom de l'ordinateur.

    """
    #Déclaration des variables
    num_ordi: int
    ordis: list[tuple[int, str, int, float, int]] = charger_ordi_jeu(jeu, False)
    ordi_return: Ordi = Ordi()

    #Affichage des nom des ordinateurs
    print("Liste des ordinateurs : ")
    for ordi in ordis:
        print(f"{ordi[0]}. {ordi[1]}, niveau : {ordi[2]}")
    print()

    #Saisie du nom de l'ordinateur
    num_ordi = int(input_choix([str(ordi[0]) for ordi in ordis], "Saisir le numéro de l'ordinateur : ", "Veuillez saisir un numéro valide : "))

    num_ordi -= 1

    #Attribution des valeurs à l'objet Ordi
    ordi_return.id = ordis[num_ordi][0]
    ordi_return.nom = ordis[num_ordi][1]
    ordi_return.difficultee = ordis[num_ordi][2]
    ordi_return.score = ordis[num_ordi][3]
    ordi_return.nb_parties = ordis[num_ordi][4]

    print()
    return ordi_return





def input_entier(borneMin:int, borneMax:int, message:str, erreur:str) -> int:
    """
    Fonction pour vérifier si l'entrée utilisateur est un entier et qu'il est compris entre les bornes données
    Args:
        borneMin(int): Borne inférieure.
        borneMax(int): Borne supérieure.
        message(str): Message à afficher.
        erreur(str): Message d'erreur à afficher.

    Returns:
        nombre(int): Nombre entré par l'utilisateur.
    """

    input_: str
    nombre: int
    boucle: bool = True

    input_ = input(message)
    while not input_.isdigit():
        print(erreur)
        input_ = input(message)
    nombre = int(input_)

    while boucle:
        if input_.isdigit():
            nombre = int(input_)
            if borneMin <= nombre <= borneMax:
                boucle = False
            else:
                print(erreur)
                input_ = input(message)
        else:
            print(erreur)
            input_ = input(message)
    return nombre


def clear_console() -> None:
    """
    Procédure pour effacer la console
    Args:
        (None) : Ne prend pas de paramètres.

    Returns:
        (None) : Ne retourne rien.

    """
    print("\033c", end="")


#La fonction sauvegarde_score_joueur à été déplacée dans le fichier gestion_db.py



#La fonction charger_score à été déplacée dans le fichier gestion_db.py



#La fonction charger_score_joueur à été supprimée car elle n'est plus utilisée






def verification_type(value: str, type_:type) -> bool:
    """
    Fonction pour vérifier si la valeur est du type demandé
    Args:
        value(str): Valeur à vérifier.
        type_(type): Type demandé.

    Returns:
        (bool): True si la valeur est du type demandé, False sinon.
    """

    return isinstance(value, type_)


def input_choix(choix:list[str], message:str, erreur:str) -> str:
    """
    Fonction pour vérifier si l'entrée utilisateur est un choix valide
    Args:
        choix(list[str]): Liste des choix possibles.
        message(str): Message à afficher.
        erreur(str): Message d'erreur à afficher.

    Returns:
        nombre(int): Nombre entré par l'utilisateur.
    """

    #Déclaration des variables
    input_: str

    #Saisie de l'entrée utilisateur
    input_ = input(message).lower()
    choix_ = [choix[i].lower() for i in range(len(choix))]
    while input_ not in choix_:
        print(erreur)
        input_ = input(message)
    return input_
