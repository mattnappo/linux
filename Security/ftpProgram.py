import urllib, ftplib, sys, datetime
def upload():
    try:
        name = input("Enter filename: ")
        file = open(name,'rb')
        ftp.storbinary("STOR "+name, open(name, "rb"))
        file.close()
        ftp.quit()
        input("Complete; "+name+" uploaded. Press enter to continue.")
    except:
        print("File not found.")
def grab(username, password):
    try:
        name = input("Enter filename: ")
        file = open(name,'wb')
        ftp.retrbinary("RETR "+ name, file.write)
        file.close()
        ftp.quit()
        input("Complete; "+name+" uploaded. Press enter to continue.")
    except:
        print("File not found.")
while True:
    user = input("Enter username (EXIT to quit): ")
    password = input("Enter password: ")
    try:
        ftp = ftplib.FTP('ftp.mattnappo.com',user,password)
        if user == "EXIT":
            sys.exit()
        else:
            while True:
                where = input("[G]rab file, [U]plaod file, or [E]xit? ")
                if where == "G" or where == "g":
                    grab(user, password)
                elif where == "U" or where == "u":
                    upload()
                elif where == "E" or where == "e":
                    sys.exit()
    except ftplib.error_perm:
        print("Unknown account.")