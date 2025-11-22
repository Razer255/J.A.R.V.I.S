import pyttsx3
import datetime
import os 

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 200)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

with open("Alarmtext.txt", "rt") as extractedtime:
    time = extractedtime.read().strip()

with open("Alarmtext.txt", "w") as deletetime:
    deletetime.truncate(0)

def ring(time):
    timeset = time.replace(" and ", ":").replace("set an alarm", "").strip()
    print("Alarm set for:", timeset)
    while True:
        currenttime = datetime.datetime.now().strftime("%H:%M:%S")
        if currenttime == timeset:
            speak("Alarm ringing, sir")
            os.startfile("C:/Users/rishipal/Downloads/al.mp3")  # Change this path to your alarm sound
        elif currenttime + "00:00:30" == timeset:
            exit()

ring(time)
