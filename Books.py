

class Book:

    def __init__(self, title, author, isbn, genre, publisher,inventoryNumber,state):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publisher = publisher
        self.__inventoryNumber = inventoryNumber
        self.__state = state

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def author(self):
        return self.__author

    @author.setter
    def author(self, author):
        self.__author = author

    @property
    def isbn(self):
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn):
        self.__isbn = isbn

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre):
        self.__genre = genre

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher):
        self.__publisher = publisher

    @property
    def inventoryNumber(self):
        return self.__inventoryNumber

    @inventoryNumber.setter
    def inventoryNumber(self, inventoryNumber):
        self.__inventoryNumber = inventoryNumber

    @property
    def state(self):
        return self.__state

    @state.setter
    def state(self, state):
        self.__state = state




