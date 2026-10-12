# import requests
#
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
#
# response = requests.get(api_url)
#
# response.json()
#
# print(response.json())
# print(response.status_code)
#
# #post method to send data to the API
#
# api_url = "https://jsonplaceholder.typicode.com/todos/"
#
# data ={
#     "userId": 1,
#     "title": "Buy shawarma for self",
#     "completed": False
# }
#
# response = requests.post(api_url, json=data)
# print(response.json())
# print(response.status_code)
#
# #Put method to update data in API
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
#
# todo = {
#     "userId": 1,
#     "title": "Take a shower this morning",
#     "completed": True
# }
#
# response = requests.put(api_url, json=todo)
# print(response.json())
# print(response.status_code)
#
# #Patch method partially update data in API
#
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# todo = {
#     "completed": False
# }
#
# response = requests.patch(api_url, json= todo)
# print(response.json())
# print(response.status_code)
#
# #

# import requests
#
# #Get method to retrieve data from the API
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
#
# response = requests.get(api_url)
#
# response.json()
#
#
# print(f"Response: {response.json()}")
# print(response.status_code)
#
# #Post method to send data to the API
# api_url = "https://jsonplaceholder.typicode.com/todos"
# data = {
#     "UserId": 1,
#     "title": "Buy shawarma for self",
#     "completed": False
# }
#
# response = requests.post(api_url, json=data)
# print(f"Response: {response.json()}")
# print(response.status_code)
#
# #Put method to update data in API
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
#
# todo = {
#     "UserId": 1,
#     "title": "Take a shower this morning",
#     "completed": True
# }
#
# response = requests.put(api_url, json=todo)
# print(f"Response: {response.json()}")
# print(response.status_code)
#
# #Patch method to update data in API
# api_url = "https://jsonplaceholder.typicode.com/todos/1"
# todo = {
#     "completed": False
# }
#
# response = requests.patch(api_url, json=todo)
# print(f"Response: {response.json()}")
# print(response.status_code)
#
# #Delete method to delete data in API
# api_url = "https://jsonplaceholder.typicode.com/todos/201"
# response = requests.delete(api_url)
# print(f"Response: {response.json()}")
# print(response.status_code)

import requests
import pandas as pd

base_url = "http://www.omdbapi.com/"
api_key = "ce55c518"

params = {
    "apikey": api_key,
    "s": "transformers"
}
response = requests.get(base_url, params=params)
results = response.json().get("Search", [])


# print(f"Response: {response.json()}")
print(f"Results: {results}")
# print(results[0])

if response.status_code == 200:
    print("Request was successful!")
else:
    print("Request failed!")


movies_list = []
for result in results:
    movies_details = {
        "Title": result["Title"],
        "Year": result["Year"],
        "ID": result["imdbID"],
        "Type": result["Type"]
    }

    movies_list.append(movies_details)
print(f"movies_list: {movies_list}")

movies_df = pd.DataFrame(movies_list)
print(f"movies in my DF: \n{movies_df}")