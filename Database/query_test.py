import sqlite3

def insertStudentInfo():
    try:
        # Connect to the SQLite database file
        conn = sqlite3.connect("./Database/Yash.sqlite")
        cursor = conn.cursor()
        
        # Parameterized query to insert data into stud_info table
        query = "INSERT INTO stud_info (stud_fnm, stud_lnm, phone, s_date, batch_time) VALUES (?, ?, ?, ?, ?)"
        #cursor.execute(query, (name, surname, phone, date, time))
        #cursor.execute("Delete from stud_info")
        cursor.execute("drop table anki")
        #cursor.execute("drop table sdf")
        # Commit the transaction
        conn.commit()
        print("Data inserted successfully!")

    except sqlite3.Error as e:
        print("Error:", e)
    finally:
        # Close the connection
        conn.close()

# Example usage
# name = input("Enter student's first name: ")
# surname = input("Enter student's last name: ")
# phone = input("Enter student's phone number: ")
# date = input("Enter registration date (YYYY-MM-DD): ")
# time = input("Enter batch time: ")

#insertStudentInfo()

