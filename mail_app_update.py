#this is updated version of sendingMailApp

#sendingMailApp is an application that allows you to send emails 

import smtplib

#make an SMTP object to connect SMTP server for gmail domain
smtpObj = smtplib.SMTP('smtp.gmail.com', 587)

#say 'hello' to SMTP mail server
smtpObj.ehlo()

#turn on connection encryption
smtpObj.starttls()

#log in to server
#IMPORTANT! Probably, you will have to make an application password fot your gmail account:
#Log in to your google account --> Security --> Application passwords --> Enter your current password --> Choose the application --> Generete
mail = input("Enter your gmail login: ")
password = input("Enter your gmail password: ")

smtpObj.login(mail, password)
print("Successful connection!\nYou can now send an email.")

#send mail
while True:
    recipientsMail = input("Enter the recipient's email address: ")
    subject = input("Enter subject of message:")
    message = input("Enter message:")
    smtpObj.sendmail(mail, recipientsMail, 'Subject: ' + subject + '\n' + message)
    print("Your message has been sent successfully!\nDo you want to send another email? Choose yes or no.")
    answear = input()
    if answear == "yes" or answear == "Yes":
        continue
    else:
#exit application
        print("You will now be logged out.")
        smtpObj.quit()
        print("You have been logged out successfully")
        break
