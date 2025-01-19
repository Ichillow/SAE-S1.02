#Ordi, est la structure de données qui permet de stocker les informations d'un ordinateur dans la base de donnée.
class Ordi:
    id: int
    nom: str
    difficultee: int
    score: float = 0
    nb_parties: int = 0


#JoueurAllumettes
class JoueurAllumettes:
    nom: str
    score: float = 0
    nbAllumettes: int = 0
    nbCoups: int = 0
    difficultee: int = -1

#JoueurMorpion
class JoueurMorpion:
    nom: str
    score: float = 0
    nbCoups: int = 0
    signe: str = ""
    difficultee: int = -1


#OrdiDevinette
class JoueursDevinette:
    nom: str
    difficultee: int = -1