import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "c7ec7f357caf44c3a582c03dfaa03f77"

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/in/apoorva-panwar488/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
    
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles:
                speak(article['title'])

    

if __name__ == "__main__":
    speak("Initializing Chatur....")
    while True:
    # Listen for the wake word "Chatur"
    # obtain audio from the microphone
        r = sr.Recognizer()
        

        # recognize speech using google
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "Hello"):
                speak("ha")
            #Listen for command
            with sr.Microphone() as source:
                print("Chatur Active")
                audio = r.listen(source)
                command = r.recognize_google(audio)

                processCommand(command)


        except Exception as e:
            print("Error; {0}".format(e))