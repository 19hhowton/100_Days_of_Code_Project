import pprint
import requests

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
    # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url="https://api.sheety.co/85f2b9b9a2bb548204ee85606ddff07e/flightDeals/prices")
        data = response.json()
        self.destination_data = data["prices"]
        pprint.pprint(self.destination_data)
        return self.destination_data
        
    def update_destination_codes(self):        
        """Update  only the iata codes in the the Google Sheet 
        using only self.destination_data's iata codes."""
        print(self.destination_data)
        for city in self.destination_data:              
            new_data = {
                "price" : {
                    'iataCode': city["iataCode"], 
            }}
            
            row_id = city["id"]
                    
            url = f"https://api.sheety.co/85f2b9b9a2bb548204ee85606ddff07e/flightDeals/prices/{row_id}"
            response = requests.put(url=url,  
                                    json=new_data)

            print(response.text)
            response.raise_for_status()
    
