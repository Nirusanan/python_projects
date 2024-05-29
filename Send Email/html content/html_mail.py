import getpass
import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "#######@outlook.com"
TO_EMAIL = "##########"
PASSWORD = getpass.getpass("Enter password: ")

message = MIMEMultipart("alternative")
message['Subject'] = "Mail with html content sent using python"
message['From'] = FROM_EMAIL
message['To'] = TO_EMAIL
message['Cc'] = FROM_EMAIL


html = ""
with open("html content/mail.html", "r") as file:
    html = file.read()

html_part = MIMEText(html, 'html')
message.attach(html_part)
print(message)

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, message.as_string())
smtp.quit()