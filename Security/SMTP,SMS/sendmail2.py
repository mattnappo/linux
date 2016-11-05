import smtplib, os
print("This program works best for gmail.")
def login(services,port):
    mail = smtplib.SMTP("smtp."+services+".com",port)
    mail.ehlo()
    mail.starttls()
    try:
        mail.login(emailsss, input("Enter password: "))
    except smtplib.SMTPAuthenticationError:
        print("Wrong Password")
    return mail
emailsss = input("Enter sender's email: ")
if "gmail" or "Gmail" in emailsss:
    mail = login("gmail",587)
    subject = input("Enter email subject: ")
    content = input("Enter email content: ")
    stuff = "Subject: "+subject+"\n"+content
    mail.sendmail(emailsss,input("Enter recipient's email: "),stuff)
    mail.close()
    print("Message Sent!")
elif "yahoo" or "Yahoo" in emailsss:
    mail = login("mail.yahoo",465)
    subject = input("Enter email subject: ")
    content = input("Enter email content: ")
    stuff = "Subject: "+subject+"\n"+content
    mail.sendmail(emailsss,input("Enter recipient's email: "),stuff)
    mail.close()
elif "hotmail" or "Hotmail" or "HotMail" in emailsss:
    mail = login("live",25)
    subject = input("Enter email subject: ")
    content = input("Enter email content: ")
    stuff = "Subject: "+subject+"\n"+content
    mail.sendmail(emailsss,input("Enter recipient's email: "),stuff)
    mail.close()
else:
    print("Message will not send.")
