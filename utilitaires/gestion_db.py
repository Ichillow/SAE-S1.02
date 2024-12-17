import sqlite3

# Créer ou ouvrir une base de données nommée 'database.db'
conn = sqlite3.connect('scores.db')

# Créer un curseur pour exécuter des commandes SQL
cursor = conn.cursor()

# Exemple : créer une table
cursor.execute('''
CREATE TABLE IF NOT EXISTS joueur (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nom TEXT NOT NULL,
    score_allumettes INTEGER NOT NULL,
    score_morpion INTEGER NOT NULL,
    score_devinettes INTEGER NOT NULL,
    nb_parties INTEGER NOT NULL
)
''')

# Valider les modifications
conn.commit()

# Fermer la connexion
conn.close()



def connection() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    """
    Fonction pour se connecter à la base de données

    Returns:
        (sqlite3.Connection, sqlite3.Cursor): Retourne la connexion et le curseur.
    """
    # Créer ou ouvrir une base de données nommée 'database.db'
    conn = sqlite3.connect('scores.db')

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




def sauvegarde_score_joueur(nom: str, score_allumettes: int, score_morpion: int, score_devinettes: int, nb_parties: int) -> None:
    """
    Procédure pour sauvegarder le score d'un joueur dans la base de données.

    Args:
        nom (str): Nom du joueur.
        score_allumettes (int): Score du joueur au jeu des allumettes.
        score_morpion (int): Score du joueur au jeu du morpion.
        score_devinettes (int): Score du joueur au jeu des devinettes.
        nb_parties (int): Nombre de parties jouées par le joueur.

    Returns:
        (None): Ne retourne rien.
    """
    # Connexion à la base de données
    conn, cursor = connection()

    # Exemple : insérer une ligne
    cursor.execute('''
    INSERT INTO joueur (nom, score_allumettes, score_morpion, score_devinettes, nb_parties)
    VALUES (?, ?, ?, ?, ?)
    ''', (nom, score_allumettes, score_morpion, score_devinettes, nb_parties))

    # Déconnexion de la base de données
    deconnection(conn)