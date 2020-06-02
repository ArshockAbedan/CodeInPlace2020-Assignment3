"""
File: bluescreen.py
----------------
Not part of the assignment. This was a lecture demo!
This is a fun algorithm to implement. It is not in the
assignment, but feel free to implement it as an extension.
Put the smaller foreground picture into the background.
Do not include any pixels that are sufficiently blue.
"""

from simpleimage import SimpleImage

INTENSITY_THRESHOLD = 1.6

def main():
    foreground = SimpleImage('images/tiefighter.jpg')
    background = SimpleImage('images/quad.jpg')
    foreground.show()
    for pixel in foreground:
        average = (pixel.red + pixel.green + pixel.blue) // 3
        if pixel.blue >= average * INTENSITY_THRESHOLD:
            x = pixel.x
            y = pixel.y
            foreground.set_pixel(x, y, background.get_pixel(x, y))
    background.show()
    foreground.show()


if __name__ == '__main__':
    main()
