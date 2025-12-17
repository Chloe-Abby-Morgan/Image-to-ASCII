from PIL import Image
import numpy

image_file_path = "image.jpg"
output_file_path = r"C:\Users\chloe\Desktop\Dev\Image to ASCII\Image-to-ASCII" + r"\output.html"
image_width = 100
image_height = 200
char_list = " `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@"

char_list = list(char_list)

#Resizes image and makes it monochromatic
img = Image.open(image_file_path).resize((image_width,image_height)).convert("L")
img_array = numpy.array(img)

output = numpy.empty(shape=(image_height,image_width), dtype=str)

#Loops through every element of the image array and converts it to its corresponding ASCII brightness value
for row_index in range(len(img_array)):
    for pixel_index in range(len(img_array[row_index])):
        pixel_char = char_list[round(((len(char_list)-1)/256) * img_array[row_index, pixel_index])]
        output[row_index, pixel_index] = pixel_char

#Writes to a HTML file
with open(output_file_path, "w") as f:

    print("<body style =\"background-color:black; color:white;\">",file=f)
    print("<pre style>",file=f)

    for row in output:
        print(" ".join(row), file=f)

print("Image converted!" + "\n"  "Output saved to: " + output_file_path)