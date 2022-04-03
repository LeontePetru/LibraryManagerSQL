import mysql.connector
from Books import Book

class SQLPersist:

  def __init__(self):
    self.__mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root"
    )

  @property
  def mydb(self):
    return self.__mydb

  @mydb.setter
  def mydb(self, mydb):
    self.__mydb = mydb

class BookSQLPersist(SQLPersist):

  def __init__(self):
    super().__init__()


  def saveBook(self,book):
    mycursor = self.mydb.cursor()
    print("INSERT INTO `bookstoreschema`.`booktable` (`title`, `author`, `isbn`, `genre`, `publisher`, `inventoryNumber`, `state`) "
                     "VALUES ('"+book.title+"', '"+book.author+"', '"+book.isbn+"', '"+book.genre+"', '"+book.publisher+"', '"+book.inventoryNumber+"', '"+book.state+"')")
    mycursor.execute("INSERT INTO `bookstoreschema`.`booktable` (`title`, `author`, `isbn`, `genre`, `publisher`, `inventoryNumber`, `state`) "
                     "VALUES ('"+book.title+"', '"+book.author+"', '"+book.isbn+"', '"+book.genre+"', '"+book.publisher+"', '"+book.inventoryNumber+"', '"+book.state+"')")
    self.mydb.commit()

  def read(self):

    bookList = []
    mycursor = self.mydb.cursor()
    sql_select_Query = "SELECT * FROM bookstoreschema.booktable;"
    mycursor.execute(sql_select_Query)
    records = mycursor.fetchall()
    #n=mycursor.rowcount
    for row in records:
      title=row[0]
      author=row[1]
      isbn=row[2]
      genre=row[3]
      publisher=row[4]
      inventoryNumber=row[5]
      status=row[6]
      book=Book(title,author,isbn,genre,publisher,inventoryNumber,status)
      bookList.append(book)

    return bookList

#bsql=BookSQLPersist()
#book=Book("Padurea","Rebreanu","445-234","Drama","P45","25","borrowed")
#list=bsql.read()
#for l in list:
 # print(l.__dict__)

#print(mydb)


