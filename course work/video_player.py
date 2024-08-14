import tkinter as tk
from tkinter import filedialog, messagebox
import font_manager as fonts  # Importing custom font manager
from check_videos import CheckVideos  # Importing the CheckVideos class
from create_videos_list import CreateVideosList  # Importing the CreateVideosList class
from update_videos import Updatevideos  # Importing the UpdateVideos class
from mp3_player import MP3Player  # Importing the MP3Player class


# Function to handle the "Check Videos" button click event
def check_videos_clicked():
    status_lbl.config(text="Check Videos button was clicked!")  # Update status label
    CheckVideos(tk.Toplevel(window))  # Open a new window for CheckVideos

# Function to handle the "Create Videos List" button click event
def create_videos_list():
    status_lbl.config(text="Create Videos List button was clicked!")  # Update status label
    CreateVideosList(tk.Toplevel(window))  # Open a new window for CreateVideosList

# Function to handle the "Update Videos" button click event
def update_videos():
    status_lbl.config(text="Update Videos button was clicked!")  # Update status label
    Updatevideos(tk.Toplevel(window))  # Open a new window for UpdateVideos

# Function to handle the "Play MP3" button click event
def play_mp3():
    status_lbl.config(text="mp3 player button was clicked!")  # Update status label
    MP3Player(tk.Toplevel(window))

# Main application window
window = tk.Tk()
window.geometry("650x200")  # Adjust the size of the main window
window.title("Video player")  # Set the title of the main window

fonts.configure()  # Apply custom font configurations

# Header label to guide the user
header_lbl = tk.Label(window, text="Select an option by clicking one of the buttons below")
header_lbl.grid(row=0, column=0, columnspan=4, padx=10, pady=10)  # Positioning the label in a grid

# Button for checking videos
check_videos_btn = tk.Button(window, text="Check Videos", command=check_videos_clicked)
check_videos_btn.grid(row=1, column=0, padx=10, pady=10)  # Positioning the button in a grid

# Button for creating a videos list
create_videos_list_btn = tk.Button(window, text="Create Videos List", command=create_videos_list)
create_videos_list_btn.grid(row=1, column=1, padx=10, pady=10)  # Positioning the button in a grid

# Button for updating videos
update_videos_btn = tk.Button(window, text="Update Videos", command=update_videos)
update_videos_btn.grid(row=1, column=2, padx=10, pady=10)  # Positioning the button in a grid

# Button for playing MP3 files
play_mp3_btn = tk.Button(window, text="Play MP3", command=play_mp3)
play_mp3_btn.grid(row=1, column=3, padx=10, pady=10)  # Positioning the button in a grid

# Status label to show feedback to the user
status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
status_lbl.grid(row=2, column=0, columnspan=4, padx=10, pady=10)  # Positioning the label in a grid

# Start the Tkinter main loop to run the application
window.mainloop()
