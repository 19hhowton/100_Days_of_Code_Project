import requests
import pprint
import vonage

URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

# weather_params = {
#     "lat" : 12.957,
#     "lon" : 77.401,
#     "appid" : "ce5d45b3516066fb8fbb8a11b95e04ee",
#     "cnt" : 4,
# }       

weather_params = {
    "lat" : 21.59,
    "lon" : 74.56,
    "appid" : "ce5d45b3516066fb8fbb8a11b95e04ee",
    "cnt" : 4,
}               

heather_number = 917619177011
sharada_number = 917619177022

response = requests.get(URL_ENDPOINT, params = weather_params)
response.raise_for_status()
weather_data = response.json()

to_bring_umbrella = False
for period in weather_data["list"]:
    # print(period["weather"][0]["id"])
    weather_id = period["weather"][0]["id"]
    if int(weather_id) < 700:
        to_bring_umbrella = True
if to_bring_umbrella:
    print("Don't forget to bring an umbrella!")
    client = vonage.Client(key="1572d60c", secret="pSsgJ2ocbiIBAYiI")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
    {
        "from": "Heather's Weather Updates",
        "to": f"{heather_number}",
        "text": "Looks like it might rain today. Don't forget to bring an umbrella! ",
    })

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
