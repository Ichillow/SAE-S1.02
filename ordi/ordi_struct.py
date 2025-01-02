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
    difficutee: int = -1



class OrdiDevinette1:
    nom: str
    score: float = 0
    triche: int = 0

class OrdiDevinette2:
    nom: str
    score: float = 0
    nbCoups: int = 0