import os
from dotenv import load_dotenv 
import requests
from datetime import datetime
import pprint

load_dotenv("38_Fitness_Tracker\.env")

### NUTRITIONIX CONFIG ###
NX_APP_ID = os.getenv("NX_APP_ID")
NX_API_KEY = os.getenv("NX_API_KEY")
nutri_endpoint = os.getenv("NX_ENDPOINT")

### SHEETY CONFIG ##
username = os.getenv("SHEETY_USERNAME")
projectName = os.getenv("SHEETY_PROJECT_NAME")
sheetName = os.getenv("SHEETY_SHEET_NAME")
sheet_url = f"https://api.sheety.co/{username}/{projectName}/{sheetName}"

### NUTRITIONIX REQUEST ###
query = input("Tell me what excercises you did: ")

query_json = {
    "query": query,
}
headers = {
    "Content-Type": "application/json",
    "x-app-id": NX_APP_ID,
    "x-app-key": NX_API_KEY,
}
response = requests.post(url=nutri_endpoint, json=query_json, headers=headers)
response.raise_for_status()
query_response = response.json()

### SHEETY REQUEST ###
for exercise in query_response["exercises"]:
    exercise_type = exercise["name"] 
    duration = exercise["duration_min"] 
    calories = exercise["nf_calories"] 
    
    sheet_inputs = {
    "workout": {
            "date": datetime.now().strftime("%d/%m/%Y"),
            "time": datetime.now().strftime("%X"),
            "exercise": exercise_type,
            "duration": duration,
            "calories": calories
}
    }

    response = requests.post(url=sheet_url, json=sheet_inputs)
    print(response.text)
    response.raise_for_status()




# response = requests.get(url=sheet_endpoint)
# print(response.text)
# response.raise_for_status()


