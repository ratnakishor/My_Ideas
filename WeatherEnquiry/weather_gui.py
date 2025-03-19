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
 
    for widget in frame2.winfo_children():
        widget.destroy()  # Remove all widgets inside the frame

    key = "OpenWeather API key"
    city = e.get()#input("Enter the city name: ")
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={key}'

    try:
        response = request.urlopen(url)
        data = response.read()
        weather = json.loads(data)

    except error.HTTPError:    
        print("City not found.")
        speak("City Not Found.")
        tkinter.Label(frame2, text = "Not Found", fg = "red").grid(row = 2, column = 0)
        tkinter.Label(frame2, text = "Not Found", fg = "red").grid(row = 4, column = 0)
        tkinter.Label(frame2, text = "Not Found", fg = "red").grid(row = 6, column = 0)
        tkinter.Label(frame2, text = "Not Found", fg = "red").grid(row = 8, column = 0)
    

        #os._exit(0)
    
    

    city = f"City: {weather['name']}. "
    #country = f"Country: {weather['sys']['country']}. "
    state = f"Weather: {weather['weather'][0]['main']}. "
    temp = f"Temperature: {weather['main']['temp']} degrees. "
    humidity = f"Humidity: {weather['main']['humidity']} percent. "
    
    l1 = tkinter.Label(frame2, text = city, fg = "red")
    l1.grid(row = 2, column = 0, padx = 10, pady = 10)
    tkinter.Label(frame2, text = state, fg = "red").grid(row = 4, column = 0, padx = 10, pady = 10)
    tkinter.Label(frame2, text = temp, fg = "red").grid(row = 6, column = 0, padx = 10, pady = 10)
    tkinter.Label(frame2, text = humidity, fg = "red").grid(row = 8, column = 0, padx = 10, pady = 10)
    
    
    print(city)
    #print(country)
    print(state)
    print(temp)
    print(humidity)

    speak(city + state + temp + humidity)
    

window = tkinter.Tk()
window.geometry("450x200")
window.title("Weather Data")

frame1 = tkinter.Frame(window, padx=20, highlightthickness=3)
frame1.grid(row=0, column=0)

frame2 = tkinter.Frame(window, padx=20)
frame2.grid(row=0, column=1)



tkinter.Label(frame1, text = "Enter City Name:", fg = "green").grid(row = 2, column = 0)

e = tkinter.Entry(frame1, width = 25, text = " Enter City Name")
e.grid(row = 4, column = 0, padx = 10, pady = 10)

button = tkinter.Button(frame1, text='Submit', command = weather)
button.grid(row = 6, column = 0, padx = 10, pady = 10)


exit_button = tkinter.Button(frame1, text='Exit', command = window.destroy, padx = 10, pady = 10)
exit_button.grid(row = 8, column = 0)

window.mainloop()