import sys
#import google
from googlesearch import search
import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import pyaudio
import time
import requests,json

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()

#talk("hello")


def take_command():

    with sr.Microphone() as source:
        print('listening...')
        listener.adjust_for_ambient_noise(source)
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
                print(command)
        except LookupError:
            print("Could not understand audio")
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    #elif 'time' in command:
     #   time = datetime.datetime.now().strftime('%I:%M %p')
      #  talk('Current time is ' + time)
    elif 'who the heck is' in command:
        person = command.replace('who the heck is', '')
        info = wikipedia.summary(person, 1)
        print(info)
        talk(info)
    elif 'date' in command:
        #talk('sorry, I have a headache')
        dt=str(datetime.date.today())
        print(dt)
        talk("Today's date is"+ dt)
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'weather' in command:     # Enter your API key here
        api_key = "b49fc337dde81490958f556094103567"

        # base_url variable to store url
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        # Give city name
        #city_name = input("Enter city name : ")
        city_name = "ahmedabad"
        # complete_url variable to store
        # complete url address
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # get method of requests module
        # return response object
        response = requests.get(complete_url)
        # python format data
        x = response.json()

        # city is not found
        if x["cod"] != "404":
            # store the value of "main"
            # key in variable y
            y = x["main"]

            # store the value corresponding
            # to the "temp" key of y
            current_temperature = y["temp"]-273.15
            # print following values
            print(" Temperature (in celcius unit) = " +
                  str(current_temperature) )
            talk(current_temperature)
        else:
            print(" City Not Found ")
    elif 'stop' in command:
        sys.exit()
    elif 'search the internet' or 'search the web' or 'search' or 'search google' in command:
        print("hi from google")
        query = command.replace('search the internet', '')
        for j in search(query, tld='co.in', num=10, stop=10, pause=2):
            print(j)

    elif 'set timer' or 'timer' or 'set a timer' in command:
        t = command.replace('set timer', '')
        print(t)
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
        print('Fire in the hole!!')
    else:
        talk('Please say the command again.')


while True:
    run_alexa()
