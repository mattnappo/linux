import os, datetime
from client import Client

class Linux():
    def __init__(self):
        self.programs = {
        "login":"login to an account",
        "register":"create a new account"
        }
        self.tools = {
        "crack":"a variety of password cracking tools\nSyntax: crack -<toolname>\nTools: \n-smtp\n-hash\n-zip",
        "hack":"hacking tools\nSyntax: hack -<toolname>\nTools: \n-firewall \n-something",
        "util":"other utilities"
        }
        self.client = Client()
        self.where = "login_page"
        self.start()
    def start(self):
        while True:
            self.cmd()
    def login(self):
        username = input("Username: ")
        password = input("Password: ")
        print(self.client.username)
        print(self.client.password)
        if self.client.login(username, password) == True:
            os.system("clear")
            now = datetime.datetime.now()
            dt = str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
            print(username + " logged in on " + dt)
            self.where = "workspace"
        else:
            print("Unknonwn Login")
    def register(self):
        pass
    def help(self, mod, arr):
        if mod == "":
            print("Syntax: 'help -<command>' for more information")
            for key, value in arr.items():
                print(key)
        else:
            print(arr[mod])
    def lookup(self, arr, commands):
        lookup = ""
        for program in arr:
            if commands[1] == program:
                lookup = program
                break
        if lookup == "":
            print("Incorrect Syntax")
        else:
            if self.where == "workspace":
                self.help(lookup, self.tools)
            elif self.where == "login_page":
                self.help(lookup, self.programs)
    def cmd(self):
        x = input("/ ")
        commands = x.split(" -")
        if commands[0] == "help":
            if x == "help":
                if self.where == "login_page":
                    self.help("", self.programs)
                elif self.where == "workspace":
                    self.help("", self.tools)
            else:
                if self.where == "login_page":
                    self.lookup(self.programs, commands)
                elif self.where == "workspace":
                    self.lookup(self.tools, commands)
        elif commands[0] == "login":
            self.login()
        elif commands[0] == "register":
            self.register()
        elif commands[0] == "clear":
            os.system("clear")
        elif commands[0] == "":
            pass
        else:
            print("Unknown Command")
