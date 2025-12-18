from PIL import Image
import numpy

image_file_path = "image.jpg"
output_file_path = r"C:\Users\chloe\Desktop\Dev\Image to ASCII\Image-to-ASCII" + r"\output.html"
image_width = None
image_height = None
is_coloured = True
char_list = list(" `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@")

#Sets the default values of the image dimensions to the dimensions of the image
if image_width == None:
    image_width = Image.open(image_file_path).width
if image_height == None:
    image_height = Image.open(image_file_path).height

#The image is resized, made monochromatic and converted into a numpy array
img_array = numpy.array(Image.open(image_file_path).resize((image_width,image_height)).convert("L"))

if is_coloured:

    #An array containing all RGB values
    img_colours = numpy.array(Image.open(image_file_path).resize((image_width,image_height)))
    
    output = numpy.empty(shape=(image_height,image_width), dtype="U46")

    #Loops through every element of the image array and converts it to its corresponding ASCII brightness value
    for row_index in range(len(img_array)):
        for pixel_index in range(len(img_array[row_index])):
            pixel_char = char_list[round(((len(char_list)-1)/256) * img_array[row_index, pixel_index])]
            output[row_index, pixel_index] = f"<span style=\"color: rgb({img_colours[row_index,pixel_index][0]},{img_colours[row_index,pixel_index][1]},{img_colours[row_index,pixel_index][2]})\">" + pixel_char + "</span>"

    #Writes to a HTML file
    with open(output_file_path, "w") as f:

        print("<body style =\"background-color:black;\">",file=f)
        print("<pre style>",file=f)                                                                 

        for row in output:
            print(" ".join(row), file=f)

    print("Image converted!" + "\n"  "Output saved to: " + output_file_path)

else:

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