import os
import pyautogui
import subprocess




# define function to process each text file
def process_text_file(filename):

    # open file 
    subprocess.call(["open", "-a", "TextEdit", filename])
    
    # wait for editor to open
    pyautogui.sleep(1)

    # minimize font size
    for i in range(9):
        pyautogui.hotkey("command", "-")

    # fullscreen
    pyautogui.hotkey("ctrl", "command", "f")
    
    # zoom in
    for i in range(4):
        pyautogui.keyDown('shift')
        pyautogui.keyDown('command')
        pyautogui.press('.')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('command')

    #scroll to top left
    pyautogui.hotkey("command", "up")

    screenshot = pyautogui.screenshot()
    
    
    # save screenshot to file
    screenshot_filename = os.path.splitext(filename)[0] + ".png"
    screenshot.save(screenshot_filename)
    
    # close text editor
    pyautogui.hotkey("command", "w")

filename = "00.jpg.txt"

process_text_file(filename)


# iterate through all text files in directory
for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        process_text_file(filename)


