
import tkinter as tk
from tkinter import ttk, CENTER
from tkinter.messagebox import showinfo
from BookVM import BookViewModel
import tkinter.font as tkFont

#WIDTH = 1280
#HEIGHT = 720


root = tk.Tk()
root.geometry('1280x720')
background_image = tk.PhotoImage(file='.\Images\BookInventoryGUI.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)


bookVM= BookViewModel()
bookData=bookVM.stringOfBooks()
n=bookData.__len__()

genres = bookVM.genres
states = bookVM.states
publishers = bookVM.publishers
authors = bookVM.authors

        #for i in range(n):
         #   if bookData[i][3] not in genres:
          #      genres.append(bookData[i][3])
            #if bookData[i][6] not in states:
             #   states.append(bookData[i][6])
           # if bookData[i][4] not in publishers:
            #    publishers.append(bookData[i][4])
            #if bookData[i][2] not in authors:
             #   authors.append(bookData[i][1])

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

titleEntry=tk.Entry(bg="#cccccc",font=font)
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
    #print(sortParameters)
    createTable(bookVM.sortedListOfStrings(sortParameters))

def searchByTitle():
    createTable(bookVM.nameSortedListOfStrings(titleEntry.get()))
    #canvas.update_idletasks()

sortButton=tk.Button(font=(12),text="Sort by",command=sortButtonFunc,foreground="#ff6366",bg="#cccccc")
sortButton.place(relx=0.025,rely=0.44,relheight=0.04,relwidth=0.125)

sortButton=tk.Button(font=(12),text="Search title",command=searchByTitle,foreground="#ff6366",bg="#cccccc")
sortButton.place(relx=0.835,rely=0.32,relheight=0.06,relwidth=0.155)


        #for i in range(genres.__len__()):
         #   print(genres[i])

def createTable(data):
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
                #for j in range(7):

                #if ((bookData[i][3]==sortStates[0] or sortStates[0]=='genre') and
                 #   (bookData[i][6]==sortStates[1] or sortStates[1]=='status') and
                  #  (bookData[i][4]==sortStates[2] or sortStates[2]=='publisher') and
                   # (bookData[i][1]==sortStates[3] or sortStates[3]=='author')):
        index = index + 1
        tv.insert(parent='',index=index,iid=index,values=(index,bookData[i][0],bookData[i][1],bookData[i][2],
                                                                    bookData[i][3],bookData[i][4],bookData[i][5],bookData[i][6]))

    tv.pack()

#unsortedParameters = []
#unsortedParameters.append("genre")
#unsortedParameters.append("status")
#unsortedParameters.append("publisher")
#unsortedParameters.append("author")
createTable(bookVM.stringOfBooks())

root.mainloop()



