import hashlib
def hash(password):
    password = password.encode("utf-8")
    save = hashlib.sha512(password).hexdigest()
    return save
password = input("Enter password: ")
print(hash(password))