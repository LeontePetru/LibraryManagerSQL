import mysql.connector
from Books import Book
from Users import LoggedUser

#Singleton class
class SQLPersist:
  __instance = None
  __mydb= None

  def __init__(self):
    if SQLPersist.__instance != None:
      print("This class is a singleton!")
    else:
      self.__mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root"
      )
      SQLPersist.__instance=self

  @staticmethod
  def getInstance():
    """ Static access method. """
    if SQLPersist.__instance == None:
      SQLPersist()
    return SQLPersist.__instance

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
    mycursor = self.getInstance().mydb.cursor()
    #print("INSERT INTO `bookstoreschema`.`booktable` (`title`, `author`, `isbn`, `genre`, `publisher`, `inventoryNumber`, `state`) "
     #                "VALUES ('"+book.title+"', '"+book.author+"', '"+book.isbn+"', '"+book.genre+"', '"+book.publisher+"', '"+book.inventoryNumber+"', '"+book.state+"')")
    mycursor.execute("INSERT INTO `bookstoreschema`.`booktable` (`title`, `author`, `isbn`, `genre`, `publisher`, `inventoryNumber`, `state`) "
                     "VALUES ('"+book.title+"', '"+book.author+"', '"+book.isbn+"', '"+book.genre+"', '"+book.publisher+"', '"+book.inventoryNumber+"', '"+book.state+"')")
    self.getInstance().mydb.commit()

  def read(self):

    bookList = []
    mycursor = self.getInstance().mydb.cursor()
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

  def update(self,book):
    mycursor = self.getInstance().mydb.cursor()
    updateCommand="UPDATE `bookstoreschema`.`booktable` SET `title` = '"+book.title+"', `author` = '"+book.author+"', " \
                  "`isbn` = '"+book.isbn+"', `genre` = '"+book.genre+"', `publisher` = '"+book.publisher+"', " \
                  "`state` = '"+book.state+"' WHERE (`inventoryNumber` = '"+book.inventoryNumber+"');"
    mycursor.execute(updateCommand);
    self.getInstance().mydb.commit()

  def delete(self,invNumber):
    mycursor = self.getInstance().mydb.cursor()
    updateCommand="DELETE FROM `bookstoreschema`.`booktable` WHERE (`inventoryNumber` = '"+invNumber+"');"
    mycursor.execute(updateCommand)
    self.getInstance().mydb.commit()



class UserSQLPersist(SQLPersist):

  def __init__(self):
    super().__init__()

  def read(self):

    userList = []
    mycursor = self.getInstance().mydb.cursor()
    sql_select_Query = "SELECT * FROM bookstoreschema.usertable;"
    mycursor.execute(sql_select_Query)
    records = mycursor.fetchall()
    #n=mycursor.rowcount
    for row in records:
      username=row[0]
      password=row[1]
      role=row[2]
      book=LoggedUser(username,password,role)
      userList.append(book)

    return userList

  def saveUser(self, user):
    mycursor = self.getInstance().mydb.cursor()
    mycursor.execute("INSERT INTO `bookstoreschema`.`usertable` (`username`, `password`, `role`)"
                     " VALUES ('"+user.username+"', '"+user.password+"', '"+user.role+"');")
    self.getInstance().mydb.commit()

  def delete(self, username):
    mycursor = self.getInstance().mydb.cursor()
    updateCommand = "DELETE FROM `bookstoreschema`.`usertable` WHERE (`username` = '" + username + "');"
    mycursor.execute(updateCommand)
    self.getInstance().mydb.commit()

