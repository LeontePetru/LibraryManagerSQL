from SQLPersistance import BookSQLPersist

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
                self.__genres.append(self.)
            # if bookData[i][6] not in states:
            #   states.append(bookData[i][6])
            if self.__bookList[i].publisher not in self.__publishers:
                self.__publishers.append(self.__bookList.publishers)
            if self.__bookList[i].author not in self.__authors:
                self.__authors.append(self.__bookList.author)

        @property
        def bookList(self):
            return self.__bookList

        @bookList.setter
        def bookData(self, bookList):
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

