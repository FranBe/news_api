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
from utils import format_utils
#****************************************************************
#                       Preconfiguration
#****************************************************************

# Initializing dotenv and Config
load_dotenv() # General env variables
load_dotenv('.env.newsapi') # Spescific env variables

mi_config = Config() # General config variables



#****************************************************************
#                    Functions/procedures
#****************************************************************

def GetFullUrl():
    """ Procedure for getting the full URL needed by the API
    """

    # Loading environment variables
    NEWS_API_KEY = os.getenv('NEWS_API_KEY')

    # Base URL
    base_url = mi_config.base_url

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

    return full_url


def RetrieveNews(url:str):
    """ Function for retrieving news from API and send them by email

    Args:
        url(str): full url API with endpoints and parameters

    Returns:
        response: response requests object
    """
    try:
        r = requests.get(url)
        return r
    except requests.exceptions.Timeout:
        # Maybe set up for a retry, or continue in a retry loop
        print("Timeout error!")
        return None
    except requests.exceptions.TooManyRedirects:
        # Tell the user their URL was bad and try a different one
        print("TooManyRedirects!")
        return None
    except requests.exceptions.RequestException as e:
        # catastrophic error. bail.
        print("asd")
        raise SystemExit(e)

def GetJsonContent(url:str):
    """Function for getting json needed for email message"""

    r = RetrieveNews(url)
    
    return r.json()