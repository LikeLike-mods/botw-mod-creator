import oead
from .actorpack import ActorPack

def _unwarp(value):
    return getattr(value, "v", value)

class Weapon:
    def __init__(self, name : str):
        self.name = name
        self.pack = ActorPack(name)
        self._path = f"Actor/GeneralParamList/{name}.bgparamlist"
        self._params = self.pack.get_params(self._path)


    def _get(self, section, key):
        return int(_unwarp(self._params.objects[section].params[key]))

    def _set(self, section, key, value):
        self._params.objects[section].params[key] = oead.S32(int(value))



    @property
    def attack(self):
        return self._get("Attack", "Power")

    @property
    def durability(self):
        return self._get("General", "Life")

    @property
    def sell_price(self):
        return self._get("Item", "SellingPrice")

    @attack.setter
    def attack(self, value):
        if value < 0:
            raise ValueError
        self._set("Attack", "Power", value)

    @durability.setter
    def durability(self, value):
        if value < 1:
            raise ValueError
        self._set("General", "Life", value)

    @sell_price.setter
    def sell_price(self, value):
        if value < 0:
            raise ValueError
        self._set("Item", "SellingPrice", value)

    def save(self, mod_dir):
        self.pack.set_params(self._path, self._params)
        return self.pack.save(mod_dir)