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
headers = {
    "Accept-Language": "en-US,en;q=0.9", 
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
  }

# URL = "https://www.amazon.com/Instant-Pot-Plus-60-Programmable/dp/B01NBKTPTS"
URL = "https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

response = requests.get(URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")

a_price_whole = soup.find(name="span", class_="a-price-whole")
price_whole = a_price_whole.get_text()

a_price_decimal = soup.find(name="span", class_="a-price-fraction")
price_decimal = a_price_decimal.string

price = f"{price_whole}{price_decimal}"
print(price)


########## SEND TWILIO MESSAGE ##########
if float(price) < 100:
  message = client.messages.create(
    from_='+18886022720',
    body=f"Instant Pot Duo is at ${price}. You can buy it here: {URL}",
    to='+15125200338'
  )

  print(message.sid)