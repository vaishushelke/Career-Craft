import pymysql
import os

def init():
    print("Connecting to MySQL server...")
    try:
        # Connect to MySQL engine without a database specified
        conn = pymysql.connect(host='localhost', user='root', password='')
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS careercraft;")
        conn.commit()
        cursor.close()
        conn.close()
        
        print("Connected! Initializing tables...")
        # Connect to the created database
        conn = pymysql.connect(host='localhost', user='root', password='', database='careercraft')
        cursor = conn.cursor()
        
        with open(os.path.join(os.path.dirname(__file__), 'database.sql'), 'r') as f:
            sql_script = f.read()
            
        # Execute each statement
        for statement in sql_script.split(';'):
            if statement.strip():
                cursor.execute(statement)
                
        conn.commit()
        cursor.close()
        conn.close()
        print("Database initialized successfully!")
    except Exception as e:
        print(f"Failed to initialize database. Make sure MySQL/XAMPP is running. Error: {e}")

if __name__ == '__main__':
    init()
