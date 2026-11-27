import json
from pathlib import Path

_FILE = Path(__file__).parent / "data" / "weapon_fields.json"


def load_fields():
    return json.loads(_FILE.read_text(encoding= "utf-8"))