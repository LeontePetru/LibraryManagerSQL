import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
from UserVM import UserViewModel
import os
from tkinter import messagebox as mb


root = tk.Tk()
root.geometry('1280x720')

background_image = tk.PhotoImage(file='.\Images\LogIn.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

font = tkFont.Font(family="Times New Roman",size=16,weight="bold")

userEntry=tk.Entry(bg="#cccccc",font=font)
userEntry.place(relx=0.65,rely=0.525,relheight=0.06,relwidth=0.23)

passwordEntry=tk.Entry(bg="#cccccc",font=font,show='*')
passwordEntry.place(relx=0.65,rely=0.68,relheight=0.06,relwidth=0.23)

def buttonLogInFunc():
    #print(userEntry.get())
    #print(passwordEntry.get())
    #userPers=LoggedUserPersistance("users.json")
    #result=userPers.searchByUsername(userEntry.get())
    userVM=UserViewModel()
    result=userVM.searchByUsername(userEntry.get())
    if (result==False or result.password != passwordEntry.get()):
        mb.showerror("LogIn","Wrong username password combination")
    elif (result.role=="keeper"):
        root.quit()
        os.system('LoggedUserGUI.py -k')
    elif (result.role=="admin"):
        root.quit()
        os.system('LoggedUserGUI.py -a')
    elif (result.role=="user"):
        root.quit()
        os.system('UserGUI.py')



def Guest():
    root.quit()
    os.system('UserGUI.py')
    #root.destroy()


logInButton=tk.Button(bg="#cccccc",font=font,text="Log In",command=buttonLogInFunc,foreground="#ff6366")
logInButton.place(relx=0.675,rely=0.77,relheight=0.06,relwidth=0.18)

guestButton=tk.Button(bg="#cccccc",font=font,text="Continue as Guest",command=Guest,foreground="#ff6366")
guestButton.place(relx=0.675,rely=0.86,relheight=0.06,relwidth=0.18)


root.mainloop()