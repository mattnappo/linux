from tkinter import *
from os.path import isfile
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("450x150")
        self.title("Login")
        
        menu = Menu(self)
        self.config(menu=menu)
        account = Menu(menu)
        account.add_command(label="Register", command=self.register)
        menu.add_cascade(label="Account", menu=account)
        
        self.title = Label(self, text="Login Form\n").pack()
        self.username = Entry(self, width=30)
        self.username.pack()
        self.password = Entry(self, width=30, show="*")
        self.password.pack()
        self.pin = Entry(self, width="10", show="*", text="pin")
        self.pin.pack()
        space = Label(self).pack()
        self.enter = Button(self, text="Login", command=self.login).pack()
    def login(self):
        credentials = []
        uName = self.username.get()
        pW = self.password.get()
        p = self.pin.get()
        credentials.append(uName)
        credentials.append(pW)
        credentials.append(p)
        htg = p+".txt"
        if isfile(htg) == True:  
            with open(htg, "r") as correctCreds:
                if correctCreds.read() == str(credentials):
                    self.popup("Correct Credentials!")
                    self.regi.destroy()
        else:
            self.popup2("Incorrect Credentials!")
    def register(self):
        self.regi = Tk()
        Tk.__repr__(self.regi)
        self.regi.geometry("450x150")
        self.regi.title("Register")
        
        menu = Menu(self.regi)
        self.regi.config(menu=menu)
        account = Menu(menu)
        account.add_command(label="Login", command=App())
        menu.add_cascade(label="Account", menu=account)
        
        self.regi.title = Label(self.regi, text="Register Form\n").pack()
        self.regi.username = Entry(self.regi, width=30)
        self.regi.username.pack()
        self.regi.password = Entry(self.regi, width=30, show="*")
        self.regi.password.pack()
        self.regi.pin = Entry(self.regi, width="10", show="*", text="pin")
        self.regi.pin.pack()
        space = Label(self.regi).pack()
        self.regi.enter = Button(self.regi, text="Register", command=self.write).pack()
    
        self.popup("Account Created!")
    def write(self):
        credentials = []
        uName = self.regi.username.get()
        pW = self.regi.password.get()
        p = self.regi.pin.get()
        credentials.append(uName)
        credentials.append(pW)
        credentials.append(p)
        htg = p+".txt"
        with open(htg, "w") as creds:
            creds.write(str(credentials))
        self.popup("Account Created!")
        self.regi.destroy()
    def popup(self, msg):
        def leave():
            popup.destroy()
        popup = Tk()
        popup.wm_title("!")
        label = Label(popup, text=msg).pack()
        exit = Button(popup, text="Ok", command=leave).pack()
    def popup2(self, msg):
        def leave():
            popup2.destroy()
        popup2 = Tk()
        popup2.wm_title("!")
        label = Label(popup2, text=msg).pack()
        exit = Button(popup2, text="Ok", command=leave).pack()
        register = Button(popup2, text="Register", command=self.register).pack()
root = App()
root.mainloop()