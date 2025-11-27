#This program will help you to send email using pyhton to the reciever

import smtplib
import ssl
from email.message import EmailMessage
EMAIL = "namankraj@gmail.com"
APP_PASSWORD = "Your app password here"
RECIEVER = "namankraj2@gmail.com"
msg = EmailMessage()
msg["from"] = "namankraj@gmail.com"
msg["To"] = "namankraj2@gmail.com"
msg["subject"] = "Pyhton msg send trial"
msg.set_content("This email is shared by yourself")
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    
    server.login("namankraj@gmail.com", "lueg lwwz ojil dopq")
    server.send_message(msg)
