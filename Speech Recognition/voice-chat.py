import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os


# Initialize text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()

def wish():
    hour  = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >=12 and hour <16:
        speak("Good afternoon")
    elif hour >=16 and hour <18:
        speak("Good Evening")
    else:
        speak("Good Night")

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio)
        print(f"User said: {query}\n")
        return query.lower()

    except Exception as e:
        print("Sorry, Say again")
        return "None"


if __name__ == "__main__":
    wish()
    while True:
        command = listen()

        if "hello" in command:
            speak("Hi there!")
        elif "goodbye" in command:
            speak("Goodbye!")
            break
        elif "play music" in command:
            music_dir = os.path.abspath('put your path')
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open google' in command:
            webbrowser.open("google.com")
        else:
            speak("I'm sorry, I don't understand.")


