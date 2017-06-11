import smtplib
import sys
from email.mime.text import MIMEText

def sendemail(email, argmsg): 
    msg = "From: Support <support@threeIceHoles.com>\nTo:<"+email+">\nSubject: Your notification is ready\n\n"+argmsg

    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.login('uprm.notification@gmail.com','<INSERT_PASSWORD>')#INSERT PASSWORD HERE

    server.sendmail('support@threeIceHoles.com',email, msg)
    return
