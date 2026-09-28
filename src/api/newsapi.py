#****************************************************************
#                           Libraries
#****************************************************************

import requests
from dotenv import load_dotenv
import os
from time import strftime,gmtime

# Import config
from config.config import Config
from mailing.send_email import send_email
#****************************************************************
#                       Preconfiguration
#****************************************************************

# Initializing dotenv and Config
load_dotenv()
load_dotenv('.env.newsapi')

mi_config = Config()


# Loading environment variables
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Base URL

base_url = mi_config.base_url

#****************************************************************
#                       Program
#****************************************************************

# News API with defaults parameters
main = os.getenv('MAIN','everything')
country = os.getenv('COUNTRY','us')
sources = os.getenv('SOURCES','bbc-news')
topic = os.getenv('TOPIC')
language = os.getenv('LANG_NEWS','en')
domains = os.getenv('DOMAINS','bbc.co.uk')
sort_by = os.getenv('SORT_BY','publishedAt')
limit = int(os.getenv('LIMIT',20))

# Retrieve the last news  as default (remember they're from yesterday since I'm using free version of the API)
date_format = f"%Y-%m-{gmtime().tm_mday -1}"
date_from_default = strftime(date_format, gmtime())
date_from = os.getenv('DATE_FROM',date_from_default)

# Rest of URL with endpoints and parameters
rest_url = f"everything?q='{topic}'&from={date_from}&sortBy={sort_by}&language={language}&domains={domains}&sources={sources}&apiKey={NEWS_API_KEY}"

# Request
full_url = base_url + rest_url

def RetrieveNews():
    """ Function for retrieving news from API and send them by email
    """

    # string variable for request final result
    body = ""

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

     # Access the article titles and description when there isn't any error message from API
    if content["status"] != "error":
        for article in content["articles"][:limit]:
            if article["title"] is not None:
                body = (
                    body
                    + 2 * "\n"
                    + article["publishedAt"]
                    + "\n"
                    + article["title"]
                    + "\n"
                    + article["description"]
                    + 2 * "\n"
                    + "URL: " + article["url"]
                    + 2 * "\n"
                    + 20 * "-" 

            )
    else:
        body = (
        "Error!"
        + "\n" 
        + "Code:" + content["code"]
        + "\n" 
        + "Message:" + content["message"])

    print(body)
    send_email(body)
