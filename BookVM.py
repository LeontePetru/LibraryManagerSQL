from SQLPersistance import BookSQLPersist
from Books import Book

class BookViewModel:
    def __init__(self):
        self.__bookPersist=BookSQLPersist()
        self.__bookList=self.__bookPersist.read()
        self.__n=self.__bookList.__len__()

        self.__genres = []
        self.__genres.append("genre")
        self.__states = []
        self.__states.append("status")
        self.__states.append("available")
        self.__states.append("borrowed")
        self.__publishers = []
        self.__publishers.append("publisher")
        self.__authors = []
        self.__authors.append("author")

        for i in range(self.__n):
            if self.__bookList[i].genre not in self.__genres:
                self.__genres.append(self.__bookList[i].genre)
            # if books[i][6] not in states:
            #   states.append(books[i][6])
            if self.__bookList[i].publisher not in self.__publishers:
                self.__publishers.append(self.__bookList[i].publisher)
            if self.__bookList[i].author not in self.__authors:
                self.__authors.append(self.__bookList[i].author)

    @property
    def bookList(self):
        return self.__bookList

    @bookList.setter
    def books(self, bookList):
        self.__bookList = bookList

    @property
    def genres(self):
        return self.__genres

    @genres.setter
    def genres(self, genres):
        self.__genres = genres

    @property
    def states(self):
        return self.__states

    @states.setter
    def states(self, states):
        self.__states = states

    @property
    def authors(self):
        return self.__authors

    @authors.setter
    def authors(self, authors):
        self.__authors = authors

    @property
    def publishers(self):
        return self.__publishers

    @publishers.setter
    def publishers(self, publishers):
        self.__publishers = publishers

    def stringOfBooks(self):
        listOfString = []
        books = self.__bookList
        n = books.__len__()

        for i in range(n):
            stringGen = []
            stringGen.append(books[i].title)
            stringGen.append(books[i].author)
            stringGen.append(books[i].isbn)
            stringGen.append(books[i].genre)
            stringGen.append(books[i].publisher)
            # print(books[i].publisher)
            stringGen.append(books[i].inventoryNumber)
            stringGen.append(books[i].state)
            listOfString.append(stringGen)

        return listOfString
    
    def sortedListOfStrings(self,sortStates):
        listOfString = []
        sortedbooks=[]
        books = self.__bookList
        for i in range (self.__n):
            if ((books[i].genre == sortStates[0] or sortStates[0] == 'genre') and
                    (books[i].state == sortStates[1] or sortStates[1] == 'status') and
                    (books[i].publisher == sortStates[2] or sortStates[2] == 'publisher') and
                    (books[i].author == sortStates[3] or sortStates[3] == 'author')):
                sortedbooks.append(books[i])

        for i in sortedbooks:
            stringGen = []
            stringGen.append(i.title)
            stringGen.append(i.author)
            stringGen.append(i.isbn)
            stringGen.append(i.genre)
            stringGen.append(i.publisher)
            # print(books[i].publisher)
            stringGen.append(i.inventoryNumber)
            stringGen.append(i.state)
            listOfString.append(stringGen)

        return listOfString

    def nameSortedListOfStrings(self,name):
        sortedBookData1=[]
        books = self.__bookList
        listOfString = []

        for i in books:
            if i.title.lower() == name.lower() or name=="":
                sortedBookData1.append(i)

        for i in sortedBookData1:
            stringGen = []
            stringGen.append(i.title)
            stringGen.append(i.author)
            stringGen.append(i.isbn)
            stringGen.append(i.genre)
            stringGen.append(i.publisher)
            # print(books[i].publisher)
            stringGen.append(i.inventoryNumber)
            stringGen.append(i.state)
            listOfString.append(stringGen)

        return listOfString

    def searchByNumber(self,invNumber):
        books = self.__bookList
        for i in books:
            if i.inventoryNumber==invNumber:
                return i;
        return False

    def borrow(self,invNumber):
        book=self.searchByNumber(invNumber)
        book.state="borrowed"
        self.__bookPersist.update(book)

    def returnBook(self,invNumber):
        book = self.searchByNumber(invNumber)
        book.state = "available"
        self.__bookPersist.update(book)

    def insertUpdate(self,title,author,isbn,genre,publisher,invNumber,status):
        book1=Book(title,author,isbn,genre,publisher,invNumber,status)
        self.__bookPersist.delete(invNumber);
        self.__bookPersist.saveBook(book1)

    def deleteBook(self,invNumber):
        self.__bookPersist.delete(invNumber);
        #self.__bookInventory.bookPersistence.saveBook(book1)

    def bookNumbers(self):
        books = self.__bookList

        borrowed=0
        available=0
        for b in books:
            if b.state=="borrowed":
                borrowed=borrowed+1
            else:
                available=available+1

        return [available,borrowed]


#bookVM= BookViewModel()
#list=bookVM.stringOfBooks()

#for l in list:
#    print(l)