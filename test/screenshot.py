import os
import pyautogui

# define function to process each text file
def process_text_file(filename):
    # open file 
    os.system(f"TextEdit.txt {filename}")
    
    # wait for editor to open
    pyautogui.sleep(1)
    
    # minimize font size
    for i in range(9):
        pyautogui.hotkey("cmd", "-")

    # fullscreen
    pyautogui.hotkey("ctrl", "cmd", "f")
    
    # zoom in
    for i in range(2):
        pyautogui.hotkey("shift", "cmd", ".")

    #scroll to top left
    pyautogui.moveTo(0, 0)

    screenshot = pyautogui.hotkey("cmd", "5")
    
    
    # save screenshot to file
    screenshot_filename = os.path.splitext(filename)[0] + ".png"
    screenshot.save(screenshot_filename)
    
    # close text editor
    pyautogui.hotkey("cmd", "w")

# iterate through all text files in directory
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        # process each text file
        process_text_file(filename)