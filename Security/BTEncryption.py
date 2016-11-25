from binaryTree import BinaryTree
class Decrypt():
	def __init__(self):
		self.decryptedTree = BinaryTree()
		self.decrypted = ""
	def decrypt(self):
		self.decrypted = input("Enter a string: ")
		for x in self.decrypted:
			self.decryptedTree.add(x)
		self.printer()
	def printer(self):
		print(self.decrypted + " to " + self.decryptedTree.get() + ".")

class Encrypt():
	def __init__(self):
		self.encryptedTree = BinaryTree()
		self.encrypted = ""
	def encrypt(self):
		self.encrypted = input("Enter a string: ")
			for x in self.encrypted:
				self.encryptedTree.add(x)
		self.printer()
	def printer(self):
		print(self.encrypted + " to " + self.encryptedTree.get() + ".")
while True:
	what = input("[E]ncrypt or [D]ecrypt? ")
	if what == "E" or what == "e":
		decrypter = Decrypt()
		decrypter.decrypt()
	elif what == "D" or what == "d":
		encrypter = Encrypt()
		encrypter.encrypt()