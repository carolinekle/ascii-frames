from PIL import Image


ASCII_CHARS = ["@", "#", "S", "%", "?", "*", "+",";",":",",","."]

def resize_image(image, new_width=250):
	width, height = image.size
	ratio = height / width
	new_height = int(new_width * ratio)
	resized_image = image.resize((new_width, new_height))
	return(resized_image)


def grayify(image):
    grayscale_image = image.convert("L")
    return(grayscale_image)

def pixels_to_ascii(image):
    pixels = image.getdata()
    characters = ""
    for pixel in pixels:
        if pixel == 255:
            characters += " "
        else:
            characters += ASCII_CHARS[pixel // 25]
    return(characters)

def main(new_width=250):
	path = input("enter a pathname to an image: ")
	try:
		image = Image.open(path)
	except:
		print(path, "not valid. try again.")

		new_image_data = pixels_to_ascii(grayify(resize_image(image)))


		pixel_count = len(new_image_data)
		ascii_image = "\n".join([new_image_data[index:(index+new_width)] for index in range(0, pixel_count, new_width)])


		print(ascii_image)

		with open("test.txt", "w") as f:
			f.write(ascii_image)



main()