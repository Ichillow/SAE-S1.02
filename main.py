#Importation des modules
import sys
sys.path.append("./")

#Téléchargement des modules non installés
try:
    from colorama import init
except ImportError:
    print("Module de couleur non installé, installation...")
    import os
    os.system("pip install colorama")
    from colorama import init

#Initialisation de colorama
init()

from jeux.allumettes import allumettes
from jeux.morpion import morpion
from jeux.devinette import devinette

from utilitaires.utils import clear_console
from menus.menus import menu_principale, menu_score, menu_regle, affichage_score, affichage_regles


#La fonction rejouer permet de demander à l'utilisateur s'il veut rejouer
def rejouer() -> bool:
    """
    Demande à l'utilisateur s'il veut rejouer à un jeu.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.
    
    Returns:
        valeur (bool): True si l'utilisateur veut rejouer, False sinon.
    """

    #Déclaration de la variable
    valeur: bool

    #Demande à l'utilisateur s'il veut rejouer
    valeur = True if input("Voulez-vous rejouer ? (o/N) : ").casefold() == "o" else False
    clear_console()
    return valeur


#Le programme principal
if __name__ == "__main__":
    choix: int
    boucle: bool = True
    boucle_de_jeu: bool = True

    clear_console()

    while boucle:
        choix = menu_principale()

        match choix:
            case 1:
                while boucle_de_jeu:
                    devinette()
                    boucle_de_jeu = rejouer()
                boucle_de_jeu = True
            case 2:
                while boucle_de_jeu:
                    allumettes()
                    boucle_de_jeu = rejouer()
                boucle_de_jeu = True
            case 3:
                while boucle_de_jeu:
                    morpion()
                    boucle_de_jeu = rejouer()
                boucle_de_jeu = True
            case 4: 
                while boucle_de_jeu:
                    match menu_score():
                        case 1:
                            affichage_score("devinettes")
                        case 2:
                            affichage_score("allumettes")
                        case 3:
                            affichage_score("morpion")
                        case 4:
                            boucle_de_jeu = False
                        case _:
                            clear_console()
                            print("Erreur de choix")
                clear_console()
                boucle_de_jeu = True
            case 5:
                while boucle_de_jeu:
                    match menu_regle():
                        case 1:
                            affichage_regles("devinettes")
                        case 2:
                            affichage_regles("allumettes")
                        case 3:
                            affichage_regles("morpion")
                        case 4:
                            boucle_de_jeu = False
                        case _:
                            clear_console()
                            print("Erreur de choix")
                clear_console()
                boucle_de_jeu = True
            case 6:
                boucle = False
            case _:
                clear_console()
                print("Erreur de choix")
    clear_console()
    print("Merci d'avoir joué !")
