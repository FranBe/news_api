import smtplib
import ssl
from getpass import getpass


port = 465
smtp_server = "smtp.gmail.com"
sender_email = "my@gmail.com"
password = getpass("Type your password and press enter: ")

context = ssl.create_default_context()
with smtplib.SMTP_SSL(
    smtp_server,
    port,
    context=context,
    ) as server:
    server.login(sender_email, password)
    # Send email here