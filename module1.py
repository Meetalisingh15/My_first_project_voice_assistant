#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      dines
#
# Created:     22-05-2024
# Copyright:   (c) dines 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pyttsx3 as p
import speech_recognition as sr
from selenium_web import *
from youtube_auto import *
from news import *
from jokes import *
import randfacts
from weather import *
import datetime
import webbrowser
engine=p.init()
rate=engine.getProperty('rate')
engine.setProperty('rate',160)
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
def speak(text):
    engine.say(text)
    engine.runAndWait()
def wish_me():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        return("morning")
    elif hour>=12 and hour<16:
        return("afternoon")
    else:
        return("evening")
today_date=datetime.datetime.now()
r=sr.Recognizer()
speak("hello sir, good"+wish_me()+", i am your voice assistant")
speak("today is"+today_date.strftime("%d")+"of"+today_date.strftime("%B")+"and its currently"+today_date.strftime("%I")+today_date.strftime("%M")+today_date.strftime("%p"))
speak("temperature in new delhi is"+str(temp())+"degree celsius,and with"+str(des()))
speak("how are you?")
with sr.Microphone() as source:
    r.energy_threshold=10000
    r.adjust_for_ambient_noise(source,1.2)
    print("listening...")
    audio=r.listen(source)
    text=r.recognize_google(audio)
    print(text)
if "what" and "about" and "you" in text:
    speak("i am having a good day sir")
speak("what can i do for you?")
with sr.Microphone() as source:
        r.energy_threshold=10000
        r.adjust_for_ambient_noise(source,1.2)
        print("listening...")
        audio=r.listen(source)
        text2=r.recognize_google(audio)
        print(text2)
if "information" in text2:
        speak("which type of information you need?")
        with sr.Microphone() as source:
            r.energy_threshold=10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening...")
            audio=r.listen(source)
            infor=r.recognize_google(audio)
            print(infor)
        speak("searching {} in wikipedia".format(infor))
        print("searching {} in wikipedia".format(infor))
        assist= infow()
        assist.get_info(infor)
elif "play" and "video" in text2:
        speak("you want me to play which video??")
        with sr.Microphone() as source:
            r.energy_threshold=10000
            r.adjust_for_ambient_noise(source,1.2)
            print("listening...")
            audio=r.listen(source)
            vid=r.recognize_google(audio)
            print(vid)
        speak("playing {} on youtube".format(vid))
        print("playing {} on youtube".format(vid))
        assist= music()
        assist.play(vid)
elif "news" in text2:
        print("sure sir, now i will read news for you")
        speak("sure sir, now i will read news for you")
        top_headlines = get_top_headlines()
        for i in range(len(top_headlines)):
            print(top_headlines[i])
            speak(top_headlines[i])
elif "fact" in text2:
        speak("sure sir, ")
        r=randfacts.getFact()
        print(r)
        speak("did you know that, "+r)
elif "joke" in text2:
        speak("sure sir, get ready for some chuckles ")
        ar=joke()
        print(ar[0])
        speak(ar[0])
        print(ar[1])
        speak(ar[1])

elif 'open YouTube' in text2:
        speak("Here you go to Youtube\n")
        webbrowser.open("youtube.com")
elif "open Google" in text2:
        speak("here you go to Google")
        webbrowser.open("https://www.google.com/")





