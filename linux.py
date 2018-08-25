# to do: better command handler (JSON thingy with exec?("python code in string"))
# cleanup my code (WHY IS THIS 200 lines???? WTF)
# make quick stop for cracking tools
# work on logging
import os, datetime, getpass, tools
from client import Client
class Linux():
    def __init__(self):
        os.system("clear")
        print("ｌｉｎｕｘ : 為サス")
        self.programs = {
        "login":"login to a user's workspace\nQuickLogin syntax (optional): login <username> <password>",
        "register":"register a new user"
        }
        self.tools = {
        "smtpcrack":"use extensive password dictionaries to brute force into an email account\nSyntax: smtpCrack <email address> <smtp server name>",
        "ftpcrack":"use extensive password dictionaries to brute force into an ftp server\nSyntax: ftpCrack <username> <host>",
        "hashcrack":"use extensive password dictionaries to crack a SHA256 hash\nSyntax: hashCrack <SHA256 hash>\n--lookup: searches for plaintext in dictionaries\n--add: adds a password to the dictionaries",
        "manage":"manage user account",
        "logout":"leave the workspace"
        }
        self.manages = {
        "change":"change username or password\nSyntax: change --username <username>\n            --password",
        "delete":"permanently delete account\nSyntax: delete <username>",
        "exit":"exit the account management panel"
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
            print("Invalid login.")
    def register(self):
        username = input("Username: ")
        if self.client.isInUse(username) == True:
            print("Username already in use.")
        else:

            password = getpass.getpass("Password: ")
            confirm = getpass.getpass("Password (again): ")
            if password == confirm:
                self.client.register(username, password, False)
                print("Account created.")
            else:
                print("Passwords do not match.")
    def help(self, mod, arr):
        if mod == "":
            print("Syntax: 'help <command>' for more information")
            for key, value in arr.items():
                print(key)
        else:
            print(arr[mod])
    def lookup(self, arr, commands):
        looker = ""
        for program in arr:
            if commands[1] == program:
                looker = program
                break
        if looker == "":
            print("Invalid syntax.")
        else:
            if self.location == "workspace":
                self.help(looker, self.tools)
            elif self.location == "login_page":
                self.help(looker, self.programs)
            elif self.location == "manage":
                self.help(looker, self.manages)
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
                elif self.location == "manage":
                    self.help("", self.manages)
            else:
                if self.location == "login_page":
                    self.lookup(self.programs, commands)
                elif self.location == "workspace":
                    self.lookup(self.tools, commands)
                elif self.location == "manage":
                    self.lookup(self.manages, commands)
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
                elif len(commands) == 3 and commands[2] == "--add":
                    with open("passwords/custom.txt", "a") as f:
                        f.write(commands[1] + "\n")
                    print("Added " + commands[1] + " to the dictionary.")
                else:
                    print("Invalid syntax.")
            elif commands[0] == "ftpcrack":
                if len(commands) == 3:
                    ftpCrack = tools.FTPCrack(commands[1], commands[2])
                else:
                    print("Invalid syntax.")
            elif commands[0] == "logout":
                if len(commands) == 1:
                    self.__init__()
                else:
                    print("Invalid syntax.")
            elif commands[0] == "manage":
                if len(commands) == 1:
                    self.location = "manage"
                    os.system("clear")
                    print("Account management")
                else:
                    print("Invalid syntax.")
            elif commands[0] == "help" or commands[0] == "clear":
                pass # because these commands are handled elsewhere
            else:
                print("Invalid command.")
        elif self.location == "manage":
            if commands[0] == "delete":
                if len(commands) == 2:
                    if commands[1] == self.client.username:
                        while True:
                            ays = input("Delete account '" + self.client.username + "' (YES/NO)? ")
                            if ays == "YES":
                                if getpass.getpass("Password: ") == self.client.password:
                                    if self.client.remove() == True:
                                        self.__init__()
                                    else:
                                        print("Remove failed unexpectedly.")
                                else:
                                    print("Incorrect password.")
                                break
                            elif ays == "NO":
                                print("Account not deleted.")
                                break
                    else:
                        print("Incorrect username.")
                else:
                    print("Invalid syntax.")
            elif commands[0] == "change":
                if len(commands) == 3 or len(commands) == 2:
                    if commands[1] == "--username":
                        if len(commands) == 3:
                            while True:
                                ays = input("Change username from '" + self.client.username + "' to '" + commands[2] + "' (YES/NO)? ")
                                if ays == "YES":
                                    pwd = getpass.getpass("Password: ")
                                    print("pwd: " + pwd + "\nself.client.password: " + self.client.password)
                                    if tools.sha256(pwd) == self.client.password:
                                        if self.client.change("username", commands[2]) == True:
                                            print("Username changed successfully.")
                                        else:
                                            print("Change failed unexpectedly.")
                                    else:
                                        print("Incorrect password.")
                                    break
                                elif ays == "NO":
                                    print("Username not changed")
                                    break
                        else:
                            print("Invalid syntax.")
                    elif commands[1] == "--password":
                        if len(commands) == 2:
                            pwd = getpass.getpass("Current password: ")
                            if tools.sha256(pwd) == self.client.password:
                                newpw = getpass.getpass("New password: ")
                                confirm_newpw = getpass.getpass("Confirm new password: ")
                                if newpw == confirm_newpw:
                                    if newpw == self.client.password:
                                        print("Your new password must be different than your old password.")
                                    else:
                                        if self.client.change("password", newpw) == True:
                                            print("Password successfully changed.")
                                        else:
                                            print("Change failed unexpectedly.")
                                else:
                                    print("Passwords do not match.")
                            else:
                                print("Incorrect password.")
                        else:
                            print("Invalid syntax.")
                    else:
                        print("Invalid syntax")
                else:
                    print("Invalid syntax")
            elif commands[0] == "exit":
                if len(commands) == 1:
                    self.location = "workspace"
                else:
                    print("Invalid syntax.")
            elif commands[0] == "help" or commands[0] == "clear":
                pass
            else:
                print("Invalid command.")
        elif self.location  == "login_page":
            if commands[0] == "login":
                if len(commands) == 3:
                    self.login(True, commands[1], commands[2])
                elif len(commands) == 1:
                    self.login(False, "", "")
                else:
                    print("Invalid syntax.")
            elif commands[0] == "register":
                if len(commands) == 1:
                    self.register()
                else:
                    print("Invalid syntax.")
            elif commands[0] == "help" or commands[0] == "clear":
                pass
            else:
                print("Invalid command.")
os.system("clear")
l = Linux()
