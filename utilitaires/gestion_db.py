import sqlite3, os
from typing import Optional



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
    # Valider les modifications
    conn.commit()

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


    cursor.execute("""CREATE TABLE IF NOT EXISTS ordi_allumette (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            score INTEGER NOT NULL,
            nb_parties INTEGER NOT NULL
    )
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS ordi_morpion (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            score INTEGER NOT NULL,
            nb_parties INTEGER NOT NULL
    )
    """)

    cursor.execute("""CREATE TABLE IF NOT EXISTS ordi_devinette (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            score INTEGER NOT NULL,
            nb_parties INTEGER NOT NULL
    )
    """)


    cursor.execute("INSERT INTO ordi_allumette (nom, score, nb_parties) VALUES ('Toby', 0, 0);")
    cursor.execute("INSERT INTO ordi_allumette (nom, score, nb_parties) VALUES ('Tim', 0, 0);")
    cursor.execute("INSERT INTO ordi_allumette (nom, score, nb_parties) VALUES ('Lakia', 0, 0);")
    cursor.execute("INSERT INTO ordi_allumette (nom, score, nb_parties) VALUES ('Dixie', 0, 0);")
    cursor.execute("INSERT INTO ordi_allumette (nom, score, nb_parties) VALUES ('Patrick', 0, 0);")
    cursor.execute("INSERT INTO ordi_allumette (nom, score, nb_parties) VALUES ('Charles', 0, 0);")

    cursor.execute("INSERT INTO ordi_morpion (nom, score, nb_parties) VALUES ('Waldo', 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, score, nb_parties) VALUES ('Frasier', 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, score, nb_parties) VALUES ('Jefferson', 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, score, nb_parties) VALUES ('Corby', 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, score, nb_parties) VALUES ('Rex', 0, 0);")
    cursor.execute("INSERT INTO ordi_morpion (nom, score, nb_parties) VALUES ('Baba', 0, 0);")

    cursor.execute("INSERT INTO ordi_devinette (nom, score, nb_parties) VALUES ('Jacob', 0, 0);")
    cursor.execute("INSERT INTO ordi_devinette (nom, score, nb_parties) VALUES ('Linda', 0, 0);")
    cursor.execute("INSERT INTO ordi_devinette (nom, score, nb_parties) VALUES ('Louis', 0, 0);")
    cursor.execute("INSERT INTO ordi_devinette (nom, score, nb_parties) VALUES ('Joel', 0, 0);")
    cursor.execute("INSERT INTO ordi_devinette (nom, score, nb_parties) VALUES ('William', 0, 0);")
    cursor.execute("INSERT INTO ordi_devinette (nom, score, nb_parties) VALUES ('Ernestine', 0, 0);")


    conn.commit()


    deconnection(conn)