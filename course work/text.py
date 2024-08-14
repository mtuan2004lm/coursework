from library_item import LibraryItem  # Import the LibraryItem class from the library_item module

def test_item_creation():
    """
    Test the creation of LibraryItem objects and ensure that attributes are correctly assigned.
    """
    # Test 1: Create a LibraryItem without a rating (defaults to 0)
    item1 = LibraryItem("Day one", "Crash Symbols")
    assert item1.name == "Day one"  # Check if the name is correctly assigned
    assert item1.director == "Crash Symbols"  # Check if the director is correctly assigned
    assert item1.rating == 0  # Check if the default rating is 0
    assert item1.play_count == 0  # Check if the default play count is 0

    # Test 2: Create a LibraryItem with a specified rating
    item2 = LibraryItem("Melodikaas and chips", "Dr. RemiX", 4)
    assert item2.name == "Melodikaas and chips"  # Check if the name is correctly assigned
    assert item2.director == "Dr. RemiX"  # Check if the director is correctly assigned
    assert item2.rating == 4  # Check if the rating is correctly assigned
    assert item2.play_count == 0  # Check if the default play count is 0

def test_info_string():
    """
    Test the info() method to ensure it returns the correct string representation.
    """
    # Test 1: Create a LibraryItem and test the info() method
    item1 = LibraryItem("Day one", "Crash Symbols")
    assert item1.info() == "Day one - Crash Symbols "  # Check if the info string is correctly formatted

    # Test 2: Create another LibraryItem with a rating and test the info() method
    item2 = LibraryItem("Melodikaas and chips", "Dr. RemiX", 4)
    assert item2.info() == "Melodikaas and chips - Dr. RemiX ****"  # Check if the info string includes the star rating

def test_star_representation():
    """
    Test the stars() method to ensure it returns the correct number of stars based on the rating.
    """
    # Test 1: Create a LibraryItem with a rating of 2 stars and test the stars() method
    item1 = LibraryItem("Droid at the Controls", "Dr. RemiX", 2)
    assert item1.stars() == "**"  # Check if the correct number of stars is returned

    # Test 2: Create a LibraryItem with a rating of 4 stars and test the stars() method
    item2 = LibraryItem("Melodikaas and chips", "Dr. RemiX", 4)
    assert item2.stars() == "****"  # Check if the correct number of stars is returned

    # Test 3: Create a LibraryItem with a rating of 1 star and test the stars() method
    item3 = LibraryItem("Anything Dub", "Dr. RemiX", 1)
    assert item3.stars() == "*"  # Check if the correct number of stars is returned
