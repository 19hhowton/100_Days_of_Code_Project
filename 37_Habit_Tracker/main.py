import requests
from datetime import datetime

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME = "hhowton19"
TOKEN = "aknodiskv"
GRAPH_ID = "cycle1"
headers = {
        "X-USER-TOKEN": TOKEN
    }
today_full = datetime.now()
today = today_full.strftime("%Y%m%d")

#######################################

# def create_user(TOKEN, USERNAME):
#     user_params = {
#         "token": {TOKEN},
#         "username": {USERNAME},
#         "agreeTermsofService": "yes",
#         "notMinor": "yes",
#     }
#     response = requests.post(url=pixela_endpoint, json=user_params)
#     # print(response.text)
#     # https://pixe.la/@hhowton19


# def create_graph(TOKEN, USERNAME):
#     # graph_endpoint = "https://pixe.la/v1/users/a-know/graphs"
#     graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

#     graph_params = {
#         "id": "cycle1",
#         "name": "S&H Cycle",
#         "unit": "km",
#         "type": "int",
#         "color": "momiji",
#     }

#     response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
#     print(response.text)

# def create_pixel():
#     single_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/"

#     pixel_params = {
#         "date": today,
#         "quantity": "5",
#     }

#     response = requests.post(url=single_pixel_endpoint, json=pixel_params, headers=headers)
#     print(response.text)

# def delete_pixel():
#     delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today}"


#     response = requests.delete(url=delete_pixel_endpoint, headers=headers)
#     print(response.text)