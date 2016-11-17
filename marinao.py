class Hold():
	def __init__(self):
		self.result = []
		self.string = []
	def where(self):
		while True:
			wherer = input("[E]ncrypt or [D]ecrpyt a Message? ")
			if wherer == "E" or wherer == "e":
				self.encrypt()
			else:
				self.decrypt()
	def setter(self):
		self.result = []
		self.string = []
	def encrypt(self):
		self.setter()
		x = input("Enter String: ")
		for i in x:
			self.result.append(chr(ord(i)-2))
		self.printer()
	def decrypt(self):
		self.setter()
		x = input("Enter Code: ")
		for i in x:
			self.result.append(chr(ord(i)+2))
		self.printer()
	def printer(self):
		for x in self.result:
			print(x, end="")
		print("")
obj = Hold()
obj.where()