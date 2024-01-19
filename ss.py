import requests
from ss import *

key = '1fbba753a8d549e38cec024e647b0643'
api_address="https://newsapi.org/v2/everything?q=tesla&from=2023-12-18&sortBy=publishedAt&apiKey=" + key 
json_data = requests.get(api_address).json()



ar=[]

def news():
    for i in range (3):
        ar.append("Number "+str(i+1) + json_data["articles"][i]["title"]+" . ")

    return ar

  