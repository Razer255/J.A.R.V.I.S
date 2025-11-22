import pyautogui
import time
import speech_recognition as sr
import webbrowser
import pyttsx3
import threading

engine = pyttsx3.init()

def speak(text):
    """Make the program speak the provided text."""
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        audio = recognizer.listen(source)
    try:
        command = recognizer.recognize_google(audio)
        speak(f"Command recognized: {command}")
        print(f"Command recognized: {command}")
        return command.lower()
    except (sr.UnknownValueError, sr.RequestError) as e:
        speak("Sorry, I couldn't understand that.")
        print(f"Could not understand the audio or request failed: {e}")
        return ""

def open_whatsapp_web():
    # Open WhatsApp Web in a new thread
    threading.Thread(target=webbrowser.open, args=("https://web.whatsapp.com",)).start()
    speak("Opening WhatsApp Web...")
    print("Opening WhatsApp Web...")
    time.sleep(2)  # Adjust this sleep time if needed based on internet speed

def find_and_click_search_bar():
    try:
        # Locate the search bar on the screen using the image
        search_bar_location = pyautogui.locateCenterOnScreen('C:/Users/rishipal/Desktop/Python Work/search_bar.png', confidence=0.8)
        if search_bar_location:
            pyautogui.click(search_bar_location)
            print("Found the search bar.")
            return True
        else:
            speak("Could not locate the search bar. Make sure WhatsApp Web is fully loaded.")
            return False
    except Exception as e:
        print(f"Error locating search bar: {e}")
        return False

def send_whatsapp_message(contact_name, message_text):
    if find_and_click_search_bar():
        print(f"Searching for contact {contact_name}")
        pyautogui.typewrite(contact_name)
        time.sleep(1)
        pyautogui.press("enter")
        
        speak(f"Sending message: {message_text}")
        pyautogui.typewrite(message_text)
        pyautogui.press("enter")
        speak("Message sent.")

if __name__ == "__main__":
    command = listen_for_command()
    
    if "whatsapp" in command:
        open_whatsapp_web()
        time.sleep(1)
        
        speak("Who do you want to send the message to?")
        contact_name = listen_for_command()
        
        if contact_name:
            speak("What message would you like to send?")
            message_text = listen_for_command()
            
            if message_text:
                send_whatsapp_message(contact_name, message_text)
