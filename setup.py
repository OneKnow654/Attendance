import sqlite3
from cred.kawaii import load_data


def create_database():
    

    # Connect to or create the SQLite database
    conn = sqlite3.connect(load_data()[0])
    cursor = conn.cursor()

    # Create the 'admin' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username VARCHAR(20),
                        password VARCHAR(50)
                    )''')
    
    #cursor.execute("ALTER TABLE {table_name} ADD COLUMN week text")

    # Commit changes and close the connection
    conn.commit()
    conn.close()



create_database()