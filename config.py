from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_PATH = BASE_DIR / "biblio.db"

MAX_EMPRUNTS = 3

DUREE_EMPRUNT_JOURS = 14