import os
import pyautogui
from PIL import Image


# define function to process each text file
def process_text_file(filename):

    # open file 
    os.system("open -a TextEdit")
    
    # wait for editor to open
    pyautogui.sleep(1)
    
    # minimize font size
    for i in range(9):
        pyautogui.hotkey("command", "-")

    # fullscreen
    pyautogui.hotkey("control", "command", "f")
    
    # zoom in
    for i in range(2):
        pyautogui.hotkey("shift", "command", ".")

    #scroll to top left
    pyautogui.moveTo(0, 0)

    screenshot = pyautogui.screenshot()
    
    
    # save screenshot to file
    screenshot_filename = os.path.splitext(filename)[0] + ".png"
    filepath = os.path.join(directory, screenshot_filename)
    
    # close text editor
    pyautogui.hotkey("command", "w")

# iterate through all text files in directory
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        # process each text file
        process_text_file(filename)


