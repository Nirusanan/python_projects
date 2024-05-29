import getpass
import smtplib

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "####@outlook.com"
TO_EMAIL = "#########"
PASSWORD = getpass.getpass("Enter password: ")

MESSAGE  = """ Subject: mail sent using python
Hii all,

This is a testing email.

Thanks. """

smtp = smtplib.SMTP(HOST, PORT)

status_code, response = smtp.ehlo()
print(f"Echoing the server: {status_code} {response}")

status_code, response = smtp.starttls()
print(f"starting TLS connection: {status_code} {response}")

status_code, response = smtp.login(FROM_EMAIL, PASSWORD)
print(f"Logging in: {status_code} {response}")

smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
smtp.quit()