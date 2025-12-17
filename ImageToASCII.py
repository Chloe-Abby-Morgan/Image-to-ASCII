#Bug - This only works for square images (e.g width = 50 and height = 100 does not work)

from PIL import Image
import numpy

image_file_path = "image.jpg"
output_file_path = r"C:\Users\chloe\Desktop\Dev\Image to ASCII\Image-to-ASCII" + r"\output.txt"
image_width = 100
image_height = 50
char_list = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

char_list = list(char_list)

#Resizes image and makes it monochromatic
img = Image.open(image_file_path).resize((image_width,image_height)).convert("L")
img_array = numpy.array(img)

output = numpy.empty(shape=(image_width,image_height), dtype=str)

#Loops through every element of the image array and converts it to its corresponding ASCII brightness value

for row_index in range(len(img_array)):
    for pixel_index in range(len(img_array[row_index])):
        pixel_char = char_list[round(((len(char_list)-1)/256) * img_array[row_index, pixel_index])]
        output[pixel_index, row_index] = pixel_char

with open(output_file_path, "w") as f:
    for row in output:
        print("".join(row), file=f)

print("Image converted!" + "\n"  "Output saved to: " + output_file_path)