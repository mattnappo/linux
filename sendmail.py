import smtplib, os

mail = smtplib.SMTP("mail.themastersschool.com", 587)

mail.ehlo()
mail.starttls()

sender = input("Enter your email: ")
password = input("Enter password: ")
mail.login(sender, password)

recepient = input("Enter recipient's email: ")

subject = input("Enter email subject: ")
body = input("Enter email content: ")
content = "Subject: "+subject+"\n"+content

mail.sendmail(sender, recepient , content)
mail.close()

print("Message Sent!")
