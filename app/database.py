import sqlite3
import os

def get_db():
    db_path = 'api.db'
    if os.environ.get('VERCEL'):
        db_path = '/tmp/api.db'
        
    db = sqlite3.connect(db_path)
    db.row_factory = sqlite3.Row
    
    # Auto-génération de la table posts si manquante
    db.execute('''
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            body TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()
    return db

