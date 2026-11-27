from pathlib import Path

UPDATE = Path(r"")
GAME = Path(r"")

def find_file(relative_path):
    """
    Cherche un fichier du jeu : d'abord dans Update, puis dans Game.
    Renvoie le chemin complet, ou None si introuvable.
    """
    for base in (UPDATE, GAME):
        canditate = base / relative_path
        if canditate.exists():
            return canditate
    return None