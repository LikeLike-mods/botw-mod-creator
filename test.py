from botwlibs.modbuilder import create_mod_folder
from botwlibs.weapons import Weapon

mod_dir = create_mod_folder("MonMod_Epee", "Test : epee du voyageur modifiee")

arme = Weapon("Weapon_Sword_001")
print("=== Avant ===")
print(arme.describe())

arme.attack = 50
arme.durability = 100

print()
print("=== Après ===")
print(arme.describe())
print()
print("Écrit :", arme.save(mod_dir))