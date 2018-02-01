import hashlib, os
class HashCrack():
	def __init__(self, h):
		self.hash = h
		self.brute_force()
	def sha256(self, raw):
		encoded = raw.encode("utf-8")
		hashed = hashlib.sha256(encoded).hexdigest()
		return hashed
	def scan(self, f):
		passwfile = open(f, "r").readlines()
		for password in passwfile:
			password = password.strip()
			sha256value = self.sha256(password)
			if self.hash == sha256value:
				print("[+]Hash Found: " + password)
				return True
			else:
				print(sha256value)
	def brute_force(self):
		files = os.listdir("passwords/")
		for f in files:
			print("\nDICTIONARY: " + f + "\n")
			if self.scan("passwords/" + f) == True:
				break
def sha256(raw):
	encoded = raw.encode("utf-8")
	hashed = hashlib.sha256(encoded).hexdigest()
	return hashed

h = HashCrack(sha256("qwerty123"))
