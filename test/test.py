
import pyautogui

def screenshot():

    screenshot = pyautogui.screenshot()
    screenshot.save('test.png')

screenshot()