import smtplib, ssl
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from config.config import Config
from dotenv import load_dotenv 
import os
from pathlib import Path
from jinja2 import Environment, FileSystemLoader



# Instantiate Config and environment variables
Config = Config()
load_dotenv()

# Loading environment for jinja2
env = Environment(loader=FileSystemLoader('%s/templates/' % os.path.dirname(__file__)))

template = env.get_template("child.html")

# Setting project root dir
project_root = Path(__file__).resolve().parent

def get_html(file:str):

    with open(file,'r') as html:
        return html.read()


def send_email(message):
    """ Function for sending hmtl email to recipients
    """
    # Loading environment variables
    host = Config.smtp_server
    port = Config.smtp_port
    subject = Config.subject

    sender_email = os.getenv('SMTP_USERNAME')
    sender_email_pass = os.getenv('SMTP_PASSWORD')
    recipients = os.getenv('RECIPIENTS')

    # Setting multipart MIME
    msg = MIMEMultipart()

    # Setting email parameters
    msg["to"] = os.getenv('RECIPIENTS')
    msg["from"] = sender_email
    msg["subject"] = subject

    # Loading json content in 
    html = template.render(**message)

    msg.attach(MIMEText(html, "html", "utf-8"))

    context = ssl.create_default_context()
    
    try:
        with smtplib.SMTP_SSL(host, port, context=context) as server:
            server.login(sender_email, sender_email_pass)
            server.send_message(msg)
    except smtplib.SMTPResponseException as ex:
        print(f"Error {ex}")
    
    
    