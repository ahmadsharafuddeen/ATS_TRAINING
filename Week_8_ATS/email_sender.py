import smtplib
from email.message import EmailMessage

email = EmailMessage()
email["from"] = "Ahmad Sharafudeen"
email["to"] = "ahmad.sharafudeen@gmail.com"
email["subject"] = "You won 1,000,000 dollars!"

email.set_content("I am a Python master!")

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("ahmad.sharafudeen@gmail.com", "Ahmad1999")
    smtp.send_message(email)
    print('all good boss!')