from pathlib import Path

UPDATE = Path(r"C:\Users\maxch\Documents\nin_games\The Legend of Zelda Breath of the Wild [Update] [0005000e101c9500]\content")
GAME = Path(r"C:\Users\maxch\Documents\nin_games\The Legend of Zelda Breath of the Wild [Game] [00050000101c9500]\content")

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