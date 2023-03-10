import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour) 
    if hour>=0 and hour<12:
        speak("good morning sir!")
    elif hour>=12 and hour<18:
        speak("good afternoon sir!")
    else:
        speak("good evening")    
    if __name__=="__main__":
       speak("I am Javis sir . please tell me how can i help you")  

def takeCommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold=0.5
        audio = r.listen(source)

    try:
        print("recognising...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        print(e)

        print("say that agian please sir...")
        speak("say that agian please sir...")
        return "none"
    return query




if __name__=="__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=12)
            speak("according to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")    
        elif ' the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is {strTime}")
      
       

          
