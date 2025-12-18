from PIL import Image
import numpy

image_file_path = "image.jpg"
output_file_path = r"C:\Users\chloe\Desktop\Dev\Image to ASCII\Image-to-ASCII" + r"\output.html"
image_width = 100
image_height = 100
is_coloured = True
char_list = list(" `.-':_,^=;><+!rc*/z?sLTv)J7(|Fi{C}fI31tlu[neoZ5Yxjya]2ESwqkP6h9d4VpOGbUAKXHm8RD#$Bg0MNWQ%&@")


if is_coloured:

    #Two arrays are created, one monochromatic to select which ASCII character to use and the other containing all RGB values
    img_colours = numpy.array(Image.open(image_file_path).resize((image_width,image_height)))
    img_array = numpy.array(Image.open(image_file_path).resize((image_width,image_height)).convert("L"))

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