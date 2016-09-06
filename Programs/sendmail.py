import smtplib, os
mail = smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()
mail.starttls()
emailsss = input("Enter your email: ")
mail.login(emailsss, input("Enter password: "))
subject = input("Enter email subject: ")
content = input("Enter email content: ")
stuff = "Subject: "+subject+"\n"+content
mail.sendmail(emailsss,input("Enter recipient's email: "),stuff)
mail.close()
print("Message Sent!")