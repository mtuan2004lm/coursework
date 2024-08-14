import tkinter as tk  # Import the tkinter library for GUI development
import tkinter.scrolledtext as tkst  # Import ScrolledText widget for text areas with scrollbars

import video_library as lib  # Import the video_library module for managing video data
import font_manager as fonts  # Import the font_manager module for font configuration


def set_text(text_area, content):
    """Helper function to set text in a ScrolledText widget."""
    text_area.delete("1.0", tk.END)  # Clear the current content in the text area
    text_area.insert(1.0, content)  # Insert new content at the beginning


class Updatevideos:
    """Class representing the 'Update Videos' window for updating video ratings."""
    
    def __init__(self, window):
        """Initialize the Updatevideos window and its components."""
        window.geometry("750x350")  # Set the window size
        window.title("Update Videos")  # Set the window title

        # Label prompting the user to enter a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)

        # Entry field for the user to input the video number
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10)

        # Label prompting the user to enter a rating
        rating_lbl = tk.Label(window, text="Rating")
        rating_lbl.grid(row=0, column=3, padx=10, pady=10)

        # Entry field for the user to input the new rating
        self.input_rating_txt = tk.Entry(window, width=3)
        self.input_rating_txt.grid(row=0, column=4, padx=10, pady=10)

        # Button to trigger the update of the video's rating
        check_video_btn = tk.Button(window, text="Update Video Rating", command=self.update_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)

        # ScrolledText widget to display video details
        self.video_txt = tkst.ScrolledText(window, width=50, height=10)
        self.video_txt.grid(row=1, column=0, columnspan=4, padx=10, pady=10)

        # Label to display the status of actions
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)

    def update_video_clicked(self):
        """Handle the event when the 'Update Video Rating' button is clicked."""
        key = self.input_txt.get()  # Get the video number from the input field
        name = lib.get_name(key)  # Get the video name using the key
        newrating = int(self.input_rating_txt.get())  # Get the new rating from the input field
        
        if name is not None:  # Check if the video exists
            if 1 <= newrating <= 5:  # Ensure the rating is between 1 and 5
                director = lib.get_director(key)  # Get the director's name
                lib.set_rating(key, newrating)  # Update the rating in the library
                rating = lib.get_rating(key)  # Retrieve the updated rating
                play_count = lib.get_play_count(key)  # Get the current play count
                video_details = f"{name}\n{director}\nRating: {rating}\nPlays: {play_count}"  # Format video details
                set_text(self.video_txt, video_details)  # Display the video details in the text area
                self.status_lbl.configure(text="Update Video button was clicked!")  # Update the status label
            else:
                set_text(self.video_txt, f"Rating should be between 1 and 5")  # Show error if rating is out of range
                self.status_lbl.configure(text="Invalid rating input!")  # Update the status label
        else:
            self.status_lbl.configure(text=f"Video {key} not found")  # Show error if video not found

    def list_videos_clicked(self):
        """Handle the event when the 'List Videos' button is clicked."""
        video_list = lib.list_all()  # Get the list of all videos from the library
        set_text(self.list_txt, video_list)  # Display the list in the text area
        self.status_lbl.configure(text="List Videos button was clicked!")  # Update the status label


if __name__ == "__main__":
    window = tk.Tk()  # Create the main application window
    fonts.configure()  # Configure fonts using font_manager
    Updatevideos(window)  # Initialize the Updatevideos window
    window.mainloop()  # Run the application
