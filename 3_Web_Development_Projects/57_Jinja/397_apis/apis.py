import requests

def get_gender(name):
    genderize_url = "https://api.genderize.io"
    params = {"name": name}
    response = requests.get(url=genderize_url, params=params)
    text = response.json()
    return text["gender"]

def get_age(name):
    agify_url = "https://api.agify.io"
    params = {"name": name}
    response = requests.get(url=agify_url, params=params)
    text = response.json()
    return text["age"]

# name = "Angela"
# print(get_gender(name))
# print(get_age(name))