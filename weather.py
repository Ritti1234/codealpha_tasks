import requests
from ss import *

key2 = '849fa42f783970b262aa4a7e9ed27a0a'
api_address="https://api.openweathermap.org/data/2.5/weather?q=Sehore&appid=" + key2 
json_data = requests.get(api_address).json()

def temp():
    temperature=round(json_data["main"]["temp"]-273,1)
    return temperature

def des():
    description =json_data["weather"][0]["description"]
    return description

