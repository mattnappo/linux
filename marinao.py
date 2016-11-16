class Hold():
	def __init__(self):
		self.result = []
		self.string = []
	def where(self):
		while True:
			wherer = input("[E]ncrypt or [D]ecrpyt a Message? ")
			if wherer == "E" or wherer == "e":
				self.encrypt()
	def encrypt(self):
		x = input("Enter String: ")
		for i in x:
			self.result.append(ord(y-2))
	def deocde(self):
		x = input("Enter Code: ")
		for y in x:
			self.result.append(ord(y+2))
	def printer(self):
		print(self.result)
Hold.where()