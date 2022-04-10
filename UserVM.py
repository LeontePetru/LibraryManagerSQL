from SQLPersistance import  UserSQLPersist
from Users import LoggedUser

class UserViewModel:

    def __init__(self):
        self.__userPersistance=UserSQLPersist()
        self.__users=self.__userPersistance.read()

    @property
    def users(self):
        return self.__users

    @users.setter
    def states(self, users):
        self.__users = users

    @property
    def usersPers(self):
        return self.__userPersistance

    @usersPers.setter
    def states(self, userPersistance):
        self.__userPersistance = userPersistance

    def stringOfUsers(self):
        listOfString= []
        users=self.users
        n=users.__len__()

        for i in range(n):
            stringGen=[]
            stringGen.append(users[i].username)
            stringGen.append(users[i].password)
            stringGen.append(users[i].role)

            listOfString.append(stringGen)

        return listOfString

    def searchByUsername(self,username):
        users = self.users
        n = users.__len__()

        for i in range(n):
            if (users[i].username==username):
                return users[i]
        return False

    def deleteByUsername(self,username):
        self.__userPersistance.delete(username)

    #def insertUpdateUser(self,username,password,role):
     #   user1=LoggedUser(username,password,role)
      #  self.deleteByUsername(username)
       # pers=self.usersPers
        #pers.insertUser(user1)
    #


userVM=UserViewModel()
print(userVM.stringOfUsers());