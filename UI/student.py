from tkinter import ttk,Toplevel
from connect import createTable,fetch
import datetime as dt
from cred.kawaii import * 



def remove_all_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()



def open_new_student_window(win):
    def save_student_info():
        name = name_entry.get()
        surname = surname_entry.get()
        phone = phone_entry.get()
        date = cal.get()
        time = time_entry.get()
        createTable.create_table(name, surname, phone,date ,time)
        
    
    new_student_window = Toplevel(win)
    new_student_window.geometry("400x300")
    new_student_window.title("New Student")
    

    # Name Entry
    ttk.Label(new_student_window, text="Name:").pack()
    name_entry = ttk.Entry(new_student_window)
    name_entry.pack()

    # Surname Entry
    ttk.Label(new_student_window, text="Surname:").pack()
    surname_entry = ttk.Entry(new_student_window)
    surname_entry.pack()

    # Phone Entry
    ttk.Label(new_student_window, text="Phone:").pack()
    phone_entry = ttk.Entry(new_student_window)
    phone_entry.pack()

    # Date Entry
    ttk.Label(new_student_window, text="Date:").pack()
    cal = ttk.Entry(new_student_window)
    cal.pack()

    # Time Entry 
    ttk.Label(new_student_window, text="Time:").pack()
    time_entry = ttk.Entry(new_student_window)
    time_entry.pack()

    # Save Button
    save_button = ttk.Button(new_student_window, text="Save", command=save_student_info)
    save_button.pack()

    new_student_window.mainloop()

def current_datetime():
    x = dt.datetime.now()
    cdt = x.date() + x.time().replace(microsecond=0)
    return str(cdt)

def abset(mod=1,datetime=f"{dt.datetime.now().date()}[{dt.datetime.now().time().replace(microsecond=0)}]",week = None):
    db = fetch.con(get())
    c = db.cursor()
    if mod==1:
        c.execute(f"insert into {tget()}(status,date_time) values('Absent','{datetime}');")
    elif mod==2:
        c.execute(f"insert into {tget()}(status,date_time) values('Absent','{datetime}');")
    elif mod == 3:
        c.execute(f"insert into {tget()}(status,date_time,week) values('Absent','{datetime}','{week}');")
    db.commit()
    db.close()

def custom_absent(win):
    main_win = Toplevel(win)
    main_win.geometry("400x400+500+150")
    main_win.title("Custom Absent")

    small_win = ttk.Frame(main_win, height=400, width=400)
    small_win.pack()

    small2_win = ttk.Frame(main_win, height=400, width=400)
    small2_win.pack()

    # Function to switch to the first frame
    def show_first_frame():
        small_win.pack()
        small2_win.pack_forget()
    def show_second_frame():
        small2_win.pack()
        small_win.pack_forget()

    # small window first page
    ttk.Label(small_win, text="Enter Time : ").pack()
    time_entry = ttk.Entry(small_win)
    time_entry.pack(pady=5)

    ttk.Label(small_win, text="Enter Date [yyyy-mm-dd] : ").pack()
    date_entry = ttk.Entry(small_win)
    date_entry.pack(pady=5)

    ttk.Button(small_win, text='Submit', command=lambda: abset(2, f"{date_entry.get()} [{time_entry.get()}]")).pack(pady=10)
    ttk.Button(small_win, text='Add Week', command=show_second_frame).pack(pady=10)

    # small window second page
    ttk.Label(small2_win, text="Enter week period [start -  end ]: ").pack()
    week_entry = ttk.Entry(small2_win)
    week_entry.pack(pady=5)

    ttk.Button(small2_win, text='Back', command=show_first_frame).pack(pady=10)
    ttk.Button(small2_win, text='Mark', command=lambda: abset(3, week=week_entry.get())).pack(pady=10)

    # Initially show the first frame
    show_first_frame()

    main_win.mainloop()