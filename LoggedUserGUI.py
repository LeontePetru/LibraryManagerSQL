import sys
import tkinter as tk
from tkinter import ttk, CENTER
from tkinter.messagebox import showinfo
from BookVM import BookViewModel
from UserVM import UserViewModel
import tkinter.font as tkFont
from tkinter import messagebox as mb


root = tk.Tk()
root.geometry('1280x720')
background_image = tk.PhotoImage(file='.\Images\BookInventoryGUI.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)

role=sys.argv[1]
getRole="user"


bookVM= BookViewModel()
bookData=bookVM.stringOfBooks()
n=bookData.__len__()

userVM = UserViewModel()
userData=userVM.stringOfUsers()


genres = bookVM.genres
states = bookVM.states
publishers = bookVM.publishers
authors = bookVM.authors

font = tkFont.Font(family="Times New Roman",size=12,weight="bold")

selectGenres = ttk.Combobox(root,font=(12),foreground="#ff6366",background="#cccccc")
selectGenres['values'] = genres
selectGenres.current(0)
selectGenres.place(relx=0.025,rely=0.2,relheight=0.04,relwidth=0.125)

selectAuthors = ttk.Combobox(root,font=(12),foreground="#ff6366",background="#cccccc")
selectAuthors['values'] = authors
selectAuthors.current(0)
selectAuthors.place(relx=0.025,rely=0.26,relheight=0.04,relwidth=0.125)

selectPublishers = ttk.Combobox(root,font=(12),foreground="#ff6366",background="#cccccc")
selectPublishers['values'] = publishers
selectPublishers.current(0)
selectPublishers.place(relx=0.025,rely=0.32,relheight=0.04,relwidth=0.125)

selectStates = ttk.Combobox(root,font=(12),foreground="#ff6366",background="#cccccc")
selectStates['values'] = states
selectStates.current(0)
selectStates.place(relx=0.025,rely=0.38,relheight=0.04,relwidth=0.125)

titleEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
titleEntry.place(relx=0.835,rely=0.245,relheight=0.06,relwidth=0.155)

def sortButtonFunc():
    sortParameters =[]
    sortGenres=selectGenres.get()
    sortParameters.append(sortGenres)
    sortStates = selectStates.get()
    sortParameters.append(sortStates)
    sortPublishers = selectPublishers.get()
    sortParameters.append(sortPublishers)
    sortAuthors = selectAuthors.get()
    sortParameters.append(sortAuthors)
    createBookTable(bookVM.sortedListOfStrings(sortParameters))

def searchByTitle():
    createBookTable(bookVM.nameSortedListOfStrings(titleEntry.get()))

sortButton=tk.Button(font=(12),text="Sort by",command=sortButtonFunc,foreground="#ff6366",bg="#cccccc")
sortButton.place(relx=0.025,rely=0.44,relheight=0.04,relwidth=0.125)

sortButton=tk.Button(font=(12),text="Search title",command=searchByTitle,foreground="#ff6366",bg="#cccccc")
sortButton.place(relx=0.835,rely=0.32,relheight=0.06,relwidth=0.155)


canvasLabel1=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelBorrow=tk.Label(master=canvasLabel1,text=" Borrow: \n \n Return:",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelBorrow.pack()
canvasLabel1.place(relx=0.205, rely=0.5, relheight=0.09, relwidth=0.06)

canvasLabel2=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelBorrow=tk.Label(master=canvasLabel2,text=" Book No#: \n \n Book No#:",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelBorrow.pack()
canvasLabel2.place(relx=0.28, rely=0.5, relheight=0.09, relwidth=0.07)

borrowNumberEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
borrowNumberEntry.place(relx=0.365, rely=0.5, relheight=0.035, relwidth=0.11)

returnNumberEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
returnNumberEntry.place(relx=0.365, rely=0.55, relheight=0.035, relwidth=0.11)

canvasLabel3=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelBorrow=tk.Label(master=canvasLabel3,text=" Username: \n \n Username:",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelBorrow.pack()
canvasLabel3.place(relx=0.485, rely=0.5, relheight=0.09, relwidth=0.08)

borrowUserEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
borrowUserEntry.place(relx=0.58, rely=0.5, relheight=0.035, relwidth=0.1)

returnUserEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
returnUserEntry.place(relx=0.58, rely=0.55, relheight=0.035, relwidth=0.1)

def borrow():
    bookVM.borrow(borrowNumberEntry.get())
    bookVM.__init__()
    sortButtonFunc()

def returnBook():
    bookVM.returnBook(returnNumberEntry.get())
    bookVM.__init__()
    sortButtonFunc()

def deleteBook():
    bookVM.deleteBook(DeleteGetEntry.get())
    bookVM.__init__()
    sortButtonFunc()

def getBook():
    book=bookVM.searchByNumber(DeleteGetEntry.get())
    TitleEntry2.delete(0,"end")
    TitleEntry2.insert(0,book.title)
    AuthorEntry.delete(0, "end")
    AuthorEntry.insert(0, book.author)
    ISBNEntry.delete(0, "end")
    ISBNEntry.insert(0, book.isbn)
    GenreEntry.delete(0, "end")
    GenreEntry.insert(0, book.genre)
    PublisherEntry.delete(0, "end")
    PublisherEntry.insert(0, book.publisher)
    InvNoEntry.delete(0, "end")
    InvNoEntry.insert(0, book.inventoryNumber)
    StatusEntry.delete(0, "end")
    StatusEntry.insert(0, book.state)

def insertUpdate():
    bookVM.insertUpdate(TitleEntry2.get(),AuthorEntry.get(),ISBNEntry.get(),GenreEntry.get(),
                           PublisherEntry.get(),InvNoEntry.get(),StatusEntry.get())
    bookVM.__init__()
    sortButtonFunc()

def getUser():
    pass
    user1=userVM.searchByUsername(UsernameEntry.get())
    RoleEntry.delete(0,"end")
    RoleEntry.insert(0,user1.role)

def deleteUser():
    pass
    user1=userVM.searchByUsername(UsernameEntry.get())
    if  user1 != False:
        if (user1.role=="keeper" or user1.role=="admin") and role=="-k":
            mb.showerror("Error", "Can not change an admin or a bookeeper")
            return

    userVM.deleteByUsername(UsernameEntry.get())
    userVM.__init__()
    createUsersTable(userVM.stringOfUsers())

def insertUpdateUser():
    pass
    #userVM.insertUpdateUser(UsernameEntry.get(),PasswordEntry.get(),RoleEntry.get())
    #userVM.__init__()
    #createUsersTable(userVM.stringOfUsers())

#def bookReport():
 #   userVM.usersPers.file("")


borrowButton=tk.Button(font=(12),text="Borrow Book",command=borrow,foreground="#ff6366",bg="#cccccc")
borrowButton.place(relx=0.7,rely=0.49,relheight=0.035,relwidth=0.1)

returnButton=tk.Button(font=(12),text="Return Book",command=returnBook,foreground="#ff6366",bg="#cccccc")
returnButton.place(relx=0.7,rely=0.545,relheight=0.035,relwidth=0.1)

deleteBookButton=tk.Button(font=(12),text="Delete Book",command=deleteBook,foreground="#ff6366",bg="#cccccc")
deleteBookButton.place(relx=0.43,rely=0.615,relheight=0.035,relwidth=0.095)

canvasLabel3=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelDelete=tk.Label(master=canvasLabel3,text="No#:",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelDelete.pack()
canvasLabel3.place(relx=0.535, rely=0.617, relheight=0.03, relwidth=0.03)

DeleteGetEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
DeleteGetEntry.place(relx=0.58, rely=0.615, relheight=0.035, relwidth=0.1)

GetButton=tk.Button(font=(12),text="Get Book",command=getBook,foreground="#ff6366",bg="#cccccc")
GetButton.place(relx=0.7,rely=0.615,relheight=0.035,relwidth=0.1)

canvasLabel4=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelDelete=tk.Label(master=canvasLabel4,text="Title:                    Author:                 ISBN:",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelDelete.pack()
canvasLabel4.place(relx=0.46, rely=0.655, relheight=0.03, relwidth=0.32)

TitleEntry2=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
TitleEntry2.place(relx=0.43, rely=0.685, relheight=0.035, relwidth=0.13)

AuthorEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
AuthorEntry.place(relx=0.57, rely=0.685, relheight=0.035, relwidth=0.11)

ISBNEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
ISBNEntry.place(relx=0.69, rely=0.685, relheight=0.035, relwidth=0.11)

canvasLabel5=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelDelete=tk.Label(master=canvasLabel5,text="  Genre:         Publisher:        InvNo#         Status:",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelDelete.pack()
canvasLabel5.place(relx=0.44, rely=0.725, relheight=0.03, relwidth=0.34)

GenreEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
GenreEntry.place(relx=0.43, rely=0.76, relheight=0.035, relwidth=0.09)

PublisherEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
PublisherEntry.place(relx=0.53, rely=0.76, relheight=0.035, relwidth=0.09)

InvNoEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
InvNoEntry.place(relx=0.63, rely=0.76, relheight=0.035, relwidth=0.08)

StatusEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
StatusEntry.place(relx=0.72, rely=0.76, relheight=0.035, relwidth=0.08)

InsertUpdateButton=tk.Button(font=(12),text="Insert Book / Update Book",command=insertUpdate,foreground="#ff6366",bg="#cccccc")
InsertUpdateButton.place(relx=0.5,rely=0.81,relheight=0.035,relwidth=0.22)

canvasLabel6=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
canvasLabel6.place(relx=0.41, rely=0.6, relheight=0.25, relwidth=0.003)
canvasLabel7=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
canvasLabel7.place(relx=0.4097, rely=0.6, relheight=0.25, relwidth=0.003)

DeleteUserButton=tk.Button(font=(12),text="Delete User",command=deleteUser,foreground="#ff6366",bg="#cccccc")
DeleteUserButton.place(relx=0.18,rely=0.615,relheight=0.035,relwidth=0.1)

GetUserButton=tk.Button(font=(12),text="Get User",command=getUser,foreground="#ff6366",bg="#cccccc")
GetUserButton.place(relx=0.3,rely=0.615,relheight=0.035,relwidth=0.1)

canvasLabel8=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelDelete=tk.Label(master=canvasLabel8,text="   Username: ",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelDelete.pack()
canvasLabel8.place(relx=0.175, rely=0.68, relheight=0.03, relwidth=0.1)

UsernameEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
UsernameEntry.place(relx=0.3, rely=0.68, relheight=0.035, relwidth=0.1)

canvasLabel9=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelDelete=tk.Label(master=canvasLabel9,text="   Password: ",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelDelete.pack()
canvasLabel9.place(relx=0.175, rely=0.72, relheight=0.03, relwidth=0.1)

canvasLabel10=tk.Canvas(root,bg="#ffffff",borderwidth=0,selectborderwidth=0)
labelDelete=tk.Label(master=canvasLabel10,text="   Role: ",font=(12),fg="#ff6366",bg="#ffffff",borderwidth=0)
labelDelete.pack()
canvasLabel10.place(relx=0.175, rely=0.76, relheight=0.03, relwidth=0.1)

PasswordEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366",show="*")
PasswordEntry.place(relx=0.3, rely=0.72, relheight=0.035, relwidth=0.1)

RoleEntry=tk.Entry(bg="#cccccc",font=font,fg="#ff6366")
RoleEntry.place(relx=0.3, rely=0.76, relheight=0.035, relwidth=0.1)

InsertUpdateButton=tk.Button(font=(12),text="Insert User / Update User",command=insertUpdateUser,foreground="#ff6366",bg="#cccccc")
InsertUpdateButton.place(relx=0.2,rely=0.81,relheight=0.035,relwidth=0.18)


BookReport=tk.Button(font=(12),text="Book Report",command=insertUpdateUser,foreground="#ff6366",bg="#cccccc")
BookReport.place(relx=0.2,rely=0.86,relheight=0.035,relwidth=0.18)

def createBookTable(data):
    canvas = tk.Canvas(root)
    canvas.place(relx=0.175, rely=0.2, relheight=0.28, relwidth=0.65)

    tv = ttk.Treeview(canvas,selectmode='browse')
    vsb = ttk.Scrollbar(orient="vertical", command=tv.yview)
    tv.configure(yscrollcommand=vsb.set)

    tv['columns']=('number', 'title', 'author','isbn','genre','publisher','inventoryNumber','state')

    tv.column('#0',width=0)
    tv.column('number', anchor=CENTER,width=30)
    tv.column('title', anchor=CENTER,width=180)
    tv.column('author', anchor=CENTER,width=120)
    tv.column('isbn', anchor=CENTER,width=100)
    tv.column('genre', anchor=CENTER,width=100)
    tv.column('publisher', anchor=CENTER,width=130)
    tv.column('inventoryNumber', anchor=CENTER,width=70)
    tv.column('state', anchor=CENTER,width=100)

    tv.heading('number', text='No#', anchor=CENTER)
    tv.heading('title', text='Title', anchor=CENTER)
    tv.heading('author', text='Author', anchor=CENTER)
    tv.heading('isbn', text='ISBN', anchor=CENTER)
    tv.heading('genre', text='Genre', anchor=CENTER)
    tv.heading('publisher', text='Publisher', anchor=CENTER)
    tv.heading('inventoryNumber', text='InvNo#', anchor=CENTER)
    tv.heading('state', text='Status', anchor=CENTER)

    index=-1
    bookData=data
    n1=bookData.__len__()

    for i in range(n1):
        index = index + 1
        tv.insert(parent='',index=index,iid=index,values=(index,bookData[i][0],bookData[i][1],bookData[i][2],
                                                                    bookData[i][3],bookData[i][4],bookData[i][5],bookData[i][6]))

    tv.pack()

def createUsersTable(usersData):
    canvas1 = tk.Canvas(root)
    canvas1.place(relx=0.015, rely=0.615, relheight=0.23, relwidth=0.15)

    tv1 = ttk.Treeview(canvas1,selectmode='browse')
    vsb1 = ttk.Scrollbar(orient="vertical", command=tv1.yview)
    tv1.configure(yscrollcommand=vsb1.set)

    tv1['columns']=('number', 'username', 'role',)

    tv1.column('#0',width=0)
    tv1.column('number', anchor=CENTER, width=15)
    tv1.column('username', anchor=CENTER,width=100)
    tv1.column('role', anchor=CENTER,width=75)

    tv1.heading('number', text='N.', anchor=CENTER)
    tv1.heading('username', text='Username', anchor=CENTER)
    tv1.heading('role', text='Type', anchor=CENTER)

    index=-1
    userData=usersData
    n1=userData.__len__()

    for i in range(n1):
        index = index + 1
        tv1.insert(parent='',index=index,iid=index,values=(index,userData[i][0],userData[i][2]))
    tv1.pack()

createBookTable(bookVM.stringOfBooks())
createUsersTable(userVM.stringOfUsers())

root.mainloop()



