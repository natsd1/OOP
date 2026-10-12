import requests
import pandas as pd

base_url = "http://www.omdbapi.com/"
api_key = "ce55c518"

param = {
    "apikey": api_key,
    "S": "Avatar"
}
response = requests.get(base_url, params=param)


print(response.json())

if response.status_code == 200:
    print("Response successful")
else:
    print("Response failed")

movies_list = []
for movie in response.json()['Movies']: