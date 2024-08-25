import requests
from datetime import datetime, timedelta
import vonage
# import pprint

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

## Get Yesteray and Day Before Yesterday
Y = datetime.now() - timedelta(1)
Y_DATE = datetime.strftime(Y, "%Y-%m-%d")
DBY = datetime.now() - timedelta(2)
DBY_DATE = datetime.strftime(DBY, "%Y-%m-%d")


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday at CLOSING then print("Get News").
alpha_APIKEY = "MJ6VKQ5XGMPQ0S40"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": alpha_APIKEY,
}

STOCK_ENDPOINT = f'https://www.alphavantage.co/query'

alpha_r = requests.get(STOCK_ENDPOINT, params=stock_params)
alpha_data = alpha_r.json()

yesterday_close = float(alpha_data["Time Series (Daily)"][Y_DATE]["4. close"])
day_before_yesterday_close = float(alpha_data["Time Series (Daily)"][DBY_DATE]["4. close"])
difference = yesterday_close - day_before_yesterday_close
percent_difference = round(((difference / yesterday_close) * 100), 2)

def get_arrow(percent_difference):
    if percent_difference > 0:
        return "🔺"
    else: 
        return "🔻" 

arrow = get_arrow(percent_difference)



## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
news_APIKEY = "c84a280e1b134c7fb0773be9190889ba"

Y_news_url = f"https://newsapi.org/v2/everything?q={STOCK}&from={Y_DATE}&to={Y_DATE}&sortBy=popularity&apiKey={news_APIKEY}"

news_r = requests.get(Y_news_url)
news_data = news_r.json()

title_0 = news_data["articles"][0]["title"]
desc_0 = news_data["articles"][0]["description"]

title_1 = news_data["articles"][1]["title"]
desc_1 = news_data["articles"][1]["description"]

title_2 = news_data["articles"][2]["title"]
desc_2 = news_data["articles"][2]["description"]

message = f"{STOCK} {arrow} {percent_difference} \n \
  1. Headline: {title_0} \n \
     Brief: {desc_0}   \n \
  2. Headline: {title_1} \n \
     Brief: {desc_1}   \n \
  3. Headline: {title_2} \n \
     Brief: {desc_2}   \n \ "

print(message)

## STEP 3: Use VONTAGE
# Send a seperate message with the percentage change and each article's title and description to your phone number. 

# client = vonage.Client(key="1572d60c", secret="pSsgJ2ocbiIBAYiI")
# sms = vonage.Sms(client)

# responseData = sms.send_message(
#     {
#         "from": "TSLA Stock Updates",
#         "to": "917619177011",
#         "text": f"{message}",
#     }
# )

# if responseData["messages"][0]["status"] == "0":
#     print("Message sent successfully.")
# else:
#     print(f"Message failed with error: {responseData['messages'][0]['error-text']}")










#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

