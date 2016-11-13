'''import sys
from tkinter import *
class Form():
def login():
    pass
GUI = Tk()
ent = StringVar()
GUI.geometry("450x450+500+300")
GUI.title("Login")
title = Label(GUI, text="Login Form").pack()
uName = Label(GUI, text="Username ").pack()
username = Entry().pack()
pW = Label(GUI, text="Password ").pack()
password = Entry().pack()
button = Button(GUI, text="Login", command=login).pack()
self.password.get()
GUI.mainloop()'''
from linkedlist import LinkedList
from tkinter import *
class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.geometry("450x450+500+300")
        self.title("Login")
        
        self.title = Label(self, text="Login Form\n").pack()
        self.username = Entry(self, width=30)
        self.username.pack()
        self.password = Entry(self, width=30)
        self.password.pack()
        self.enter = Button(self, text="Login", command=self.save).pack()
    def save(self):
        credentials = LinkedList()
        uName = self.username.get()
        pW = self.password.get()
        credentials.append(uName)
        credentials.append(pW)
        print(credentials.printer())
root = App()
root.mainloop()