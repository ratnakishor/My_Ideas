import json
from urllib import request,error
import pyttsx3
import os

engine = pyttsx3.init()
engine.setProperty('rate', 125)

def speak(s):
    engine.say(s)
    engine.runAndWait()
    return

key = "your Openweather API key"
city = input("Enter the city name: ")
url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

try:
    response = request.urlopen(url)
    data = response.read()
    weather = json.loads(data)

except error.HTTPError:    
    print("City not found.")
    speak("City Not Found.")
    os._exit(0)
    
    

city = f"City: {weather['name']}. "
country = f"Country: {weather['sys']['country']}. "
state = f"Weather: {weather['weather'][0]['main']}. "
temp = f"Temperature: {weather['main']['temp']} degrees. "
humidity = f"Humidity: {weather['main']['humidity']} percent. "

speak(city + state + temp + humidity)

print(city)
#print(country)
print(state)
print(temp)
print(humidity)




