from tkinter import  ttk
from UI.student import open_new_student_window,abset,custom_absent
from UI.displayData import listBar
from UI.studentInfo import *


def student_window(win):
    open_new_student_window(win)
        
def remove_all_widgets(root):
    for widget in root.winfo_children():
        widget.destroy()

def mainPage(root):
    remove_all_widgets(root)
    root.geometry("1200x600")

    listBar(root) 
    # Create a frame
    frame = ttk.Frame(root)
    frame.place(x=10,y=10)

    # Add buttons
    new_student_button = ttk.Button(frame, text="New Student", command=lambda:student_window(root))
    new_student_button.pack(padx=5, pady=5)

    absence_attendance_button = ttk.Button(frame, text="Absence Attendance", command=abset)
    absence_attendance_button.pack(padx=5, pady=5)

    absence_attendance_custom_button = ttk.Button(frame, text="Custom Attendance", command=lambda:custom_absent(root))
    absence_attendance_custom_button.pack(padx=5, pady=5)

    detail_button = ttk.Button(frame, text="Detail", command=lambda:disp_box(root))
    detail_button.pack(padx=5, pady=5)
    
    root.mainloop()
