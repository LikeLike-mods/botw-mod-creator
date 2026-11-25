from botwlibs.modbuilder import create_mod_folder
from botwlibs.weapons import Weapon

mod_dir = create_mod_folder("MonMod_Epee", "Test : epee du voyageur modifiee")

arme = Weapon("Weapon_Sword_001")
print("Avant :", arme.attack, arme.durability, arme.sell_price)

arme.attack = 50
arme.durability = 100
arme.sell_price = 9999

print("Après :", arme.attack, arme.durability, arme.sell_price)
print("Écrit :", arme.save(mod_dir))