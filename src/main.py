from api.newsapi import GetFullUrl,GetJsonContent
from mailing.send_email import send_email

def main():

    # Getting API full url
    full_url = GetFullUrl()

    # Json content for email message
    content = GetJsonContent(full_url)

    # Sending email
    send_email(content)


if __name__ == "__main__":
    main()