import tkinter.font as tkfont 

def configure():
    """
    Configures the default fonts for the Tkinter application.
    
    This function sets up custom font settings for different Tkinter widget types:
    - Default font
    - Text widget font
    - Fixed-width font
    """
    # Set the desired font family
    family = "Segoe UI"  # Change this to any other font family if needed
    family = "Helvetica"  # The font family used for the default, text, and fixed fonts

    # Configure the default font used by various Tkinter widgets
    default_font = tkfont.nametofont("TkDefaultFont") 
    default_font.configure(size=15, family=family) 
    # Sets the default font size to 15 and family to "Helvetica"
    
    # Configure the font used by text widgets
    text_font = tkfont.nametofont("TkTextFont") 
    text_font.configure(size=12, family=family)
    # Sets the text widget font size to 12 and family to "Helvetica"
    
    # Configure the font used by widgets that require a fixed-width font (e.g., text boxes)
    fixed_font = tkfont.nametofont("TkFixedFont") 
    fixed_font.configure(size=12, family=family) 
    # Sets the fixed-width font size to 12 and family to "Helvetica"
