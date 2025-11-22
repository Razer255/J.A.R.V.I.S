import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import threading
import time

class JarvisGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("JARVIS")
        self.root.geometry("400x400")
        self.root.config(bg='black')

        self.status_label = Label(root, text="JARVIS Offline", bg='black', fg='white', font=("Helvetica", 16))
        self.status_label.pack(pady=20)

        self.mic_label = Label(root, bg='black')
        self.mic_label.pack(pady=20)

        self.sound_wave_label = Label(root, bg='black')
        self.sound_wave_label.pack(pady=20)

    def update_status(self, status_text):
        self.status_label.config(text=status_text)

    def show_listening(self):
        mic_img = Image.open("mic.png")
        mic_img = mic_img.resize((100, 100), Image.ANTIALIAS)
        mic_photo = ImageTk.PhotoImage(mic_img)
        self.mic_label.config(image=mic_photo)
        self.mic_label.image = mic_photo

    def hide_listening(self):
        self.mic_label.config(image='')
        self.mic_label.image = None

    def show_speaking(self):
        pass
