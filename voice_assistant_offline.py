import speech_recognition as sr
import pyttsx3
import datetime
import os
import webbrowser
import time

engine = pyttsx3.init()

def speak(text):
    print(f"Assistant: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Listening...")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query.lower()
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def tell_time():
    now = datetime.datetime.now().strftime("%I:%M %p")
    speak(f"The current time is {now}")

def open_website(website_name):
    websites = {
        "google": "https://www.google.com",
        "youtube": "https://www.youtube.com",
        "github": "https://github.com"
    }
    if website_name in websites:
        speak(f"Opening {website_name}")
        webbrowser.open(websites[website_name])
    else:
        speak(f"I don't know {website_name}")

def play_music():
    music_folder = "music"
    try:
        songs = os.listdir(music_folder)
        if songs:
            song_path = os.path.join(music_folder, songs[0])
            os.startfile(song_path)
            speak("Playing music.")
        else:
            speak("No music files found.")
    except:
        speak("Couldn't play music.")

def set_reminder():
    speak("What should I remind you about?")
    reminder = listen()
    speak("In how many seconds should I remind you?")
    try:
        delay = int(listen())
        speak(f"Reminder set for {delay} seconds.")
        time.sleep(delay)
        speak(f"Reminder: {reminder}")
    except:
        speak("Invalid time.")

def main():
    speak("Hello! I'm your voice assistant.")
    while True:
        speak("How can I help you?")
        command = listen()

        if "time" in command:
            tell_time()
        elif "open" in command:
            for word in ["google", "youtube", "github"]:
                if word in command:
                    open_website(word)
                    break
        elif "music" in command or "play" in command:
            play_music()
        elif "reminder" in command or "remind" in command:
            set_reminder()
        elif "stop" in command or "exit" in command:
            speak("Goodbye!")
            break
        else:
            speak("I can tell the time, open websites, play music, and set reminders.")

if __name__ == "__main__":
    main()
