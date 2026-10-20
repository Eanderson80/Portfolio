from PIL import Image
import numpy

#Directory
print("acii, base, image, pixel: ")
direct = input()
#acii converter
if(direct == "acii"):
    print("Give: ")
    input = input()
    for x in input:
        print(ord(x))
#base converter
elif(direct=="base"):
    try:
        print("Give thing to convert: ")
        result = input()

        print("what to convert from: binary, decimal, octal, or hexadecimal: ")
        start = input()

        if(start == "decimal" or start == "binary" or start == "octal" or start == "hexadecimal"):
            if(start == "binary"):
                result = int(result, 2)
            elif(start == "decimal"):
                result = int(result, 10)
            elif(start == "octal"):
                result = int(result, 8)
            elif(start == "hexadecimal"):
                result = int(result, 16)
        else:
            print("L")

        print("what to convert to: binary, decimal, octal, or hexadecimal: ")
        end = input()

        if(end == "decimal" or end == "binary" or end == "octal" or end == "hexadecimal"):
            if(end == "binary"):
                result = bin(result)
            elif(end == "octal"):
                result = oct(result)
            elif(end == "hexadecimal"):
                result = hex(result)
            print(result)
        else:
            print("l")
    #exception handling for invalid numbers
    except ValueError:
        print("bad")
#prints the pixel values of an image
elif(direct=="image"):
    try:
        print("Give image: ")
        input = input()
        image = Image.open(input)
        pixels = image.load()
        width, height = image.size
        output = ""
        for x in range(width):
            for y in range(height):
                p = pixels[x,y]
                output += str(p)
            output+="\n"
        print(output)
    #exeption handling when given an invalid path
    except FileNotFoundError:
        print("no")
#makes an image with pixel values
elif(direct=="pixel"):
    pixels = [[(200,4,4), (4,64,4), (4,4,4), (4,4,4)],[
              (4,4,4), (200,4,64), (4,4,4), (4,4,4)],[
    (4,4,4), (4,4,4), (4,4,64), (200,4,4)]]
    ar = numpy.array(pixels, dtype=numpy.uint8)
    im = Image.fromarray(ar)
    im.show()
else:
    print("Glue")