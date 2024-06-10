import ttkbootstrap as ttk
from tkinter import *
from UI.mainPage import mainPage
from connect.fetch import check_credentials


# Create the main window
root = Tk()
root.title("Create by OneKnown")

user=StringVar()    
pass1=StringVar()
# Set the theme
style = ttk.Style("darkly")
root.geometry("400x300")

def print():
    #userInfo("demo")
    if(check_credentials(user.get(),pass1.get())):
        mainPage(root)
    
    
        
        
# Create the login form elements
username_label = ttk.Label(root,text="Username")
username_entry = ttk.Entry(root,textvariable=user)
password_label = ttk.Label(root,text="Password")
password_entry = ttk.Entry(root,show="*",textvariable=pass1)
login_button = ttk.Button(root,text="Login",bootstyle=ttk.SUCCESS,command=print)

# Place the elements in the window
username_label.pack(pady=10)
username_entry.pack(pady=5)
password_label.pack(pady=10)
password_entry.pack(pady=5)
login_button.pack(pady=10)


#mainPage(root)
# Run the application
root.mainloop()