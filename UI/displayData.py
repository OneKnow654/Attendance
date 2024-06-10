from tkinter import *
from connect import fetch
from cred.kawaii import get,tset

def filter(data):
    for item in data:
        listbox.insert(END, item[0])

def populate():
    listbox.delete(0, END)
    db = fetch.con(get())
    print(get())
    cur = db.cursor()
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%'; ")
    result=cur.fetchall()
    filter(result)
    cur.close()
    

def listBar(win):

    def on_item_select(event):#database
        try:
            selected_item = listbox.get(listbox.curselection())
            print(selected_item)
            tset(selected_item)
        except Exception as e :
            #print("list on db",e)
            pass
    global listbox
    listbox = Listbox(win, font=('Arial', 14),width=30,height=35)
    listbox.pack(pady=0,side="right")
    
    populate()
    listbox.bind('<<ListboxSelect>>', on_item_select)
    