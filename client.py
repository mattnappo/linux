import os, tools
class Client():
    def __init__(self):
        self.username = ""
        self.password = ""
    def login(self, username, password):
        if self.load(username) == True:
            if self.password == tools.sha256(password):
                return True
            else:
                return False
        else:
            return False
    def isInUse(self, username):
        usernames = os.listdir("users/")
        f = username
        for username in usernames:
            if f == username:
                return True
        return False
    def load(self, username):
        self.username = username
        if self.username != "":
            filename = "users/" + self.username
            if os.path.isfile(filename) == True:
                with open(filename, "r") as f:
                    self.password = f.read()
                    return True
            else:
                return False
        else:
            return False
        return False
    def register(self, username, password):
        self.username = username
        self.password = password
        if self.username != "" and self.password != "":
            filename = "users/" + self.username
            if os.path.isfile(filename) == False:
                with open(filename, "w") as f:
                    f.write(tools.sha256(self.password))
                    return True
            else:
                return False
        else:
            return False
    def remove(self):
        if self.username != "" and self.password != "":
            filename = "users/" + self.username
            if os.path.isfile(filename) == True:
                os.remove(filename)
                return True
            else:
                return False
        else:
            return False
    def change(self, modifier, new, password):
        if modifier == "username":
            self.remove()
            self.username = new
            self.register(self.username, password)
            return True
        elif modifier == "password":
            self.remove()
            self.password = new
            self.register(self.username, password)
            return True
        return False
