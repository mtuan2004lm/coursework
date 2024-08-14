import tkinter as tk
import tkinter.scrolledtext as tkst

import video_library as lib
import font_manager as fonts

def set_text(text_area, content): 
    """
    Updates the content of a ScrolledText widget.

    Parameters:
        text_area (tkst.ScrolledText): The ScrolledText widget to update.
        content (str): The content to set in the text area.
    """
    text_area.delete("1.0", tk.END)  # Clear the existing content
    text_area.insert(1.0, content)   # Insert new content at the start

class CreateVideosList(): 
    def __init__(self, window):
        """
        Initializes the CreateVideosList class.

        Sets up the GUI for creating and managing a playlist of videos.

        Parameters:
            window (tk.Tk): The main Tkinter window instance.
        """
        self.playlist = []  # Initialize an empty playlist
        
        # Configure window size and title
        window.geometry("750x350") 
        window.title("Create Videos List") 

        # Create and place the 'Enter Video Number' label
        enter_lbl = tk.Label(window, text="Enter Video Number") 
        enter_lbl.grid(row=0, column=0, padx=10, pady=10)
        
        # Create and place the entry widget for video number input
        self.input_txt = tk.Entry(window, width=4)
        self.input_txt.grid(row=0, column=1, padx=10, pady=10)
        
        # Create and place the 'Add' button to add videos to the playlist
        check_video_btn = tk.Button(window, text="Add", command=self.add_clicked)
        check_video_btn.grid(row=0, column=2, padx=10, pady=10)  

        # Create and place the 'Reset' button to clear the playlist
        reset_btn = tk.Button(window, text="Reset", command=self.reset_clicked)  
        reset_btn.grid(row=0, column=3, padx=10, pady=10) 
        
        # Create and place the 'Play' button to play videos in the playlist
        play_btn = tk.Button(window, text="Play", command=self.play_clicked)
        play_btn.grid(row=0, column=4, padx=10, pady=10)
        
        # Create and place the ScrolledText widget to display the video list
        self.video_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.video_txt.grid(row=1, column=0, columnspan=5, sticky="W", padx=10, pady=10) 
        
        # Create and place the status label for feedback
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10)) 
        self.status_lbl.grid(row=2, column=0, columnspan=5, sticky="W", padx=10, pady=10) 

    def reset_clicked(self): 
        """
        Handles the 'Reset' button click event.

        Clears the playlist, the text area, and the input field, and updates the status label.
        """
        self.video_txt.delete("1.0", tk.END)  # Clear the text area
        self.input_txt.delete(0, tk.END)  # Clear the input field
        self.playlist.clear()  # Clear the playlist
        self.status_lbl.configure(text="Reset playlist button was clicked!")  

    def play_clicked(self):
        """
        Handles the 'Play' button click event.

        Increments the play count for each video in the playlist and for the video number entered in the input field,
        and updates the status label.
        """
        for key in self.playlist:
            lib.increment_play_count(key)  # Increment play count for each video in the playlist
        
        # Increment play count for the video number entered in the input field
        key = self.input_txt.get()
        if key:
            lib.increment_play_count(key) 
        
        self.status_lbl.configure(text="Play playlist button was clicked!") 

    def list_all(self): 
        """
        Lists all videos in the playlist.

        Retrieves video names from the library and updates the text area with the list.
        """
        output = ""
        for key in self.playlist:
            name = lib.get_name(key)  # Get the video name from the library
            output += f"{name}\n"  # Append the video name to the output string
        set_text(self.video_txt, output)  # Update the text area with the playlist

    def add_clicked(self): 
        """
        Handles the 'Add' button click event.

        Adds the video number from the input field to the playlist if it exists,
        updates the text area with the video details, and updates the status label.
        """
        key = self.input_txt.get()  # Get the video number from the input field
        name = lib.get_name(key)  # Retrieve the video name from the library
        
        if name is not None:  # Check if the video exists
            # Retrieve additional details about the video
            director = lib.get_director(key)
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            
            # Format video details and update the text area
            video_details = f"{name}\nDirector: {director}\nRating: {rating}\nPlay Count: {play_count}"
            set_text(self.video_txt, video_details)
            
            self.playlist.append(key)  # Add the video number to the playlist
            self.list_all()  # Update the text area with the updated playlist
            self.status_lbl.configure(text=f"Video {key} added!") 
        else:
            set_text(self.video_txt, f"Video {key} not found")  # Display error message in the text area
            self.status_lbl.configure(text=f"Video {key} not found")  # Update the status label
        
        self.status_lbl.configure(text="Add to playlist button was clicked!")

    def list_videos_clicked(self):
        """
        Handles the 'List Videos' button click event.

        Retrieves and displays all videos in the library.
        """
        video_list = lib.list_all()  # Get the list of all videos from the library
        set_text(self.video_txt, video_list)  # Update the text area with the video list
        self.status_lbl.configure(text="List Videos button was clicked!") 

if __name__ == "__main__":
    # Create the main Tkinter window
    window = tk.Tk() 
    # Configure fonts
    fonts.configure() 
    # Initialize the CreateVideosList class
    CreateVideosList(window) 
    # Run the Tkinter event loop
    window.mainloop()
