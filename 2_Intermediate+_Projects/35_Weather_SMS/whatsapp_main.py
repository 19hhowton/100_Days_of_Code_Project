import requests


URL_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

## Home Lat/Long
# weather_params = {
#     "lat" : 12.957,
#     "lon" : 77.401,
#     "appid" : "ce5d45b3516066fb8fbb8a11b95e04ee",
#     "cnt" : 4,
# }    

## Fake Lat/Long
weather_params = {
    "lat" : 21.59,
    "lon" : 74.56,
    "appid" : "ce5d45b3516066fb8fbb8a11b95e04ee",
    "cnt" : 4,
}                   

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
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }

    json_data = {
        'from': '14157386102',
        'to': '917619177011',
        'message_type': 'text',
        'text': "Looks like it might rain today. Don't forget to bring an umbrella! ",
        'channel': 'whatsapp',
    }

    response = requests.post(
        'https://messages-sandbox.nexmo.com/v1/messages',
        headers=headers,
        json=json_data,
        auth=('1572d60c', 'pSsgJ2ocbiIBAYiI'),
    )
    print("Bring an umbrella!")
    response.raise_for_status()

   


