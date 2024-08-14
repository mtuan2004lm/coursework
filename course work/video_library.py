# Importing the LibraryItem class from another module
from library_item import LibraryItem

# Dictionary to store LibraryItem objects, with each key being a unique identifier (e.g., "01")
library = {}

# Adding items to the library with unique keys
library["01"] = LibraryItem("Day one - Crash Symbols", "Crash Symbols", 4, "1.jpg", "1.mp3")
library["02"] = LibraryItem("Melodikaas and chips - Dr. RemiX", "Dr. RemiX", 5, "2.jpg", "2.mp3")
library["03"] = LibraryItem("Droid at the Controls - Dr. RemiX", "Dr. RemiX", 2, "3.jpg", "3.mp3")
library["04"] = LibraryItem("Anything Dub - Dr. RemiX", "Dr. RemiX", 1, "4.jpg", "4.mp3")
library["05"] = LibraryItem("8bits of Dub - Dr. RemiX", "Dr. RemiX", 3, "5.jpg", "5.mp3")

# Function to list all items in the library, formatted as a string
def list_all():
    output = ""
    for key, item in library.items():
        output += f"{key} {item.info()}\n"
    return output

# Function to get the name of an item by its key
def get_name(key):
    item = library.get(key)
    return item.name if item else None

# Function to get the director of an item by its key
def get_director(key):
    item = library.get(key)
    return item.director if item else None

# Function to get the rating of an item by its key
def get_rating(key):
    item = library.get(key)
    return item.rating if item else -1

# Function to get the link (image path) of an item by its key
def get_link(key):
    item = library.get(key)
    return item.link if item else None

# Function to set the rating of an item by its key
def set_rating(key, rating):
    item = library.get(key)
    if item:
        item.rating = rating

# Function to get the play count of an item by its key
def get_play_count(key):
    item = library.get(key)
    return item.play_count if item else -1

# Function to get the MP3 path of an item by its key
def get_mp3_path(key):
    item = library.get(key)
    return item.get_mp3_path() if item else None

# Function to increment the play count of an item by its key
def increment_play_count(key):
    item = library.get(key)
    if item:
        item.increment_play_count()

# Example usage
if __name__ == "__main__":
    # List all items in the library
    print(list_all())

    # Get details of a specific item
    print(f"Name of item '01': {get_name('01')}")
    print(f"Director of item '01': {get_director('01')}")
    print(f"Rating of item '01': {get_rating('01')} stars")
    print(f"Link of item '01': {get_link('01')}")
    
    # Increment play count
    increment_play_count("01")
    print(f"Play count of item '01' after increment: {get_play_count('01')}")

    # Update rating of an item
    set_rating("01", 5)
    print(f"Updated rating of item '01': {get_rating('01')} stars")
