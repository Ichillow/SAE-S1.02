import sys
sys.path.append("./")

from jeux.morpion import morpion

from jeux.allumettes import allumettes

from ordi.ordi_struct import Ordi

from utilitaires.utils import charger_ordi_jeu

import time


def benchmarck() -> None:
    """
    Cette fonction est la fonction principale du benchmarck. Elle permet de comparer les performances des différents jeux.

    Args:
        (None): Aucun argument n'est nécessaire pour cette fonction.

    Returns:
        (None): Cette fonction ne retourne rien.
    """
    
    #Déclaration des variables à utilisé
    ordisMorpion: list[tuple[int, str, int, float, int]] = charger_ordi_jeu("morpion", False)
    ordisAllumettes: list[tuple[int, str, int, float, int]] = charger_ordi_jeu("allumettes", False)

    info_benckmarck_morpion: tuple[Ordi, Ordi]
    info_benckmarck_allumettes: tuple[Ordi, Ordi]

    ordi1Morpion: Ordi = Ordi()
    ordi1Morpion.nom = ordisMorpion[0][1]
    ordi1Morpion.difficultee = ordisMorpion[0][2]

    ordi2Morpion: Ordi = Ordi()
    ordi2Morpion.nom = ordisMorpion[5][1]
    ordi2Morpion.difficultee = ordisMorpion[5][2]

    ordi1Allumettes: Ordi = Ordi()
    ordi1Allumettes.nom = ordisAllumettes[0][1]
    ordi1Allumettes.difficultee = ordisAllumettes[0][2]

    ordi2Allumettes: Ordi = Ordi()
    ordi2Allumettes.nom = ordisAllumettes[5][1]
    ordi2Allumettes.difficultee = ordisAllumettes[5][2]


    info_benckmarck_allumettes = (ordi2Allumettes, ordi1Allumettes)

    info_benckmarck_morpion = (ordi2Morpion, ordi1Morpion)

    
    chemainFichierMorpion: str = "./benchmarck/morpion.txt"
    chemainFichierAllumettes: str = "./benchmarck/allumettes.txt"
    chemainFichierMorpionGagnant: str = "./benchmarck/morpion_gagnant.txt"
    chemainFichierAllumettesGagnant: str = "./benchmarck/allumettes_gagnant.txt"
    chemainFichierMorpionTemps: str = "./benchmarck/morpion_temps.txt"
    chemainFichierAllumettesTemps: str = "./benchmarck/allumettes_temps.txt"

    tableauMorpion: list[str] = []
    tableauAllumettes: list[str] = []


    tabelauGagnantMorpion: list[str] = []
    tabelauGagnantAllumettes: list[str] = []

    tableauTempsMorpion: list[str] = []
    tableauTempsAllumettes: list[str] = []

    tempsDebut: float = 0
    tempsFin: float = 0

    #Début du benchmarck

    #On vide les fichiers
    with open(chemainFichierMorpion, "w") as fichier:
        fichier.write("")
    
    with open(chemainFichierAllumettes, "w") as fichier:
        fichier.write("")
    
    with open(chemainFichierMorpionGagnant, "w") as fichier:
        fichier.write("")

    with open(chemainFichierAllumettesGagnant, "w") as fichier:
        fichier.write("")
    
    with open(chemainFichierMorpionTemps, "w") as fichier:
        fichier.write("")
    
    with open(chemainFichierAllumettesTemps, "w") as fichier:
        fichier.write("")


    #Boucle pour le jeu du morpion
    for i in range(0, 10000):
        tempsDebut = time.time()
        recup_info = morpion(info_benckmarck_morpion)
        tempsFin = time.time()
        tableauMorpion.append(f"{recup_info[0]},{recup_info[1]}\n")
        tabelauGagnantMorpion.append(f"{recup_info[2]}\n")
        tableauTempsMorpion.append(f"{tempsFin - tempsDebut}\n")
    
    #Écriture des résultats dans les fichiers
    with open(chemainFichierMorpion, "w") as fichier:
        for ligne in tableauMorpion:
            fichier.write(ligne)
    
    with open(chemainFichierMorpionGagnant, "w") as fichier:
        for ligne in tabelauGagnantMorpion:
            fichier.write(ligne)

    #Écriture des résultats dans les fichiers
    with open(chemainFichierMorpionTemps, "w") as fichier:
        for ligne in tableauTempsMorpion:
            fichier.write(ligne)


    #Boucle pour le jeu des allumettes
    for i in range(0, 10000):
        timeDebut = time.time()
        recup_info = allumettes(info_benckmarck_allumettes)
        timeFin = time.time()
        tableauAllumettes.append(f"{recup_info[0]},{recup_info[1]}\n")
        tabelauGagnantAllumettes.append(f"{recup_info[2]}\n")
        tableauTempsAllumettes.append(f"{timeFin - timeDebut}\n")
    
    #Écriture des résultats dans les fichiers
    with open(chemainFichierAllumettes, "w") as fichier:
        for ligne in tableauAllumettes:
            fichier.write(ligne)

    #Écriture des résultats dans les fichiers
    with open(chemainFichierAllumettesGagnant, "w") as fichier:
        for ligne in tabelauGagnantAllumettes:
            fichier.write(ligne)
    
    #Écriture des résultats dans les fichiers
    with open(chemainFichierAllumettesTemps, "w") as fichier:
        for ligne in tableauTempsAllumettes:
            fichier.write(ligne)



    return None



def affichage_infos() -> None:

    #Pour le jeu du morpion
    chemainFichierMorpion: str = "./benchmarck/morpion.txt"
    chemainFichierMorpionGagnant: str = "./benchmarck/morpion_gagnant.txt"
    chemainFichierMorpionTemps: str = "./benchmarck/morpion_temps.txt"

    tableauMorpion: list[str] = []
    tableauMorpionGagnant: list[str] = []
    tableauMorpionTemps: list[str] = []

    moyenneOrdi1: float = 0
    moyenneOrdi2: float = 0

    pourcentageOrdi1: float = 0
    pourcentageOrdi2: float = 0

    tempsMoyen: float = 0

    with open(chemainFichierMorpion, "r") as fichier:
        tableauMorpion: list[str] = fichier.readlines()
    
    with open(chemainFichierMorpionGagnant, "r") as fichier:
        tableauMorpionGagnant: list[str] = fichier.readlines()

    with open(chemainFichierMorpionTemps, "r") as fichier:
        tableauMorpionTemps: list[str] = fichier.readlines()

    #Calcul des moyennes
    for ligne in tableauMorpion:
        ligne = ligne.split(",")
        moyenneOrdi1 += float(ligne[0])
        moyenneOrdi2 += float(ligne[1])
    
    moyenneOrdi1 /= len(tableauMorpion)
    moyenneOrdi2 /= len(tableauMorpion)

    #Calcul des pourcentages
    for ligne in tableauMorpionGagnant:
        if ligne == "Baba\n":
            pourcentageOrdi1 += 1
        else:
            pourcentageOrdi2 += 1

    pourcentageOrdi1 /= len(tableauMorpionGagnant)
    pourcentageOrdi2 /= len(tableauMorpionGagnant)

    #Calcul des temps moyens
    for ligne in tableauMorpionTemps:
        tempsMoyen += float(ligne)
    
    tempsMoyen /= len(tableauMorpionTemps)

    #Arrondi des valeurs
    moyenneOrdi1 = round(moyenneOrdi1, 3)
    moyenneOrdi2 = round(moyenneOrdi2, 3)
    pourcentageOrdi1 = round(pourcentageOrdi1, 3)
    pourcentageOrdi2 = round(pourcentageOrdi2, 3)
    tempsMoyen = round(tempsMoyen, 9)

    print()
    print("Morpion:")
    print()
    print(f"Ordi Difficile: {moyenneOrdi1}")
    print(f"Ordi Facile: {moyenneOrdi2}")
    print()
    print(f"Pourcentage Ordi Difficile: {pourcentageOrdi1}")
    print(f"Pourcentage Ordi Facile: {pourcentageOrdi2}")
    print()
    print(f"Temps moyen: {tempsMoyen}")
    print()

    #Pour le jeu des allumettes
    chemainFichierAllumettes: str = "./benchmarck/allumettes.txt"
    chemainFichierAllumettesGagnant: str = "./benchmarck/allumettes_gagnant.txt"
    chemainFichierAllumettesTemps: str = "./benchmarck/allumettes_temps.txt"

    tableauAllumettes: list[str] = []
    tableauAllumettesGagnant: list[str] = []
    tableauAllumettesTemps: list[str] = []

    moyenneOrdi1: float = 0
    moyenneOrdi2: float = 0

    pourcentageOrdi1: float = 0
    pourcentageOrdi2: float = 0

    tempsMoyen: float = 0

    with open(chemainFichierAllumettes, "r") as fichier:
        tableauAllumettes: list[str] = fichier.readlines()

    with open(chemainFichierAllumettesGagnant, "r") as fichier:
        tableauAllumettesGagnant: list[str] = fichier.readlines()

    with open(chemainFichierAllumettesTemps, "r") as fichier:
        tableauAllumettesTemps: list[str] = fichier.readlines()

    #Calcul des moyennes
    for ligne in tableauAllumettes:
        ligne = ligne.split(",")
        moyenneOrdi1 += float(ligne[0])
        moyenneOrdi2 += float(ligne[1])

    moyenneOrdi1 /= len(tableauAllumettes)
    moyenneOrdi2 /= len(tableauAllumettes)

    #Calcul des pourcentages
    for ligne in tableauAllumettesGagnant:
        if ligne == "Charles\n":
            pourcentageOrdi1 += 1
        else:
            pourcentageOrdi2 += 1

    pourcentageOrdi1 /= len(tableauAllumettesGagnant)
    pourcentageOrdi2 /= len(tableauAllumettesGagnant)

    #Calcul des temps moyens
    for ligne in tableauAllumettesTemps:
        tempsMoyen += float(ligne)

    tempsMoyen /= len(tableauAllumettesTemps)

    #Arrondi des valeurs
    moyenneOrdi1 = round(moyenneOrdi1, 3)
    moyenneOrdi2 = round(moyenneOrdi2, 3)
    pourcentageOrdi1 = round(pourcentageOrdi1, 3)
    pourcentageOrdi2 = round(pourcentageOrdi2, 3)
    tempsMoyen = round(tempsMoyen, 9)

    print("---------------------------------")
    print()
    print("Allumettes:")
    print()
    print(f"Ordi Difficile: {moyenneOrdi1}")
    print(f"Ordi Facile: {moyenneOrdi2}")
    print()
    print(f"Pourcentage Ordi Difficile: {pourcentageOrdi1}")
    print(f"Pourcentage Ordi Facile: {pourcentageOrdi2}")
    print()
    print(f"Temps moyen: {tempsMoyen}")
    print()





if __name__ == "__main__":
    benchmarck()
    affichage_infos()