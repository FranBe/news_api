#****************************************************************
#                           Libraries
#****************************************************************

import requests
from dotenv import load_dotenv
import os

# Import config
from config.config import Config

#****************************************************************
#                       Preconfiguration
#****************************************************************

# Initializing dotenv and Config
load_dotenv()
mi_config = Config()


# Loading environment variables
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

# Base URL

base_url = mi_config.url

#****************************************************************
#                       Program
#****************************************************************

main = "everything"
country = "us"
source = "bbc-news"
subject="el niño"
date_from="2026-09-20"
sort_by="popularity"
rest_url = f"everything?q={subject}&from={date_from}&sortBy={sort_by}&apiKey={NEWS_API_KEY}"

# Request
full_url = base_url + rest_url
print(full_url)

"""
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

for article in content["articles"]:
    print(article["title"])
    print("------------------------")
    print(article["description"])
    print("***********************")



# Access the article titles and description
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body = body + article["title"] + "\n" + str(article["description"]) + 2*"\n"

body = body.encode("utf-8")
send_email(message=body)


"""