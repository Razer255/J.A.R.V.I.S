import speech_recognition as sr
import os
import win32com.client
import webbrowser
import datetime
import wikipedia
import pywhatkit
import requests
from bs4 import BeautifulSoup
from colorama import Fore, Back, Style
import time
import urllib.request
import urllib.parse
import re
import smtplib
import random
import pyautogui
import threading
import subprocess





def say(text):
    speaker = win32com.client.Dispatch("SAPI.SpVoice")
    speaker.Speak(text)
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=6 and hour<12:
        say("Good Morning!")
        print( Back.YELLOW + "Good Morning" + Style.RESET_ALL)
        

    elif hour>=12 and hour<18:
        say("Good Afternoon!")   
        print(Back.LIGHTBLUE_EX + "Good Afternoon!" + Style.RESET_ALL)

    else:
        say("Good Evening!")
        print(Back.WHITE + "Good Evening!" + Style.RESET_ALL)  
    say("How can I Assist You Rishi")

def print_text_animated(text):
    for char in text:
        print(char, end= "", flush= True)
        time.sleep(0.02)
        
def search_youtube(keyword):
    encoded_keyword = urllib.parse.quote(keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + encoded_keyword).read().decode()
    video_ids = re.findall(r"watch\?v=(\S{11})", html)
    if video_ids:
        vid = "https://www.youtube.com/watch?v=" + video_ids[0]
        webbrowser.open(vid)
        print(vid)
        say("Here is the result from YouTube.")
    else:
        print("No video IDs found.")
        say("Sorry, I couldn't find any results on YouTube.")

def searchGoogle(query):
        import wikipedia as googleScrap
        keywords_to_remove = ["jarvis", "Google search", "google", "what is", "Google","google search", "Jarvis", "who was"]
        for keyword in keywords_to_remove:
            query = query.replace(keyword, "").strip()

        try:
            pywhatkit.search(query)
            result = googleScrap.summary(query,1)
            say(result)

        except:
            say("No speakable output available")
        
def set_alarm(query):
    with open("Alarmtext.txt", "w") as timehere:
        timehere.write(query)
    os.startfile("c:/Users/rishipal/Desktop/Python Work/alarm.py")
    
def repeat_after_me():
    while True:
        query = takecmd().lower()
        if "ok exit now" in query:
            say("Exiting the repeat mode.")
            break
        else:
            say(query)
            
def notepad_writing():
    subprocess.Popen("notepad.exe")
    time.sleep(1)

    while True:
        print("Listening for input to write in Notepad...")
        text = takecmd()
        
        if text == "close notepad":
            pyautogui.hotkey("ctrl", "s")
            time.sleep(1)
            pyautogui.typewrite("VoiceNote.txt")
            pyautogui.press("enter")
            time.sleep(0.5)
            pyautogui.hotkey("alt", "f4") 
            print("Notepad closed and file saved.")
            break
        else:
            pyautogui.typewrite(text)
            pyautogui.press("enter")
            
def open_portfolio():
    os.startfile("C:/Users/rishipal/Desktop/HTML work/portfolio/portfolioHome.html")
    say("Opening your portfolio...")
    print("Opening your portfolio...")

def find_and_click_dark_theme_button():
    try:
        dark_theme_button_location = pyautogui.locateCenterOnScreen('C:/Users/rishipal/Desktop/Python Work/darkthemebutton.png', confidence=0.8)
        if dark_theme_button_location:
            pyautogui.click(dark_theme_button_location)
            say("Switched to dark mode.")
            print("Switched to dark mode.")
            return True
        else:
            say("Could not locate the dark theme button. Make sure the portfolio page is fully loaded.")
            return False
    except Exception as e:
        print(f"Error locating dark theme button: {e}")
        return False

            
def open_whatsapp_web():
    threading.Thread(target=webbrowser.open, args=("https://web.whatsapp.com",)).start()
    say("Opening WhatsApp Web...")
    time.sleep(4)

def find_and_click_search_bar():
    try:
        search_bar_location = pyautogui.locateCenterOnScreen('C:/Users/rishipal/Desktop/Python Work/search_bar.png', confidence=0.8)
        if search_bar_location:
            pyautogui.click(search_bar_location)
            return True
        else:
            say("Could not locate the search bar. Please ensure WhatsApp Web is fully loaded.")
            return False
    except Exception as e:
        print(f"Error locating search bar: {e}")
        return False

def send_whatsapp_message(contact_name, message_text):
    if find_and_click_search_bar():
        pyautogui.typewrite(contact_name)
        time.sleep(1)
        pyautogui.press("enter")
        
        say(f"Sending message: {message_text}")
        pyautogui.typewrite(message_text)
        pyautogui.press("enter")
        say("Message sent.") 
            
    
def sendEmail(to, subject, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ghoshrishipal@gmail.com', 'pxag hfyt szsp xden')
    message = f'Subject: {subject}\n\n{content}'
    server.sendmail('ghoshrishipal@gmail.com', to, message)
    
def sendEmailWorkflow():
    try:
        say("Whom should I send the email to?")
        recipient = takecmd().lower()
        
        say("What should I say?")
        content = takecmd()

        contacts = {
            "mam": "parul.bhanarkar@sspu.ac.in",
            "rishi": "rishipal123ghosh@gmail.com",
            "aryan": "aryanbhosale1010@gmail.com",
            "abhishek": "parjapatabhishek62@gmail.com",
            "ritik": "ritikrcdc1322@gmail.com",
            "uday": "uday.s.raut04@gmail.com",
            "abidan": "ssabidan@gmail.com",
        }

        if recipient in contacts:
            to = contacts[recipient]
        else:
            to = recipient 

        subject = "This EMAIL IS SENT USING JARVIS"
        sendEmail(to, subject, content)
        say("Email has been sent!")
    except Exception as e:
        print(e)
        say("Sorry, I am not able to send this email")
        

def takecmd():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        r.energy_threshold = 300
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"You Said: {query}\n")
            return query
        except Exception as e:
            return "Some Error"
      
if __name__ == '__main__':
    print("             " + Back.GREEN + "JARVIS Online" + Style.RESET_ALL)
    say("JARVIS Online")
    wishMe()
    while True:
        print("Listening...")
        query = takecmd()
        # sites = [["youtube", "https://www.youtube.com"],["instagram", "https://www.instagram.com"]]
        # for site in sites:
        #     if f"Open {site[0]}".lower() in query.lower():
        #             say(f"Opening {site[0]} sir")
        #             webbrowser.open(site[1])
        sites = {
            "youtube": "https://www.youtube.com",
            "instagram": "https://www.instagram.com"
        }

        for site, url in sites.items():
            if site in query.lower():
                say(f"Opening {site}, sir")
                webbrowser.open(url)
                break
            
        if "Wake Up".lower() in query.lower():
            print(Back.GREEN + "JARVIS Online" + Style.RESET_ALL)
            say("JARVIS is Online")
                    
        if "music list" in query:
            musicPath = ("C:/Users/rishipal/Downloads/sigma.mp3")
            os.startfile(musicPath)
            
            
        if "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir the time is {strfTime}")
            
        if 'who is' in query.lower():
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                say('Searching Wikipedia...')
                print_text_animated(results)
                say("According to Wikipedia")
                say(results)
                
    
                
        if "describe yourself" in query.lower():
            say("I'm A helping A. I , I can do tasks like play music, surf websites, and many more. I was built by Rishi, and I assist him through his day-to-day work as a personal assistant. I'm built using the Python programming language.")
        
        #if "search on youtube" in query.lower():
        #    say("What would you like to search on YouTube?")
        #    print("Listening....")
        #    keyword = takecmd()
        #    say("Got it Searching"+ keyword)
        #    search_youtube(keyword)
        
        if "play" in query.lower():
            keyword = query.lower().replace("play", "").strip()
            say("Got it. Searching " + keyword + " on YouTube.")
            search_youtube(keyword)    
            
        # if "portfolio" in query.lower():
        #     os.startfile("C:/Users/rishipal/Desktop/HTML work/portfolio/portfolioHome.html")
        #     say("Opening Your Portfolio")
        if "open portfolio" in query:
            open_portfolio()
            
        if "change to dark mode" in query:
            if find_and_click_dark_theme_button():
                print("Dark mode activated.")
            
        
        if "open notepad" in query.lower():
            say("Opening Notepad for taking notes.")
            notepad_writing()
        
        if any(phrase in query for phrase in ['send a mail', 'send an email', 'send mail']):
            sendEmailWorkflow()
            

        if "send a whatsapp message" in query.lower():
            open_whatsapp_web()
            
            say("Who do you want to send the message to?")
            contact_name = takecmd().lower()
            
            if contact_name:
                say("What message would you like to send?")
                message_text = takecmd()
                
                if message_text and message_text.lower() != "some error":
                    send_whatsapp_message(contact_name, message_text)
                else:
                    say("I didn't catch the message. Please try again.")


            
        elif "set an alarm" in query.lower():
            say("Set the time")
            a = input("Please tell the time (example: 10:10:10): ")
            set_alarm(a)
            say("Done, sir")
            
        elif "temperature" in query:
             search = "temperature in Pune"
             url = f"https://www.google.com/search?q={search}"
             r  = requests.get(url)
             data = BeautifulSoup(r.text,"html.parser")
             temp = data.find("div", class_ = "BNeawe").text
             say(f"current {search} is {temp}")
             
        elif "weather" in query:
            search = "temperature in Pune"
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            say(f"current{search} is {temp}")
            print(f"current {search} is {temp}")
            
        if "repeat after me" in query.lower():
            say("Starting repeat mode. Say 'ok exit now' to stop.")
            repeat_after_me()
    
    

    
        elif "hello" in query.lower():
            say("Hello sir, how are you?")
        
        elif "i am fine" in query.lower():
            say("That's great, sir.")
        
        elif "what about you" in query.lower():
            say("Perfect sir.")
        
        elif "thank" in query.lower():
            say("You are welcome sir.")
            
        elif "i am feeling sleepy" in query.lower():
            say("Then I would like to suggest you sir,  that you should take a  nap")
        
        if "motivate me" in query.lower():
            say("Sure Sir ")
            line = ["It takes courage to grow up and become who you really are.", "Your self-worth is determined by you. You don't have to depend on someone telling you who you are.", "Believe you can and you're halfway there.", "Life shrinks or expands in proportion to one's courage."]
            random_line = random.choice(line)
            say(random_line)

        if "what is" in query.lower():
            searchGoogle(query)
        
        elif "google" in query.lower():
            searchGoogle(query)
            
        if "who was" in query.lower():
            searchGoogle(query)
        
        if "stop jarvis" in query.lower():
            say("Jarvis Going Offline")
            exit()
            
        if "good night Jarvis" in query:
            say("Good Night Sir, Jarvis Going Offline")
            print( "             " + Fore.RED ,Back.WHITE + "JARVIS GOING" + Style.RESET_ALL)
            print("               " + Fore.BLACK ,Back.WHITE + "OFFLINE" + Style.RESET_ALL)
            
            exit()
            

    
