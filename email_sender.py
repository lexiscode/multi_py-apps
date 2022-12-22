# https://www.geeksforgeeks.org/send-mail-gmail-account-using-python/

import smtplib

to = input("Enter the Email of recipient: ")
message = input("Enter your message: ")

def sendEmail(to, message):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('your-email@gmail.com', 'your-password')
    server.sendmail('your-email@gmail.com', to, message)
    server.close()

sendEmail(to, message)
