from PIL import Image
import os

# ascii characters used to build the output text
ASCII_CHARS = ["Ñ","@", "#", "S", "%", "?", "*", "+", ";", ":", ",", ".", " . "]

# resize images according to a new width
def resize_image(images, new_width=300):
    width, height = images.size
    ratio = height/width/1.65
    new_height = int(new_width * ratio)
    resized_image = images.resize((new_width, new_height))
    return(resized_image)

# convert each pixel to grayscale
def grayify(images):
    grayscale_image = images.convert("L")
    return(grayscale_image)
    
# convert pixels to a string of ascii characters
def pixels_to_ascii(images):
    pixels = images.getdata()
    characters = ""
    for pixel in pixels:
        if pixel == 255:
            characters += " "
        else:
            characters += ASCII_CHARS[pixel // 25]
    return(characters)

def main(new_width=300):
    # attempt to open images from user-input
        for filename in os.listdir(os.getcwd()):
        if filename.endswith(".jpg"):
            # open image file
            with Image.open(os.path.join(os.getcwd(), filename)) as image:
                # resize, grayscale, and convert to ascii
                new_image_data = pixels_to_ascii(grayify(resize_image(image)))
  
    # convert images to ascii    
    new_image_data = pixels_to_ascii(grayify(resize_image(images)))
    
    # format
    pixel_count = len(new_image_data)  
    ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])
    
    # print result
    print(ascii_image)
    
    # save result to "ascii_image.txt"
    with open(f"{filename}.txt", "w") as f:
        f.write(ascii_image)
 
# run program
main()