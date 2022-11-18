import requests
from email.message import EmailMessage
import ssl
import smtplib
import json
from account import *


email_sender = emailsender
email_password = emailpassword

with open('ss.json', 'r') as file:
    data = json.load(file)
    for key, value in data.items():
        recipient = value
        #print(recipient)

        email_reciever = recipient
        print(email_reciever)

payload = {'username': 'sikiru', 'password': 'honest'}
response = requests.post('https://httpbin.org/post', data=payload)
# with open('mytext.txt', 'a') as file:
#     file.write(response.text)
# dicts = response.json()
# print(dicts['form'])

subject = 'request'
body = 'successfully posted'
em = EmailMessage()
em['from'] = email_sender
em['to'] = ', '.join(email_reciever)
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_reciever, em.as_string())