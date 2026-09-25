from src.email import send_email
from src import newsapi

def main():

    newsapi.RetrieveNews()
    #send_email.send_email("Este es el mensaje")


if __name__ == "__main__":
    main()
