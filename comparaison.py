from pathlib import Path

GAME = Path(r"C:\Users\maxch\Documents\nin_games\The Legend of Zelda Breath of the Wild [Game] [00050000101c9500]\content")
UPDATE = Path(r"C:\Users\maxch\Documents\nin_games\The Legend of Zelda Breath of the Wild [Update] [0005000e101c9500]\content")

def compter(dossier):
    return sum(1 for f in dossier.rglob("*") if f.is_file())

for nom in sorted({p.name for p in GAME.iterdir()} | {p.name for p in UPDATE.iterdir()}):
    g = compter(GAME / nom) if (GAME / nom).exists() else 0
    u = compter(UPDATE / nom) if (UPDATE / nom).exists() else 0
    print(f"{nom:12} Game: {g:6}   Update: {u:6}")