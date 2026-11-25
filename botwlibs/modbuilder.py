from pathlib import Path

OUTPUT = Path(r"C:\Users\maxch\Documents\Mcreator Botw\sortie")

TITLE_IDS = "00050000101C9300,00050000101C9400,00050000101C9500"


def create_mod_folder(mod_name, description = ""):
    mod_dir = OUTPUT / mod_name
    (mod_dir / "content" / "Actor" / "Pack").mkdir(parents = True, exist_ok = True)

    rules = "\n".join([
        "[Definition]",
        f"titleIds = {TITLE_IDS}",
        f"name = {mod_name}",
        f"path = The Legend of Zelda: Breath of the Wild/Mods/{mod_name}",
        f"description = {description}",
        "version = 7",
        "default = false",
    ])

    (mod_dir / "rules.txt").write_text(rules, encoding = "utf-8")
    return mod_dir