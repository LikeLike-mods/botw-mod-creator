import oead
from pathlib import Path
from botwlibs.actorpack import ActorPack

pack = ActorPack("Weapon_Sword_001")

chemin = "Actor/GeneralParamList/Weapon_Sword_001.bgparamlist"
params = pack.get_params(chemin)

print("Dégâts actuels :", params.objects["Attack"].params["Power"])

params.objects["Attack"].params["Power"] = oead.S32(50)
pack.set_params(chemin, params)

print("Écrit dans :", pack.save())