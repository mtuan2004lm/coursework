import tkinter as tk
import tkinter.scrolledtext as tkst
import pygame
import os
import video_library as lib
import font_manager as fonts


def set_text(text_area, content):
    text_area.delete("1.0", tk.END)  # Clear the current content
    text_area.insert("1.0", content)  # Insert new content at the start


class CreateVideosList:
    def __init__(self, window):
        self.playlist = []  # Initialize an empty playlist

        # Configure window size and title
        window.geometry("750x400")
        window.title("Create Videos List")

        # Create and place the 'Enter Video Number' label
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)

        # Create and place the entry widget for video number input
        self.input_txt = tk.Entry(window, width=20)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)

        # Create and place the 'Add' button to add videos to the playlist
        add_video_btn = tk.Button(window, text="Add", command=self.add_clicked)
        add_video_btn.grid(row=0, column=2, padx=10, pady=10)

        # Create and place the 'Reset' button to clear the playlist
        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)
        reset_btn.grid(row=0, column=3, padx=10, pady=10)

        # Create and place the 'Play' button to play the selected video
        play_btn = tk.Button(window, text="Play", command=self.play_clicked)
        play_btn.grid(row=0, column=4, padx=10, pady=10)

        # Create and place the ScrolledText widget to display the video list
        self.video_txt = tkst.ScrolledText(window, width=78, height=15, wrap="none")
        self.video_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        # Bind the click event to the ScrolledText widget
        self.video_txt.bind("<Button-1>", self.on_song_click)

        # Create and place the status label for feedback
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10)

        # Initialize pygame for audio playback
        pygame.init()
        pygame.mixer.init()

    def reset_clicked(self):
        self.video_txt.delete("1.0", tk.END)  # Clear the text area
        self.input_txt.delete(0, tk.END)  # Clear the input field
        self.playlist.clear()  # Clear the playlist
        self.status_lbl.configure(text="Reset playlist button was clicked!")

    def play_clicked(self, key=None):
        if not key:
            key = self.input_txt.get()  # Get the video number from the input field

        if key in self.playlist:
            file_path = lib.get_mp3_path(key)  # Get the path to the MP3 file from the library

            if file_path and os.path.isfile(file_path):  # Check if the file exists
                try:
                    pygame.mixer.music.load(file_path)  # Load the MP3 file
                    pygame.mixer.music.play()  # Play the MP3 file
                    self.status_lbl.configure(text=f"Playing {file_path}")
                except pygame.error as e:
                    self.status_lbl.configure(text=f"Error loading MP3 file: {e}")
            else:
                self.status_lbl.configure(text=f"MP3 file {file_path} not found.")
        else:
            self.status_lbl.configure(text="Playlist is empty!")

    def list_all(self):
        output = ""
        for idx, key in enumerate(self.playlist, start=1):
            name = lib.get_name(key)  # Get the video name from the library
            output += f"{idx}. {name} ({lib.get_play_count(key)})\n"  # Append the video name and play count
        set_text(self.video_txt, output)  # Update the text area with the playlist

    def add_clicked(self):
        key = self.input_txt.get()  # Get the video number from the input field
        name = lib.get_name(key)  # Retrieve the video name from the library

        if name is not None:  # Check if the video exists
            if key not in self.playlist:
                self.playlist.append(key)  # Add the video number to the playlist
                self.list_all()  # Update the text area with the updated playlist
                self.status_lbl.configure(text=f"Video {key} added!")
            else:
                self.status_lbl.configure(text=f"Video {key} is already in the playlist.")
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Display error message in the text area
            self.status_lbl.configure(text=f"Video {key} not found")  # Update the status label

    def on_song_click(self, event):
        """
        Handles clicking on a song in the ScrolledText widget to play the corresponding MP3 file.
        """
        # Get the line number that was clicked
        clicked_index = self.video_txt.index(f"@{event.x},{event.y}")
        line_number = clicked_index.split(".")[0]

        try:
            # Get the song key from the playlist based on the line number
            key = self.playlist[int(line_number) - 1]
            self.play_clicked(key)
        except (IndexError, ValueError):
            self.status_lbl.configure(text="No song found at the clicked location.")

if __name__ == "__main__":
    # Create the main Tkinter window
    window = tk.Tk()
    # Configure fonts
    fonts.configure()
    # Initialize the CreateVideosList class
    CreateVideosList(window)
    # Run the Tkinter event loop
    window.mainloop()
