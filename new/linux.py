import os, datetime, getpass, tools
from client import Client
class Linux():
    def __init__(self):
        os.system("clear")
        print("ｌｉｎｕｘ : 為サス")
        self.programs = {
        "login":"login to a user's workspace",
        "register":"register a new user"
        }
        self.tools = {
        "smtpCrack":"use extensive password dictionaries to brute force into an email account\nSyntax: smtpCrack <email address> <smtp server name>",
        "ftpCrack":"use extensive password dictionaries to brute force into an ftp server\nSyntax: ftpCrack <username> <host>",
        "hashCrack":"use extensive password dictionaries to crack a SHA256 hash\nSyntax: hashCrack <SHA256 hash>\n--lookup: searches for plaintext in dictionaries. Ex: hashCrack plaintext --lookup",
        "manage":"manage user account",
        "logout":"leave the workspace"
        }
        self.client = Client()
        self.location = "login_page"
        self.start()
    def start(self):
        while True:
            self.cmd()
    def login(self, fast, usr, pwd):
        username, password = "", ""
        if fast == False:
            username, password = input("Username: "), getpass.getpass("Password: ")
        else:
            username, password = usr, pwd
        if self.client.login(username, password) == True:
            os.system("clear")
            now = datetime.datetime.now()
            dt = str(now.month) + "/" + str(now.day) + "/" + str(now.year) + " " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
            print(username + " logged in on " + dt)
            self.location = "workspace"
        else:
            print("Unknown login.")
    def register(self):
        pass
    def help(self, mod, arr):
        if mod == "":
            print("Syntax: 'help <command>' for more information")
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
            print("Invalid syntax.")
        else:
            if self.location == "workspace":
                self.help(lookup, self.tools)
            elif self.location == "login_page":
                self.help(lookup, self.programs)
    def cmd(self):
        x = input("/ ")
        x = x.lower()
        commands = x.split(" ")
        if commands[0] == "clear":
            os.system("clear")
        if commands[0] == "help":
            if x == "help":
                if self.location == "login_page":
                    self.help("", self.programs)
                elif self.location == "workspace":
                    self.help("", self.tools)
            else:
                if self.location == "login_page":
                    self.lookup(self.programs, commands)
                elif self.location == "workspace":
                    self.lookup(self.tools, commands)
        if self.location == "workspace":
            if commands[0] == "smtpcrack":
                if len(commands) == 3:
                    smtpCrack = tools.SMTPCrack(commands[1], commands[2])
                else:
                    print("Invalid syntax.")
            elif commands[0] == "hashcrack":
                if len(commands) == 2:
                    hashCrack = tools.HashCrack(commands[1], False)
                elif len(commands) == 3 and commands[2] == "--lookup":
                    hashCrack = tools.HashCrack(commands[1], True)
                else:
                    print("Invalid syntax.")
            elif commands[0] == "logout":
                if len(commands) == 1:
                    self.__init__()
                else:
                    print("Invalid syntax.")
            elif commands[0] == "help":
                pass
            else:
                print("Unknown command.")
        elif self.location == "manage":
            pass
        elif self.location  == "login_page":
            if commands[0] == "login":
                if len(commands) == 3:
                    self.login(True, commands[1], commands[2])
                elif len(commands) == 1:
                    self.login(False, "", "")
                else:
                    print("Invalid syntax.")
            elif commands[0] == "register":
                self.register()
            elif commands[0] == "help":
                pass
            else:
                print("Unknown command.")
