import oead
from .actorpack import ActorPack
from .weapon_fields import load_fields


_TYPES = {"int": oead.S32, "float": oead.F32, "bool": bool}


def _unwarp(value):
    return getattr(value, "v", value)

class Weapon:
    def __init__(self, name : str):
        self.name = name
        self.pack = ActorPack(name)
        self._path = f"Actor/GeneralParamList/{name}.bgparamlist"
        self._params = self.pack.get_params(self._path)
        self._fields = {f["id"]: f for f in load_fields()}



    def _get(self, field_id) -> bool:
        f = self._fields[field_id]
        value = _unwarp(self._params.objects[f["section"]].params[f["param"]])
        if f["type"] == "int":
            return int(value)
        if f["type"] == "float":
            return float(value)
        return bool(value)

    def _set(self, field_id, value):
        f = self._fields[field_id]
        if f["type"] in ("int", "float"):
            if value < f["min"] or value > f["max"]:
                raise ValueError(f"{f['label']} must be beteen {f['min']} and {f['max']}.")

            value = int(value) if f["type"] == "int" else float(value)
            
        self._params.objects[f["section"]].params[f["param"]] = _TYPES[f["type"]](value)


    def __getattr__(self, name):
        fields = self.__dict__.get("_fields", {})

        if name in fields:
            return self.get(name)
        
        raise AttributeError(name)

    def __setattr__(self, name, value):
        fields = self.__dict__.get("_fields", {})

        if name in fields:
            self._set(name, value)
        else:
            object.__setattr__(self, name, value)


    def describe(self):
        return "\n".join(

            f"{f['label']} : {self._get(fid)}  ({f['description']})"
            for fid, f in self._fields.items()

        )

    def save(self, mod_dir):
        self.pack.set_params(self._path, self._params)
        return self.pack.save(mod_dir)