import sys
sys.path.append("./")

from ordi.ordi_struct import JoueurMorpion

def ordi_morpion_difficile(ordi: JoueurMorpion, grille: list[list[str]]) -> list[list[str]]:
    def is_winner(grille: list[list[str]], signe: str):
        # Vérifie si un joueur a gagné
        return any(
            all(grille[i][j] == signe for j in range(3)) for i in range(3) #Ligne
        ) or any(
            all(grille[i][j] == signe for i in range(3)) for j in range(3) #Colonne
        ) or all(
            grille[i][i] == signe for i in range(3) #Diagonale principale
        ) or all(
            grille[i][2 - i] == signe for i in range(3) #Diagonale secondaire
        )

    def is_full(grille: list[list[str]]):
        # Vérifie si la grille est pleine
        return all(cell != " " for row in grille for cell in row)

    def minimax(grille: list[list[str]], depth: int, is_maximizing: bool):
        # Évalue la meilleure option pour le robot
        if is_winner(grille, ordi.signe):
            return 10 - depth
        if is_winner(grille, "X" if ordi.signe == "O" else "O"):
            return depth - 10
        if is_full(grille):
            return 0

        if is_maximizing:
            best_score = float("-inf")
            for i in range(3):
                for j in range(3):
                    if grille[i][j] == " ":
                        grille[i][j] = ordi.signe
                        score = minimax(grille, depth + 1, False)
                        grille[i][j] = " "
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float("inf")
            for i in range(3):
                for j in range(3):
                    if grille[i][j] == " ":
                        grille[i][j] = "X" if ordi.signe == "O" else "O"
                        score = minimax(grille, depth + 1, True)
                        grille[i][j] = " "
                        best_score = min(best_score, score)
            return best_score


    #Déclaration des variables
    best_move: tuple[int, int]
    best_score: float

    best_move = (-1, -1)
    best_score = float("-inf")

    for i in range(3):
        for j in range(3):
            if grille[i][j] == " ":
                grille[i][j] = ordi.signe
                score = minimax(grille, 0, False)
                grille[i][j] = " "
                if score > best_score:
                    best_score = score
                    best_move = (i, j)

    if best_move != (-1, -1):
        grille[best_move[0]][best_move[1]] = ordi.signe

    return grille