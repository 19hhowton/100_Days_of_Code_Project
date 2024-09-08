import requests
from bs4 import BeautifulSoup
from twilio.rest import Client
import os
from dotenv import load_dotenv 

load_dotenv("47_Amazon_Price_Tracker\.env")

########## TWILIO CONFIG ##########
account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
client = Client(account_sid, auth_token)


########## DATA SCRAPE ##########
URL = "https://appbrewery.github.io/instant_pot/"
response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

a_price_whole = soup.find(name="span", class_="a-price-whole")
price_whole = a_price_whole.get_text()

a_price_decimal = soup.find(name="span", class_="a-price-fraction")
price_decimal = a_price_decimal.string

price = f"{price_whole}{price_decimal}"

########## ##########
if float(price) < 100:
  message = client.messages.create(
    from_='+18886022720',
    body=f"Instant Pot Duo is at ${price}. You can buy it here: {URL}",
    to='+15125200338'
  )

  print(message.sid)