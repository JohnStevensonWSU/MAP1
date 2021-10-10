#!/usr/bin/env python
from PIL import Image, ImageDraw, ImageFilter, ImageOps

def main():
    inputFile = input("Enter the picture you would like to manipulate: ")
    image = Image.open(inputFile)
    fizzBuzzX(inputFile)
    fizzBuzzY(inputFile)
    #linearGradient(inputFile)
    #radialGradient(inputFile)
    grayScale(inputFile)
    drawImage(inputFile)

def fizzBuzzX(inputFile):
    image = Image.open(inputFile)
    size = image.size
    pixels = image.load()
    
    for i in range(size[0]):
        for j in range(size[1]):
            if i % 3 == 0 and i % 5 == 0:
                pixels[i,j] = (255,0,0)
            elif i % 3 == 0:
                pixels[i,j] = (0,255,0)
            elif i % 5 == 0:
                pixels[i,j] = (0,0,255)

    image.save("FizzBuzzX.png", 'PNG')
    return

def fizzBuzzY(inputFile):
    image = Image.open(inputFile)
    size = image.size
    pixels = image.load()
    
    for i in range(size[0]):
        for j in range(size[1]):
            if j % 3 == 0 and j % 5 == 0:
                pixels[i,j] = (255,0,0)
            elif j % 3 == 0:
                pixels[i,j] = (0,255,0)
            elif j % 5 == 0:
                pixels[i,j] = (0,0,255)

    image.save("FizzBuzzY.png", 'PNG')
    return

def linearGradient(inputFile):
    image = Image.open(inputFile)
    mode = image.mode 
    image.linear_gradient(mode)
    image.save("linear_gradient.png", 'PNG')
    return

def radialGradient(inputFile):
    image = Image.open(inputFile)
    mode = image.mode 
    image.radial_gradient(mode)
    image.save("radial_gradient.png", 'PNG')
    return

def grayScale(inputFile):
    image = Image.open(inputFile)
    image = ImageOps.grayscale(image)
    image.save("gray_scale.png", 'PNG')
    return

def drawImage(inputFile):
    image = Image.open(inputFile)
    size = image.size

    draw = ImageDraw.Draw(image)
    draw.ellipse((0, 0, size[0], size[1]), fill=(255, 0, 0))

    image.save('drawn_image.png', 'PNG')
    return

if __name__ == "__main__":
    main()
