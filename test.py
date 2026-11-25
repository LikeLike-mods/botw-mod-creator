import oead
from botwlibs.actorpack import ActorPack
from botwlibs.modbuilder import create_mod_folder

mod_dir = create_mod_folder("MonMod_Epee", "Test : epee du voyageur modifiee")

pack = ActorPack("Weapon_Sword_001")
chemin = "Actor/GeneralParamList/Weapon_Sword_001.bgparamlist"

params = pack.get_params(chemin)
params.objects["Attack"].params["Power"] = oead.S32(50)
pack.set_params(chemin, params)

print("Mod créé dans :", mod_dir)
print("Pack écrit :", pack.save(mod_dir))