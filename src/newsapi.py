#****************************************************************
#                           Libraries
#****************************************************************

import requests
from dotenv import load_dotenv
import os
from time import strftime,gmtime

# Import config
from config import Config
from src.email.send_email import send_email
#****************************************************************
#                       Preconfiguration
#****************************************************************

# Initializing dotenv and Config
load_dotenv()
load_dotenv('.env.params')

mi_config = Config()


# Loading environment variables
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Base URL

base_url = mi_config.url

#****************************************************************
#                       Program
#****************************************************************

main = os.getenv('MAIN','everything')
country = os.getenv('COUNTRY','us')
sources = os.getenv('SOURCES')
topic = os.getenv('TOPIC')
language = 'en'#os.getenv('LANGUAGE','en')
domains = os.getenv('DOMAINS')

# Retrieve the last news (remember it is always from yesterday in the API free version) as default
date_format = f"%Y-%m-{gmtime().tm_mday -1}"
date_from_default = strftime(date_format, gmtime())
date_from = os.getenv('DATE_FROM',date_from_default)





sort_by="publishedAt"
rest_url = f"everything?q={topic}&from={date_from}&sortBy={sort_by}&language={language}&domains={domains}&sources={sources}&apiKey={NEWS_API_KEY}"

# Request
full_url = base_url + rest_url
print(full_url)

def RetrieveNews():
    try:
        r = requests.get(full_url)
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print("Timeout error!")
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print("TooManyRedirects!")
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        raise SystemExit(e)

    content = r.json()
    # Access the article titles and description
    body = ""
    for article in content["articles"][:20]:
        if article["title"] is not None:
            body = (
                body
                + article["title"]
                + "\n"
                + article["description"]
                + 2 * "\n"
                + "URL: " + article["url"]
                + 3 * "\n"
        )

    #if (body == ""):
    #    body = "There is no results... check the params"

    print(body)
    #send_email(body)
