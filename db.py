import sqlite3
from core.config import DB_PATH

def get_connection():
    """Ouvre la connexion à la base"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Pour récupérer les données comme un dictionnaire
    return conn

def init_db():
    """Crée les tables si elles n'existent pas"""
    conn = get_connection()
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS livres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titre TEXT NOT NULL,
            auteur TEXT NOT NULL,
            stock INTEGER NOT NULL DEFAULT 0
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS adherents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nom TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        )
    """)
    
    conn.execute("""
        CREATE TABLE IF NOT EXISTS emprunts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            adherent_id INTEGER NOT NULL,
            livre_id INTEGER NOT NULL,
            date_emprunt TEXT NOT NULL,
            date_retour_prevue TEXT NOT NULL,
            date_retour_reelle TEXT,
            FOREIGN KEY(adherent_id) REFERENCES adherents(id),
            FOREIGN KEY(livre_id) REFERENCES livres(id)
        )
    """)
    
    conn.commit()
    conn.close()
    print("Base de données prête !")