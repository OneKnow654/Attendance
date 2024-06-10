import sqlite3
from cred.kawaii import  *
import csv

import sqlite3
import csv

def fetch_and_save_data():
    try:
          
        conn = sqlite3.connect(get())
        cursor = conn.cursor()

        stud_nm = tget()  
        cursor.execute(f"SELECT * FROM {stud_nm}")
        column_names = [i[0] for i in cursor.description]  # Get column names
        data = cursor.fetchall()

        # Close the connection
        conn.close()

        if data:
            with open(f'{stud_nm}.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                # Write column names
                writer.writerow(column_names)
                # Write data rows
                writer.writerows(data)
            print(f"Data from table {stud_nm} has been saved to CSV.")
        else:
            print(f"No data found in table {stud_nm}.")

    except sqlite3.Error as error:
        print("Error fetching data from SQLite database:", error)




