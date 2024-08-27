#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import os
from dotenv import load_dotenv 
from flight_search import FlightSearch
from data_manager import DataManager

flight_search = FlightSearch()
flight_search.get_destination_code("Kuala Lumpur")

data_manager = DataManager()
destination_data = data_manager.get_destination_data()

for obj in destination_data:
    obj["iataCode"]
print()

# data_manager.update_destination_codes()


# self.destination_data








#######################################






















#######################################
# https://developers.amadeus.com/self-service/category/flights/api-doc/flight-offers-search/api-reference
# AM_A_C_ENDPOINT = r"https://test.api.amadeus.com/v2/shopping/flight-offers"

# AM_A_C_params = {
#     "originLocationCode": "SYD", 
#     "destinationLocationCode": "BKK",
#     "departureDate": "2024-10-10", 
#     "adults": "1",
#     "nonStop": "false", 
#     "max": "250",
# }

# AM_A_C_headers = {
#     "Authorization": f"Bearer {access_token}"
# }

# AM_A_C_response = requests.get(url=AM_A_C_ENDPOINT,  
#                         params=AM_A_C_params, 
#                         headers=AM_A_C_headers, 
#                         )

# print(AM_A_C_response.text)

