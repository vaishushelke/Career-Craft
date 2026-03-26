import sqlite3
import os
import time

db_path = os.path.join(os.getcwd(), 'career_craft_v3.db')
print(f"Connecting to {db_path}")

def migrate():
    try:
        conn = sqlite3.connect(db_path, timeout=60)
        cursor = conn.cursor()

        # Fix users table
        cursor.execute("PRAGMA table_info(users)")
        columns = [row[1] for row in cursor.fetchall()]
        print(f"Initial users columns: {columns}")

        if not columns:
            print("Creating users table...")
            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
        elif 'username' not in columns:
            print("Username column missing. Recreating users table...")
            cursor.execute("DROP TABLE users")
            cursor.execute("CREATE TABLE users (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")

        # Fix profile_info
        cursor.execute("PRAGMA table_info(profile_info)")
        p_columns = [row[1] for row in cursor.fetchall()]
        if 'user_id' not in p_columns:
            print("Adding user_id to profile_info...")
            cursor.execute("ALTER TABLE profile_info ADD COLUMN user_id INTEGER UNIQUE REFERENCES users(id)")
        
        # New ATS/Branding columns
        new_profile_cols = {
            'phone2': 'TEXT',
            'theme_color': "TEXT DEFAULT '#06b6d4'",
            'title_font_size': "TEXT DEFAULT '32px'",
            'subtitle_font_size': "TEXT DEFAULT '18px'",
            'text_font_size': "TEXT DEFAULT '14px'"
        }
        for col, col_type in new_profile_cols.items():
            if col not in p_columns:
                print(f"Adding {col} to profile_info...")
                cursor.execute(f"ALTER TABLE profile_info ADD COLUMN {col} {col_type}")

        # Fix others
        for table in ['education', 'experience', 'skills', 'awards']:
            cursor.execute(f"PRAGMA table_info({table})")
            cols = [row[1] for row in cursor.fetchall()]
            if 'user_id' not in cols:
                print(f"Adding user_id to {table}...")
                cursor.execute(f"ALTER TABLE {table} ADD COLUMN user_id INTEGER REFERENCES users(id)")
            
            if table == 'skills' and 'skill_level' not in cols:
                print("Adding skill_level to skills...")
                cursor.execute("ALTER TABLE skills ADD COLUMN skill_level TEXT DEFAULT 'Intermediate'")

        conn.commit()
        conn.close()
        print("Migration completed successfully.")
        return True
    except sqlite3.OperationalError as e:
        print(f"OperationalError: {e}")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

if __name__ == "__main__":
    for i in range(3):
        if migrate():
            # Check schema one last time
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("PRAGMA table_info(users)")
            final_cols = [row[1] for row in cursor.fetchall()]
            print(f"Final users columns: {final_cols}")
            conn.close()
            break
        print("Retrying migration in 2 seconds...")
        time.sleep(2)
