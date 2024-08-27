import requests
import os
from dotenv import load_dotenv 

load_dotenv("39_Basic_Flight_Tracker\.env")

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AM_API_KEY")
        self._api_secret = os.getenv("AM_SECRET_KEY")
        self._token = self._get_new_token()
    
    def _get_new_token(self):        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f"grant_type=client_credentials&client_id={self._api_key}&client_secret={self._api_secret}"

        response = requests.post('https://test.api.amadeus.com/v1/security/oauth2/token', 
                                 headers=headers, 
                                 data=data)

        response.raise_for_status()

        access_token = response.json()["access_token"]
        
        return access_token
    
    def get_destination_code(self, city_name):
        params = {
            "subType": "CITY", 
            "keyword": city_name,
            }
        
        headers = {
            "Authorization": f"Bearer {self._token}"
            }
        
                #f"{os.getenv('AM_A_C_ENDPOINT')}/reference-data/locations"
        url = "https://test.api.amadeus.com/v1/reference-data/locations"
        
        response = requests.get(url=url,  
                                params=params, 
                                headers=headers, 
                                )
    
        try: 
            iata_code = response.json()["data"][0]["iataCode"]
            print(iata_code)
            
        except:
            iata_code = "N/A"
            print("N/A") 
        
        finally:
            return iata_code