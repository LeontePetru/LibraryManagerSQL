class User:
    pass

class LoggedUser(User):

    def __init__(self,username,password,role):
        self.__username=username
        self.__password=password
        self.__role=role


    @property
    def username(self):
        return self.__username

    @username.setter
    def title(self, username):
        self.__username = username

    @property
    def password(self):
        return self.__password

    @password.setter
    def title(self, password):
        self.__password = password

    @property
    def role(self):
        return self.__role

    @role.setter
    def title(self, role):
        self.__role = role