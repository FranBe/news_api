import smtplib, ssl
from email.message import EmailMessage
from config import Config
from dotenv import load_dotenv 
import os
from pathlib import Path

# Instantiate Config and environment variables
Config = Config()
load_dotenv()

project_root = Path(__file__).resolve().parent

def get_html(file:str):

    with open(file,'r') as html:
        return html.read()


def send_email(message):

    host = Config.smtp_server
    port = Config.smtp_port

    sender_email = os.getenv('SMTP_USERNAME')
    sender_email_pass = os.getenv('SMTP_PASSWORD')
    recipients = Config.recipients

    print(os.getcwd())
    html = get_html(project_root / 'templates/email.html')

    msg = EmailMessage()
    msg["to"] = Config.recipients
    msg["from"] = sender_email
    msg["subject"] = "Test Message News API"
    msg.set_content(message)
    #msg.add_alternative(html, subtype="html")

    print(msg)

    context = ssl.create_default_context()

    
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(sender_email, sender_email_pass)
            server.send_message(msg)
    except smtplib.SMTPResponseException as ex:
        print(f"Error {ex}")
    