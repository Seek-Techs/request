import requests
from email.message import EmailMessage
import ssl
import smtplib
import json
from account import *
import os

API_ENDPOINT = 'https://user-mangement-api.herokuapp.com/'
SMTP_HOST = 'smtp.gmail.com'
EMAIL_SENDER = emailsender
EMAIL_PASSWORD = emailpassword
email_receiver = []
print('running')

with open('ss.json', 'r') as file:
    data = json.load(file)
    for key, value in data.items():
        
        recipient = value

        email_receiver.append(recipient) 
        print(value)



# with open('mytext.txt', 'a') as file:
#     file.write(response.text)
# dicts = response.json()
# print(dicts['form'])

def send_update(msg_body, json):
    subject = 'post request'
    body = 'successfully posted'
    em = EmailMessage()
    em['from'] = EMAIL_SENDER
    em['to'] = ', '.join(email_receiver)
    em['subject'] = subject
    em.set_content(body)


    context = ssl.create_default_context()
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, email_receiver, em.as_string())
        # print(status_code)
payload = {
    "first name": "sikiru", 
    "last name": "yusuff",
    "email": "sikiru.yusuff@yahoo.com",
    "phone": "07065264103", 
    "sex": "male",
    "country": "nigeria",
    }
add_user_request = requests.post(f'{API_ENDPOINT}/post', data=payload)
if add_user_request.status_code == 200:
    send_update('successfully posted', add_user_request.json)

else:
    send_update('failed to post request', add_user_request.json)

req = requests.get(API_ENDPOINT)
print(req._content)
response = requests.post('https://httpbin.org/post', data=payload)
print(response._content)