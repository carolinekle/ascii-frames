from PIL import Image
import os
import pyautogui
import subprocess


ASCII_CHARS = ["Ñ","@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " . ", " "]
# ["█","▀", "▓", "╬", "╩", "░", "Γ", "φ", "µ", "Q", "≤", "Θ", "å", ".", ","]
#["Ñ","@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " . "]


def resize_image(images, new_width=250):
    width, height = images.size
    ratio = height/width/1.65
    new_height = int(new_width * ratio)
    resized_image = images.resize((new_width, new_height))
    return(resized_image)


def grayify(images):
    grayscale_image = images.convert("L")
    return(grayscale_image)


def pixels_to_ascii(images):
    pixels = images.getdata()
    characters = ""
    for pixel in pixels:
        if pixel == 255:
            characters += " "
        else:
            characters += ASCII_CHARS[pixel // 25]
    return(characters)

def main(new_width=250):
    for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"):
            with Image.open(os.path.join(os.getcwd(), filename)) as image:
                new_image_data = pixels_to_ascii(grayify(resize_image(image)))
                
                pixel_count = len(new_image_data)  
                ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
                
                new_filename = filename[:-4]
                
                with open(f"{new_filename}.txt", "w") as f:
                    f.write(ascii_image)




def frames(filename):


    subprocess.call(["open", "-a", "TextEdit", filename])


    pyautogui.sleep(1)


    for i in range(10):
        pyautogui.hotkey("command", "-")


    pyautogui.hotkey("ctrl", "command", "f")
   

    for i in range(4):
        pyautogui.keyDown('shift')
        pyautogui.keyDown('command')
        pyautogui.press('.')
        pyautogui.keyUp('shift')
        pyautogui.keyUp('command')


    pyautogui.hotkey("command", "up")

    screenshot = pyautogui.screenshot()
   
    pyautogui.sleep(1)

    new_filename = filename[:-4]

    screenshot_filename = new_filename + ".png"


    screenshot_filename = os.path.join("final", f"{new_filename}.png")

    try:
        os.mkdir("final")
    except FileExistsError:
        pass


    screenshot.save(screenshot_filename)
   
    pyautogui.sleep(1)

    pyautogui.hotkey("command", "w")

    pyautogui.sleep(1)

filename = "00.txt"

main()

frames(filename)

for filename in os.listdir(os.getcwd()):
    if filename.endswith(".txt"):
        frames(filename)


