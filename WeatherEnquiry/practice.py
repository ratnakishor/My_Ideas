from urllib import request
from pprint import pprint
import json

key = "31fb471476700640453ec247078619aa"
city = input("Enter the city name: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

response = request.urlopen(url)
json_data = response.read()
data = json.loads(json_data)

pprint(data["main"]["temp"])