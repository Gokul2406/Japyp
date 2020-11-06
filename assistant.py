import pyttsx3
from pyttsx3 import speak
import speech_recognition as sr
from speech_recognition import UnknownValueError
import wikipedia
import webbrowser
import pyjokes
from datetime import datetime
import tkinter as tk
import threading

#If this programme is being run in a linux distro(distribution) make sure to install libspeak1 by typing 'sudo apt-get install libspeak1'


app = tk.Tk()
app.geometry('1200x720')
app.title('Japyp')

label = tk.Label(
    app, text="To speak to your assistant click the wake assistant button below")
label.pack(pady=20)

commands = tk.Label(app, text="These are the list of commands \n To open the browser say open browser \n To know what time it is ask what is the time \n To know listen to a joke ask to tell a joke \n To get information from wikipedia say the name of the topic and also include the word wikipedia in your command \n To close the app just say close")
commands.pack(pady=20)

r = sr.Recognizer()

engine = pyttsx3.init()

engine.setProperty('rate', 125)

engine.say("Hello, I am your virtual Assistant")

engine.runAndWait()


def japyp():
    while True:
        try:
            with sr.Microphone() as audio_source:
                label.config(text='Listening')
                speak("Listening...")
                r.adjust_for_ambient_noise(audio_source, duration=0.2)
                user_command = r.listen(audio_source)
                label.config(text="Recognising")
                user_text = r.recognize_google(user_command)
                user_text = user_text.lower()
                speak(f"User said {user_text}")

            if "browser" in user_text:
                speak("Opening Browser")
                webbrowser.open('https://google.com', new=0)

            elif "your name" in user_text.lower():
                speak('I am japyp. What is your name ?')
                engine.runAndWait()
                user_text = user_text.replace("what's your name", "")
                engine.runAndWait()
                speak('That is a nice name')

            elif "youtube" in user_text:
                speak("Opening Youtube...")
                webbrowser.open("https://youtube.com", new=0)

            elif "wikipedia" in user_text.lower():
                speak("Searching Wikipedia")
                user_text = user_text.replace("wikipedia", "")
                results = wikipedia.summary(user_text, sentences=2)
                speak(results)

            elif "close" in user_text.lower():
                threading.Thread(target=app.destroy()).start

            elif "time" in user_text:
                now = datetime.now()
                currnet_time = now.strftime("%H : %M : %S")
                speak(f"It is {currnet_time}")

            elif "thank you" in user_text.lower():
                speak("Always at your service!")

            elif "joke" in user_text:
                joke = pyjokes.get_joke()
                label.config(text=joke)
                speak(joke)

        except UnknownValueError:
            speak("Sorry couldn't hear it")


btn = tk.Button(app, text='Wake assistant',
                command=threading.Thread(target=japyp).start)
btn.pack(pady=20)
app.mainloop()
