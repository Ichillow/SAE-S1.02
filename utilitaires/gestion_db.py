import sqlite3, os



def connection() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Fonction pour se connecter à la base de données

    Returns:
        (sqlite3.Connection, sqlite3.Cursor): Retourne la connexion et le curseur.
    """

    #Déclaration des variables
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
    chemin_db: str = os.getcwd() + '/scores/scores.db'

    # Créer ou ouvrir une base de données nommée 'database.db'
    conn = sqlite3.connect(chemin_db)

    # Créer un curseur pour exécuter des commandes SQL
    cursor = conn.cursor()

    return conn, cursor


def deconnection(conn: sqlite3.Connection) -> None:
    """
    Procédure pour se déconnecter de la base de données

    Args:
        conn (sqlite3.Connection): Connexion à la base de données.

    Returns:
        (None): Ne retourne rien.
    """

    # Fermer la connexion
    conn.close()


def create_table() -> None:

    conn, cursor = connection()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS joueur (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        score_allumettes INTEGER NOT NULL,
        score_morpion INTEGER NOT NULL,
        score_devinettes INTEGER NOT NULL,
        nb_parties INTEGER NOT NULL
    )
    """)


    cursor.execute("""CREATE TABLE IF NOT EXISTS ordi_allumettes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            difficulte INTEGER NOT NULL,
            score INTEGER NOT NULL,
            nb_parties INTEGER NOT NULL
    )
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS ordi_morpion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            difficulte INTEGER NOT NULL,
            score INTEGER NOT NULL,
            nb_parties INTEGER NOT NULL
    )
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS ordi_devinettes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            difficulte INTEGER NOT NULL,
            score INTEGER NOT NULL,
            nb_parties INTEGER NOT NULL
    )
    """)


    cursor.execute("INSERT INTO ordi_allumettes (nom, difficulte, score, nb_parties) VALUES ('Toby', 1, 0, 0);")
    cursor.execute("INSERT INTO ordi_allumettes (nom, difficulte, score, nb_parties) VALUES ('Tim', 1, 0, 0);")
    cursor.execute("INSERT INTO ordi_allumettes (nom, difficulte, score, nb_parties) VALUES ('Lakia', 2, 0, 0);")
    cursor.execute("INSERT INTO ordi_allumettes (nom, difficulte, score, nb_parties) VALUES ('Dixie', 2, 0, 0);")
    cursor.execute("INSERT INTO ordi_allumettes (nom, difficulte, score, nb_parties) VALUES ('Patrick', 3, 0, 0);")
    cursor.execute("INSERT INTO ordi_allumettes (nom, difficulte, score, nb_parties) VALUES ('Charles', 3, 0, 0);")

    cursor.execute("INSERT INTO ordi_morpion (nom, difficulte, score, nb_parties) VALUES ('Waldo', 1, 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, difficulte, score, nb_parties) VALUES ('Frasier', 1, 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, difficulte, score, nb_parties) VALUES ('Jefferson', 2, 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, difficulte, score, nb_parties) VALUES ('Corby', 2, 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, difficulte, score, nb_parties) VALUES ('Rex', 3, 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, difficulte, score, nb_parties) VALUES ('Baba', 3, 0, 0);")

    cursor.execute("INSERT INTO ordi_devinettes (nom, difficulte, score, nb_parties) VALUES ('Jacob', 1, 0, 0);")
    cursor.execute("INSERT INTO ordi_devinettes (nom, difficulte, score, nb_parties) VALUES ('Linda', 1, 0, 0);")
    cursor.execute("INSERT INTO ordi_devinettes (nom, difficulte, score, nb_parties) VALUES ('Louis', 2, 0, 0);")
    cursor.execute("INSERT INTO ordi_devinettes (nom, difficulte, score, nb_parties) VALUES ('Joel', 2, 0, 0);")
    cursor.execute("INSERT INTO ordi_devinettes (nom, difficulte, score, nb_parties) VALUES ('William', 3, 0, 0);")
    cursor.execute("INSERT INTO ordi_devinettes (nom, difficulte, score, nb_parties) VALUES ('Ernestine', 3, 0, 0);")


    conn.commit()


    deconnection(conn)



#La fonction sauvegarde_score_joueur permet de sauvegarder les scores des joueurs dans la base de données
def sauvegarde_score_joueur(jeu:str, joueur:str, valeur:float) -> None:
    """
    Procédure pour sauvegarder les scores d'un joueur

    Args:
        jeu(str): Nom du jeu.
        joueur(str): Nom du joueur.
        valeur(float): Valeur du score.

    Returns:
        (None) : Ne retourne rien.
    """

    #Déclaration des variables
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    #Vérification de l'existence du jeu
    if jeu not in ["allumettes", "morpion", "devinettes"]:
        raise NameError("Le jeu n'existe pas")

    #Connexion à la base de données
    conn, cursor = connection()


    #Vérification de l'existence du joueur, et ajout si nécessaire
    cursor.execute(f"SELECT COUNT(*) FROM joueur WHERE nom = '{joueur}'")
    if cursor.fetchone()[0] == 0:
        cursor.execute(f"INSERT INTO joueur (nom, score_allumettes, score_morpion, score_devinettes, nb_parties) VALUES ('{joueur}', 0, 0, 0, 0)")


    #Mise à jour du score
    if jeu == "allumettes":
        cursor.execute(f"UPDATE joueur SET score_allumettes = score_allumettes + {valeur}, nb_parties = nb_parties + 1 WHERE nom = '{joueur}'")
    elif jeu == "morpion":
        cursor.execute(f"UPDATE joueur SET score_morpion = score_morpion + {valeur}, nb_parties = nb_parties + 1 WHERE nom = '{joueur}'")
    elif jeu == "devinettes":
        cursor.execute(f"UPDATE joueur SET score_devinettes = score_devinettes + {valeur}, nb_parties = nb_parties + 1 WHERE nom = '{joueur}'")

    conn.commit()

    deconnection(conn)


#La fonction sauvagarde_score_ordi permet de sauvegarder les scores des ordinateurs dans la base de données
def sauvegarde_score_ordi(jeu:str, ordi:str, valeur:float) -> None:
    """
    Procédure pour sauvegarder les scores d'un ordinateur

    Args:
        jeu(str): Nom du jeu.
        ordi(str): Nom de l'ordinateur.
        valeur(float): Valeur du score.

    Returns:
        (None) : Ne retourne rien.
    """

    #Déclaration des variables
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
    ordis: list[tuple[int, str, int, int, int]]

    #Vérification de l'existence du jeu
    if jeu not in ["allumettes", "morpion", "devinettes"]:
        raise NameError("Le jeu n'existe pas")


    #Vérification de l'existence de l'ordinateur
    if jeu == "allumettes":
        ordis = charger_ordi_jeu("allumettes")
    elif jeu == "morpion":
        ordis = charger_ordi_jeu("morpion")
    elif jeu == "devinettes":
        ordis = charger_ordi_jeu("devinettes")
    else:
        ordis = []

    if ordi not in [ordi_[1] for ordi_ in ordis]:
        return None



    #Connexion à la base de données
    conn, cursor = connection()


    #Mise à jour du score
    cursor.execute(f"UPDATE ordi_{jeu} SET score = score + {valeur}, nb_parties = nb_parties + 1 WHERE nom = '{ordi}'")

    conn.commit()

    deconnection(conn)


#La fonction charger_score permet de charger les scores des joueurs dans la base de données, en fonction d'un jeu
def charger_joueurs_jeu(jeu:str) -> list[tuple[int, str, int, int, int, int]]:
    """
    Fonction pour charger les scores des joueurs d'un jeu en particulier

    Args:
        jeu(str): Nom du jeu.

    Returns:
        (list): Retourne la liste des scores des joueurs.
    """

    #Déclaration des variables
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
    scores: list[tuple[int, str, int, int, int, int]]

    #Vérification de l'existence du jeu
    if jeu not in ["allumettes", "morpion", "devinettes"]:
        raise NameError("Le jeu n'existe pas")

    #Connexion à la base de données
    conn, cursor = connection()

    #Chargement des scores
    cursor.execute(f"SELECT * FROM joueur ORDER BY score_{jeu} DESC")
    scores = cursor.fetchall()

    deconnection(conn)

    return scores


#La fonction charger_score permet de charger les scores des ordinateurs dans la base de données, en fonction d'un jeu
def charger_ordi_jeu(jeu:str) -> list[tuple[int, str, int, int, int]]:
    """
    Fonction pour charger les scores des ordinateurs d'un jeu en particulier

    Args:
        jeu(str): Nom du jeu.

    Returns:
        (list): Retourne la liste des scores des ordinateurs.
    """

    #Déclaration des variables
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor
    scores: list[tuple[int, str, int, int, int]]

    #Vérification de l'existence du jeu
    if jeu not in ["allumettes", "morpion", "devinettes"]:
        raise NameError("Le jeu n'existe pas")

    #Connexion à la base de données
    conn, cursor = connection()

    #Chargement des scores
    cursor.execute(f"SELECT * FROM ordi_{jeu} ORDER BY score DESC")
    scores = cursor.fetchall()

    deconnection(conn)

    return scores






######################################################################
#                  Fonctions pour le developpement                   #
######################################################################



#La fonction reset_scores permet de réinitialiser les scores des joueurs et des ordinateurs
def reset_db() -> None:
    """
    Procédure pour réinitialiser les scores

    Args:
        (None): Ne prend pas de paramètres.

    Returns:
        (None): Ne retourne rien.
    """

    #Déclaration des variables
    conn: sqlite3.Connection
    cursor: sqlite3.Cursor

    #Connexion à la base de données
    conn, cursor = connection()

    #Réinitialisation des joueurs
    cursor.execute("DELETE FROM joueur")

    #Réinitialisation des ordinateurs
    cursor.execute("DROP TABLE ordi_allumettes")
    cursor.execute("DROP TABLE ordi_morpion")
    cursor.execute("DROP TABLE ordi_devinettes")

    conn.commit()

    deconnection(conn)

    create_table()


