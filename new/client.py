import os
class Client():
    def __init__(self):
        self.username = ""
        self.password = ""
    def login(self, username, password):
        if self.load(username) == True:
            if self.password == password:
                return True
            else:
                return False
        else:
            return False
    def load(self, username):
        self.username = username
        if self.username != "":
            filename = "usr/" + self.username + ".usr"
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
            filename = "usr/" + self.username + ".usr"
            if os.path.isfile(filename) == False:
                with open(filename, "w") as f:
                    f.write(self.password)
                    return True
            else:
                return False
        else:
            return False
    def remove(self):
        if self.username != "" and self.password != "":
            filename = "usr/" + self.username + ".usr"
            if os.path.isfile(filename) == True:
                os.remove(filename)
                return True
            else:
                return False
        else:
            return False
    def change(self, modifier, new):
        if modifier == "username":
            self.username = new
            self.remove()
            self.register(self.password)
        elif modifier == "password":
            self.password = new
            self.remove()
            self.register(self.password)
