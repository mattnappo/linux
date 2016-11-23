import hashlib
import time
def hash(password):
    passwor = password.encode("utf-8")
    save = hashlib.sha512(passwor).hexdigest()
    return save
hackingMode = input("Enable Hacking Mode (y/n/d)? ")
if hackingMode == "y":
    while True:
        passwfile = open("main.txt", "r")
        for password in passwfile:
            print(hash(password))
            time.sleep(.03)
elif hackingMode == "n":
    passwfile = open("main.txt", "r")
    current = input("Enter hashed password: ")
    for password in passwfile:
            if hash(password) == current:
                print("[+]Found: " + password)
                break
            else:
                print(hash(password))
    input("End of dictionary")
elif hackingMode == "d":
    passwfile = open("fake.txt", "r")
    current = input("Enter hashed password: ")
    for password in passwfile:
            if hash(password) == current:
                input("[+]Found: " + password)
                break
            else:
                print(hash(password))
    input("End of dictionary")