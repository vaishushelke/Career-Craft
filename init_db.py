import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'career_craft_v3.db')

def init():
    print(f"Initializing SQLite database at: {DB_PATH}")
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        ''')

        # Profile Info table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS profile_info (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                name TEXT, email TEXT, phone TEXT, phone2 TEXT, address TEXT,
                linkedin_url TEXT, github_url TEXT, portfolio_url TEXT, summary TEXT,
                theme_color TEXT DEFAULT '#06b6d4',
                title_font_size TEXT DEFAULT '24px',
                subtitle_font_size TEXT DEFAULT '18px',
                text_font_size TEXT DEFAULT '14px',
                font_family TEXT DEFAULT 'Inter',
                template_id INTEGER DEFAULT 1,
                FOREIGN KEY (user_id) REFERENCES users(id)
            )
        ''')

        # Relational tables
        cursor.execute('CREATE TABLE IF NOT EXISTS education (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, degree TEXT, institution TEXT, years TEXT, FOREIGN KEY (user_id) REFERENCES users(id))')
        cursor.execute('CREATE TABLE IF NOT EXISTS experience (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, company TEXT, position TEXT, years TEXT, description TEXT, FOREIGN KEY (user_id) REFERENCES users(id))')
        cursor.execute('CREATE TABLE IF NOT EXISTS skills (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, skill_name TEXT, skill_level TEXT DEFAULT "Intermediate", FOREIGN KEY (user_id) REFERENCES users(id))')
        cursor.execute('CREATE TABLE IF NOT EXISTS awards (id INTEGER PRIMARY KEY AUTOINCREMENT, user_id INTEGER, title TEXT, FOREIGN KEY (user_id) REFERENCES users(id))')
        
        conn.commit()
        conn.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize database. Error: {e}")

if __name__ == '__main__':
    init()
