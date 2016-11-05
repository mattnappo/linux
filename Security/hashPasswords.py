import hashlib, uuid, os
def hash(password):
    salt = uuid.uuid4().hex
    return hashlib.sha256(salt.encode() + password.encode()).hexdigest() + ':' + salt
def checkHash(hashed_password, user_password):
    password, salt = hashed_password.split(':')
    return hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
username = input("Enter username: ")
passwords = input("Enter password: ")
if os.path.isfile(username+".txt") == True:
    hashed_password = hash(passwords)
    htg = username+".txt"
    with open(htg, "r") as file:
        old_pass = file.readlines()
else:
    hashed_password = hash(passwords)
    htg = username+".txt"
    with open(htg, "w") as file:
        file.write(hash(passwords))
        print("Account created!")
if checkHash(hashed_password, passwords):
    print("Welcome, "+username+"!")
else:
    print("Incorrect login.")