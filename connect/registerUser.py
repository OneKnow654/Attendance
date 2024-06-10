
def create_db_table(dbname):
    import sqlite3
    conn = sqlite3.connect(f"./Database/{dbname}.sqlite")
    cursor = conn.cursor()
   
    # Create the 'stud_info' table
    cursor.execute('''CREATE TABLE IF NOT EXISTS stud_info (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        stud_fnm VARCHAR(255),
                        stud_lnm VARCHAR(255),
                        phone VARCHAR(255),
                        s_date VARCHAR(255),
                        batch_time VARCHAR(30)
                    )''')

    # Commit changes and close the connection
    conn.commit()
    conn.close()


def generate(word):
    encrypt = ""
    for i in word:
        if ord(i) >=97 and ord(i) <= 122:
            encrypt +=chr(ord(i)-3)
        elif ord(i) >= 65 and ord(i) <= 90:
            encrypt +=chr(ord(i)+3)
        else:
            encrypt +=chr(ord(i)-3)

    return encrypt

def decode(word):
    encrypt = ""
    for i in word:
        if ord(i) >=97 and ord(i) <= 122:
            encrypt +=chr(ord(i)+3)
        elif ord(i) >= 65 and ord(i) <= 90:
            encrypt +=chr(ord(i)-3)
        else:
            encrypt +=chr(ord(i)+3)


    return encrypt


    
def createUser():
    import sqlite3
    from cred.kawaii import load_data
    
    username = input("Enter username: ")
    password = input("Enter password: ")
    try:
         db = sqlite3.connect(load_data()[0])
         cur = db.cursor()
         if username and password:
            cur.execute("insert into admin(username,password) values(?,?)",(username,generate(password)))
            db.commit()
            db.close()
            create_db_table(username)
            print("user has been created:")
            
    except Exception as e:
        print(e)
    
    

    
    

def create_code():
    num = input("How many characters do you want? ")
    st = ""
    
    for i in range(len(num)):
        st+=f"chr({ord(num[i])})+"
        
    print(st[:-1])
        
#create_code()

        
#createUser()