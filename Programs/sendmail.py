import smtplib, os
mail = smtplib.SMTP("smtp.live.com",587)
mail.ehlo()
mail.starttls()

sender = input("Enter your email: ")
password = input("Enter your password: ")
mail.login(sender, password)

subject = input("Enter email subject: ")
body = input("Enter email body: ")

content = "Subject: " + subject + "\n" + body

recipient = input("Enter recipient's email: ")

mail.sendmail(sender, recipient, content)
mail.close()

print("Message Sent!")
