import tkinter
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

def weather():
    
    key = "your Openweather API key"
    city = e.get()#input("Enter the city name: ")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

    try:
        response = request.urlopen(url)
        data = response.read()
        weather = json.loads(data)

    except error.HTTPError:    
        print("City not found.")
        speak("City Not Found.")
        tkinter.Label(window, text = "Not Found", fg = "red").grid(row = 2, column = 1)
        tkinter.Label(window, text = "Not Found", fg = "red").grid(row = 4, column = 1)
        tkinter.Label(window, text = "Not Found", fg = "red").grid(row = 6, column = 1)
    

        #os._exit(0)
    
    

    city = f"City: {weather['name']}. "
    #country = f"Country: {weather['sys']['country']}. "
    state = f"Weather: {weather['weather'][0]['main']}. "
    temp = f"Temperature: {weather['main']['temp']} degrees. "
    humidity = f"Humidity: {weather['main']['humidity']} percent. "
    
    tkinter.Label(window, text = state, fg = "red").grid(row = 2, column = 1)
    tkinter.Label(window, text = temp, fg = "red").grid(row = 4, column = 1)
    tkinter.Label(window, text = humidity, fg = "red").grid(row = 6, column = 1)
    
    
    print(city)
    #print(country)
    print(state)
    print(temp)
    print(humidity)

    speak(city + state + temp + humidity)
    

window = tkinter.Tk()
window.title("Weather Data")

button = tkinter.Button(window, text='Submit', command = weather)
button.grid(row = 4, column = 0)

e = tkinter.Entry(window, width = 25, text = "Enter City Name")
e.grid(row = 2, column = 0)


exit_button = tkinter.Button(window, text='Exit', command = window.destroy)
exit_button.grid(row = 6, column = 0)

window.mainloop()