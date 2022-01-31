from re import search
import pyttsx3
import datetime
import wikipedia
import os
import json
import subprocess
import requests
import webbrowser
import speech_recognition as sr
import pywhatkit
pywhatkit.start_server()
from utils import opening_text 


def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

OPENWEATHER_APP_ID = "c679fbae69a4509fd1c6077f8de74eb5"
def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()




def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good mafternoon!")
    else:
        speak("Good evening!")
    speak("I am Jarvis. At your service, Miss Salsabil")

def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("Today is " + day_of_the_week)
  
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing...")    
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n") 

    except Exception as e:
        # print(e)    
        speak("Say that again please")
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        return "None" #None string will be returned
    return query

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        elif 'open vs code' in query:
            codePath = "C:\\Users\\Anika Salsabil\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"
            os.startfile(codePath)

        elif 'open documents' in query:
            codePath = "C:\\Users\\Anika Salsabil\\Documents"
            os.startfile(codePath)
        elif 'open documents' in query:
            codePath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word 2016.lnk"
            os.startfile(codePath)
        
        elif 'youtube' in query:
            speak("What do you want to play on Youtube, Ma'am?")
            video = takeCommand().lower()
            pywhatkit.playonyt(video)
        elif 'play' and 'song' in query:
            speak("What do you want to hear, Ma'am?")
            video = takeCommand().lower()
            pywhatkit.playonyt(video)
            speak("Sure, on it")
        elif "which day it is" in query:
            tellDay()
        elif "what day it is" in query:
            tellDay()
        elif "what is the day" in query:
            tellDay()
        elif 'open google' in query:
            webbrowser.open("www.google.com")
            speak("Sure")
        elif 'search' in query:
            speak("Wait a second")
            se = takeCommand().lower()
            pywhatkit.search(se)
            speak("on it")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p")    
            speak(f"Ma'am, the time is {strTime}")
        elif "tell me your name" in query:
            speak("I am Jarvis. Your desktop Assistant")
        elif "who are you" in query:
            speak("I am Jarvis, Just a really very intelligent system. I am your personal Assistant.")
        elif "what's my name" in query:
            speak("You are Anika Salsabil.")
        elif "who am I" in query:
            speak("You are Anika Salsabil. My creator")
        elif "your butt" in query:
            speak("Sorry. I am shy")
        elif "who made you" in query:
            speak("Miss Anika Salsabil created me")
        elif "are not intelligent" in query:
            speak("I am on development phase. I am still learning. no need to be rude")
        elif "are not so intelligent" in query:
            speak("I am on development phase. I am still learning. no need to be rude")
        elif "are you there" in query:
            speak("Yes! At your service")
        elif "jarvis" in query:
            speak("Yes! At your service")
        elif "come back jarvis" in query:
            speak("Ok. I am back")
        elif "stop" in query:
            speak("Ok.")
        elif "stop talking" in query:
            speak("Ok.")
        elif "go off" in query:
            speak("K. bye")
        elif "shut up" in query:
            speak("K. bye")
        elif "shutdown" in query:
            speak("K. bye")
        elif "how are you" in query:
            speak("I am doing good. I am on some new shit")
        elif "what's up" in query:
            speak("I am doing good. I am on some new shit")
        elif "how you doing" in query:
            speak("I am doing good. I am on some new shit. How you doing")
        elif "i love you" in query:
            speak("I would have said the same but I am not really capable of that")
        elif "love me" in query:
            speak("I am not really capable of that")
        elif "hi" in query:
            speak("hello")
        elif "hello" in query:
            speak("hi")

        elif 'ip address' in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
            print(f'Your IP Address is {ip_address}')

        elif 'weather' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen sir.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
        
        elif "log off" in query or "sign out" in query or "shut down the pc" in query:
            speak("Ok , your pc will log off in 10 sec make sure you exit from all applications")
            subprocess.call(["shutdown", "/l"])

        
    



