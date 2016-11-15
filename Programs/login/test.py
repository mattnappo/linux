from tkinter import *

class Class1():
	def __init__(self, var):
		self.username = var
	
	def usernameGet(self):
		print(self.username)
Class1(34).usernameGet()