import pygame
import os  # Import the os module

class LibraryItem:
    def __init__(self, name, director, rating, link, mp3_path):
        """
        Initializes a LibraryItem instance with the provided details.
        
        Parameters:
        - name (str): The name or title of the library item (e.g., video title).
        - director (str): The director or creator of the library item.
        - rating (int): The rating of the library item, typically on a scale of 1 to 5.
        - link (str): A URL or file path to the library item's resource (e.g., a file location or web link).
        - mp3_path (str): The file path to the MP3 version of the item.
        """
        self.name = name
        self.director = director
        self.rating = rating
        self.link = link
        self.play_count = 0  # Initializes the play count to 0
        self.mp3_path = mp3_path

    def info(self):
        """
        Returns a formatted string that includes the item's name, director, and star rating.
        
        Returns:
        - str: A string in the format "{name} - {director} {stars()}", 
               where stars() represents the star rating.
        """
        return f"{self.name} - {self.director} {self.stars()}"
    
    def stars(self):
        """
        Returns a string of '*' characters representing the rating of the library item.
        
        Returns:
        - str: A string consisting of '*' characters. The number of '*' characters corresponds
               to the rating of the item. For example, a rating of 3 will return "***".
        """
        return "*" * self.rating

    def get_mp3_path(self):
        """
        Returns the MP3 file path for the library item.
        
        Returns:
        - str: The MP3 file path.
        """
        return self.mp3_path

    def increment_play_count(self):
        """
        Increments the play count for the library item.
        """
        self.play_count += 1

    def play_mp3(self):
        """
        Plays the MP3 file associated with the library item using Pygame.
        """
        if self.mp3_path and os.path.isfile(self.mp3_path):
            try:
                pygame.mixer.music.load(self.mp3_path)  # Load the MP3 file
                pygame.mixer.music.play()  # Play the MP3 file
                self.increment_play_count()  # Increment play count
                print(f"Playing: {self.name} - {self.mp3_path}")
            except pygame.error as e:
                print(f"Error playing {self.mp3_path}: {e}")
        else:
            print(f"MP3 file not found: {self.mp3_path}")

