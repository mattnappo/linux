import hashlib, uuid, os, sys
from win32cred import UsernameTargetCredential
def hash(password):
    return hashlib.sha256(password.encode()).hexdigest()
def checkHash(hashed_password, user_password):
    return hashlib.sha256(user_password.encode()).hexdigest()
while True:
    username = input("Enter username: ")
    userin = input("Enter password: ")
    htg = username+".txt"
    if os.path.isfile(htg) == True:
        correct = open(htg, "r")
        if correct.read() == hash(userin):
            while True:
                choice = input("[V]iew Files (2), [C]hange password, [R]ed button, or [E]xit? ")
                if choice == "V" or choice == "v":
                    os.system("notepad "+username+".dll:file1.txt")
                    os.system("notepad "+username+".dll:file2.txt")
                    input("Press enter to hide")
                elif choice == "C" or choice == "c":
                    new = input("Enter new password: ")
                    with open("admin.txt", "w") as writer:
                        writer.write(hash(new))
                        print("Complete!")
                elif choice == "R" or choice == "r":
                    while True:
                        print("The red button will hide and then close this python file. It will still be available to see for users that have 'show hidden files' enabled in windows explorer.")
                        comfirmredbttn = input("Would you like to red button now(y/n)? ")
                        if comfirmredbttn == "y":
                            os.system("attrib +h hider.py")
                            print("Complete!")
                            sys.exit()
                        elif comfirmredbttn == "n":
                            break
                elif choice == "E" or choice == "e":
                    break
        else:
            print("Incorrect Password")
    else:
        while True:
            register = input("This account does not exist. Do you want to create this account now (y/n)? ")
            if register == "y":
                with open(htg, "w") as registernewacc:
                    registernewacc.write(hash(userin))
                    htgyzt = username+".dll"
                    with open(htgyzt, "w") as dll:
                        os.system("attrib +h "+username+".dll")
                        print("Complete!")
                        break
            elif register == "n":
                break