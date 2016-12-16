import urllib, ftplib, sys, datetime, os
def printX():
    files = []
    #try:
    files = ftp.nlst()
    #except:
    print("Directory Empty!")
    for f in files:
        print(f)
def push():
    printX()
    name = input(": ")
    file = open(name,'rb')
    ftp.storbinary("STOR "+name, open(name, "rb"))
    file.close()
    ftp.quit()
    print("Success; "+name+" pushed at TIMESTAMP")

def edit():
    printX()
    try:
        name = input(": ")
        file = open(name,'wb')
        ftp.retrbinary("RETR "+ name, file.write)
        file.close()
        ftp.quit()
        print("Success")
    except:
        print("File not found.")


ftp = ftplib.FTP('ftp.mattnappo.com', "work@mattnappo.com", "root123")
print()
print("Status: Connected!")
where = input("[P]ush File, [E]dit File, or [Q]uit? ")
if where == "P" or where == "p":
    push()
elif where == "E" or where == "e":
    edit()
elif where == "E" or where == "e":
    sys.exit()