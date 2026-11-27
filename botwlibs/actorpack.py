from pathlib import Path
import oead

from .paths import find_file
from .modbuilder import create_mod_folder

OUTPUT = Path(r"")

class ActorPack:
    def __init__(self, name):
        """
        Prends le param 'name'
        """
        self.name = name

        path = find_file(f"Actor/Pack/{name}.sbactorpack")
        if path is None:
            raise FileNotFoundError(f"Pack introuvable : {name}")

        self.archive = oead.Sarc(oead.yaz0.decompress(path.read_bytes()))
        self.writer = oead.SarcWriter.from_sarc(self.archive)


    def get_params(self, internal_path : Path):
        """
        Lit un fichier de params AAMP à l'interieur du pack
        """
        data = bytes(self.archive.get_file(internal_path).data)
        return oead.aamp.ParameterIO.from_binary(data)

    def set_params(self, internal_path : Path, params):
        """
        Remplace un fichier de paramètres dans le pack (en mémoire)
        """
        self.writer.files[internal_path] = params.to_binary()

    def save(self, mod_dir = None):
        """
        Save the file
        """
        if mod_dir is None:
            dest = OUTPUT
        else:
            dest = Path(mod_dir) / "content" / "Actor" / "Pack"
        dest.mkdir(parents=True, exist_ok= True)
        
        alignment, data = self.writer.write()
        out = dest / f"{self.name}.sbactorpack"
        out.write_bytes(oead.yaz0.compress(data, alignment))
        return out