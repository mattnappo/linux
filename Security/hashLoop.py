import hashlib, time, random
def hashPw(password):
	passwor = password.encode("utf-8")
	save = hashlib.sha256(passwor).hexdigest()
	return save
while True:
	num = random.random()
	num = str(num)
	num = num[1:]
	print(hashPw(num))