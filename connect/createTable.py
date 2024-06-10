from connect.fetch import con
from cred.kawaii import get
from UI.displayData import populate

def create_table(name, surname, phone,date,time):
    conn = con(get())
    c = conn.cursor()
    # Create a table if it doesn't exist
    c.execute(f'''CREATE TABLE IF NOT EXISTS {name}
                 (id int AUTO_INCREMENT PRIMARY KEY,status TEXT,Date_Time TEXT,Week Text)''')

    query = "INSERT INTO stud_info (stud_fnm, stud_lnm, phone, s_date, batch_time) VALUES (?, ?, ?, ?, ?)"
    c.execute(query, (name, surname, phone, date, time))
        
    # Commit the transaction
    conn.commit()
    # Commit changes and close connection
    populate()
    conn.commit()
    conn.close()

