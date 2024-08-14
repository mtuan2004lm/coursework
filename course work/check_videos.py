import tkinter as tk
import tkinter.scrolledtext as tkst
import video_library as lib
import font_manager as fonts
from PIL import Image, ImageTk

def set_text(text_area, content):  
    """
    Updates the content of a ScrolledText widget.

    Parameters:
        text_area (tkst.ScrolledText): The ScrolledText widget to update.
        content (str): The content to set in the text area.
    """
    text_area.delete("1.0", tk.END)  # Clear existing content
    text_area.insert(1.0, content)   # Insert new content at the start

class CheckVideos(): 
    def __init__(self, window):
        """
        Initializes the CheckVideos class.

        Sets up the GUI for checking video details and listing all videos.

        Parameters:
            window (tk.Tk): The main Tkinter window instance.
        """
        window.geometry("750x350")  # Set window size
        window.title("Check Videos")  # Set window title

        # Create and place the 'List All Videos' button
        list_videos_btn = tk.Button(window, text="List All Videos", command=self.list_videos_clicked)
        list_videos_btn.grid(row=0, column=0, padx=10, pady=10)  

        # Create and place the label for entering a video number
        enter_lbl = tk.Label(window, text="Enter Video Number")
        enter_lbl.grid(row=0, column=1, padx=10, pady=10)  

        # Create and place the entry widget for video number input
        self.input_txt = tk.Entry(window, width=3)
        self.input_txt.grid(row=0, column=2, padx=10, pady=10) 

        # Create and place the 'Check Video' button
        check_video_btn = tk.Button(window, text="Check Video", command=self.check_video_clicked)
        check_video_btn.grid(row=0, column=3, padx=10, pady=10)  

        # Create and place the ScrolledText widget to display the video details
        self.list_txt = tkst.ScrolledText(window, width=48, height=12, wrap="none")
        self.list_txt.grid(row=1, column=0, columnspan=3, sticky="W", padx=10, pady=10)  

        # Create and place the status label for feedback
        self.status_lbl = tk.Label(window, text="", font=("Helvetica", 10))
        self.status_lbl.grid(row=2, column=0, columnspan=4, sticky="W", padx=10, pady=10)  

        # Create a frame to hold video details and image
        self.video_details_frame = tk.Frame(window)
        self.video_details_frame.grid(row=1, column=3, columnspan=2, sticky="NW", padx=10, pady=10)

        # Create and place the Text widget for video details
        self.video_txt = tk.Text(self.video_details_frame, width=24, height=4, wrap="none")
        self.video_txt.grid(row=1, column=3, sticky="NW", padx=10, pady=10)  

        # Create and place the label for displaying the video image
        self.image_label = tk.Label(self.video_details_frame, image=None)
        self.image_label.grid(row=2, column=3, columnspan=2, sticky="NW", padx=10, pady=10)

    def check_video_clicked(self):
        """
        Handles the 'Check Video' button click event.

        Retrieves and displays video details, increments the play count, and displays the video's image.
        """
        key = self.input_txt.get()  # Get the video number from the input field
        name = lib.get_name(key)  # Retrieve the video name from the library
        
        if name is not None:  # Check if the video exists
            director = lib.get_director(key)  # Retrieve additional video details
            rating = lib.get_rating(key)
            play_count = lib.get_play_count(key)
            
            lib.increment_play_count(key)  # Increment play count for the video
            updated_play_count = lib.get_play_count(key)  # Retrieve updated play count

            # Format video details and update the Text widget
            video_details = f"{name}\nDirector: {director}\nRating: {rating}\nPlay Count: {updated_play_count}\n"
            set_text(self.video_txt, video_details)

            link = lib.get_link(key)  # Get the link to the video image
            if link:
                try:
                    # Load and display the video image
                    image = Image.open(link)
                    image = image.resize((150, 150), Image.BILINEAR)  # Resize image
                    photo = ImageTk.PhotoImage(image)  # Convert to ImageTk.PhotoImage
                    self.image_label.configure(image=photo)  # Update the image label
                    self.photo = photo  # Keep a reference to avoid garbage collection

                except FileNotFoundError:
                    # Handle the case where the image file is not found
                    print(f"Image not found for video {key}")
                    self.image_label.configure(text="Image unavailable")
        else:
            # Display an error message if the video is not found
            set_text(self.video_txt, f"Video {key} not found")  
        
        # Update the status label
        self.status_lbl.configure(text="Check Video button was clicked!")  
    
    def list_videos_clicked(self):
        """
        Handles the 'List All Videos' button click event.

        Retrieves and displays a list of all videos in the library.
        """
        video_list = lib.list_all()  # Get the list of all videos from the library
        set_text(self.list_txt, video_list)  # Update the ScrolledText widget with the video list
        self.status_lbl.configure(text="List Videos button was clicked!") 

if __name__ == "__main__":  
    # Create the main Tkinter window
    window = tk.Tk()        
    # Configure fonts
    fonts.configure()      
    # Initialize the CheckVideos class
    CheckVideos(window)     
    # Run the Tkinter event loop
    window.mainloop()
