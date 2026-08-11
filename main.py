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
    try:
        print(f"Processing command: {c}")
        
        if "open google" in c.lower():
            webbrowser.open("https://www.google.com/")
            speak("Opening Google")
        elif "open youtube" in c.lower():
            webbrowser.open("https://youtube.com/")
            speak("Opening YouTube")
        elif "open linkedin" in c.lower():
            webbrowser.open("https://www.linkedin.com/in/apoorva-panwar488/")
            speak("Opening LinkedIn")
        elif "play" in c.lower():
            # Extract song name (everything after "play")
            song_name = c.lower().replace("play", "").strip()
            print(f"Looking for song: '{song_name}'")
            print(f"Available songs: {list(musicLibrary.music.keys())}")
            
            if song_name in musicLibrary.music:
                link = musicLibrary.music[song_name]
                webbrowser.open(link)
                speak(f"Playing {song_name}")
                print(f"Successfully opened: {link}")
            else:
                speak(f"Sorry, I don't have {song_name} in my library")
                print(f"Song '{song_name}' not found")
        elif "news" in c.lower():
            speak("Fetching news for you")
            print("Fetching news...")
            try:
                r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}", timeout=10)
                print(f"News API response status: {r.status_code}")
                
                if r.status_code == 200:
                    data = r.json()
                    articles = data.get('articles', [])
                    print(f"Found {len(articles)} articles")
                    
                    if articles:
                        speak(f"Here are the top headlines")
                        for i, article in enumerate(articles[:3], 1):
                            print(f"Headline {i}: {article['title']}")
                            speak(f"Headline {i}: {article['title']}")
                    else:
                        speak("No news found")
                else:
                    error_msg = r.json().get('message', 'Unknown error')
                    print(f"News API error: {error_msg}")
                    speak("Failed to fetch news")
            except requests.exceptions.Timeout:
                print("News API request timed out")
                speak("The news service is taking too long. Please try again")
            except Exception as news_error:
                print(f"News fetching error: {news_error}")
                speak("Could not fetch news at the moment")
        else:
            speak("I didn't understand that command. Please try again")
    except Exception as e:
        print(f"Error in processCommand: {type(e).__name__}: {e}")
        speak("Sorry, something went wrong while processing your command")

if __name__ == "__main__":
    speak("Initializing Chatur....")
    while True:
        r = sr.Recognizer()
        # Adjust recognizer sensitivity
        r.energy_threshold = 4000
        
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                # Longer timeout and phrase_time_limit for better recognition
                audio = r.listen(source, timeout=10, phrase_time_limit=3)
            word = r.recognize_google(audio)
            print(f"Recognized: {word}")
            
            # Check if "chatur" is mentioned (not exact match)
            if "chatur" in word.lower():
                speak("Yes, I'm listening")
                print("Chatur Active... Listening for command")
                
                # Listen for command with longer timeout
                with sr.Microphone() as source:
                    audio = r.listen(source, timeout=10, phrase_time_limit=4)
                    command = r.recognize_google(audio)
                    print(f"Command received: {command}")

                processCommand(command)


        except sr.UnknownValueError:
            print("Could not understand audio")
            speak("Sorry, I couldn't understand that. Please try again")
        except sr.RequestError as e:
            print(f"Error with Google Speech Recognition: {e}")
            speak("There was an error with the speech recognition service")
        except Exception as e:
            print(f"Error: {e}")
            speak("Sorry, an error occurred. Please try again")