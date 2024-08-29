import requests
from datetime import datetime

# MY_LAT = 12.971599
MY_LAT = 12.971599
MY_LONG = 77.594566

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    print(iss_latitude, iss_longitude)
    if iss_latitude >= (MY_LAT-5) and iss_latitude <= (MY_LAT+5) and iss_latitude >= (MY_LONG-5) and iss_latitude <= (MY_LONG+5):
        print("Your position is within +5 or -5 degrees of the ISS position")

    return True

def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()

    sunrise = data["results"]["sunrise"]
    sunrise_formatted = int(sunrise.split("T")[1].split(":")[0])
    sunset = data["results"]["sunset"]
    sunset_formatted = int(sunset.split("T")[1].split(":")[0])
    print(sunrise_formatted)
    print(sunset_formatted)


    time_now = datetime.now()
    time_now_hour = time_now.hour
    print(time_now_hour)

    if time_now_hour <= sunrise_formatted and time_now_hour >= sunset_formatted:
        return True


if is_iss_overhead() and is_night():
    print("ISS is overhead.")


