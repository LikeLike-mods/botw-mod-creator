import oead
from botwlibs.actorpack import SORTIE

chemin = SORTIE / "Weapon_Sword_001.sbactorpack"
archive = oead.Sarc(oead.yaz0.decompress(chemin.read_bytes()))

nom = "Actor/GeneralParamList/Weapon_Sword_001.bgparamlist"
params = oead.aamp.ParameterIO.from_binary(bytes(archive.get_file(nom).data))

print("Dégâts dans le mod :", params.objects["Attack"].params["Power"])