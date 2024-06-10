from connect import fetch,database_fetch
from cred.kawaii import *

from tkinter import *

def getDetail():
    db = fetch.con(get())
    cur = db.cursor()
    cur.execute(f"select * from stud_info  where stud_fnm='{tget()}'")
    data=cur.fetchone()
    db.commit()
    db.close()
    return data 
    
def detail_info(data:tuple):
    str = f"""
    Name          : {data[1]}
    Surname       : {data[2]} 
    Phone number  : {data[3]} 
    Strating Date : {data[4]}
    time          : {data[5]}
    """
    
    return str

def disp_box(win):
    def save():
        database_fetch.fetch_and_save_data()
        msg.config(text="save successfull ",fg="green" )

    root = Toplevel(win)
    root.title("Student Information")
    root.geometry("500x400")
    
    c = Label(root,text=detail_info(getDetail()),font=("Arial",18)).pack(side="top")
    b = Button(root, text="Close",command=lambda:root.destroy()).pack(side=BOTTOM)
    b1 = Button(root, text="save",command=lambda:save()).pack(side=BOTTOM,pady=2)
    msg=Label(root)
    msg.pack()

    root.mainloop()
