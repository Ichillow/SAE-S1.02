#Ordi, est la structure de données qui permet de stocker les informations d'un ordinateur dans la base de donnée.
class Ordi:
    id: int
    nom: str
    difficultee: int
    score: float = 0
    nb_parties: int = 0


#OrdiMorpion
class JoueurMorpion:
    nom: str
    score: float = 0
    nbCoups: int = 0
    signe: str = ""
    difficultee: int = -1


#OrdiDevinette(Fait deviner)
class JoueursDevinette:
    nom: str
    difficultee: int = -1
