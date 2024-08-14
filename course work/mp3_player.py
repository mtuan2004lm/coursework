import tkinter as tk
import tkinter.scrolledtext as tkst
import pygame
import os

# Initialize Pygame mixer
pygame.mixer.init()

class MP3Player:
    def __init__(self, window):
        self.window = window
        self.window.geometry("630x400")  # Adjust the size of the main window
        self.window.title("MP3 Manager")  # Set the title of the main window

        # List of MP3 files
        self.mp3_player = [
            {"title": "Day one - Crash Symbols", "link": "Crash Symbol - Day One.mp3"},
            {"title": "Melodikaas and chips - Dr. RemiX", "link": "Dr RemiX - Melodikaas and chips.mp3"},
            {"title": "Droid at the Controls - Dr. RemiX", "link": "Dr RemiX - Droid at the Controls.mp3"},
            {"title": "Anything Dub - Dr. RemiX", "link": "Dr RemiX - Anything Dub.mp3"},
            {"title": "8bits of Dub - Dr. RemiX", "link": "Dr RemiX - 8bits of Dub.mp3"}
        ]

        # Create a ScrolledText widget to display MP3 titles
        self.text_area = tkst.ScrolledText(self.window, width=70, height=15)
        self.text_area.pack(pady=10)

        # Populate the ScrolledText widget with MP3 titles
        for item in self.mp3_player:
            self.text_area.insert(tk.END, f"{item['title']}\n")

        # Create a Play button
        self.play_button = tk.Button(self.window, text="Play", command=self.on_play_button_click)
        self.play_button.pack(pady=10)

    def play_mp3(self, filename):
        """Play the selected MP3 file"""
        if os.path.isfile(filename):
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
        else:
            print(f"File '{filename}' not found.")

    def on_play_button_click(self):
        """Play the selected MP3 file when the Play button is clicked"""
        try:
            selected_title = self.text_area.get(tk.SEL_FIRST, tk.SEL_LAST).strip()
            for item in self.mp3_player:
                if item['title'] == selected_title:
                    self.play_mp3(item['link'])
                    break
        except tk.TclError:
            print("No selection made.")

# Main application window
window = tk.Tk()

# Create an instance of the MP3Player class
mp3_player_app = MP3Player(window)

# Start the Tkinter main loop to run the application
window.mainloop()
