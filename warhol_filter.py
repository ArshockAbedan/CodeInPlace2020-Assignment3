"""
This program generates the Warhol effect based on the original image.
"""

import random
from simpleimage import SimpleImage

N_ROWS = 2
N_COLS = 3
PATCH_SIZE = 222
WIDTH = N_COLS * PATCH_SIZE
HEIGHT = N_ROWS * PATCH_SIZE
PATCH_NAME = 'images/simba-sq.jpg'

def main():
    final_image = SimpleImage.blank(WIDTH, HEIGHT)
    # TODO: your code here.
    print("row:", "col:", "==>", "red_scale", "green_scale", "blue_scale")
    for row in range(N_ROWS):
        for col in range(N_COLS):
            red_rand = random.randrange(0, 200, 10) / 100
            green_rand = random.randrange(0, 200, 10) / 100
            blue_rand = random.randrange(0, 200, 10) / 100
            print("", row + 1, "  ", col + 1, "  ==>   ", red_rand, "      ", green_rand, "      ", blue_rand)
            patch = make_recolored_patch(red_rand, green_rand, blue_rand)
            for pixel in patch:
                final_image.set_pixel((col * PATCH_SIZE) + pixel.x, (row * PATCH_SIZE) + pixel.y, pixel)
    # This is an example which should generate a pinkish patch
    patch = make_recolored_patch(1.5, 0, 1.5)
    final_image.show()

def make_recolored_patch(red_scale, green_scale, blue_scale):
    '''
    Implement this function to make a patch for the Warhol Filter. It
    loads the patch image and recolors it.
    :param red_scale: A number to multiply each pixels' red component by
    :param green_scale: A number to multiply each pixels' green component by
    :param blue_scale: A number to multiply each pixels' blue component by
    :return: the newly generated patch
    '''
    patch = SimpleImage(PATCH_NAME)
    for pixel in patch:
        pixel.red *= red_scale
        pixel.green *= green_scale
        pixel.blue *= blue_scale
        if pixel.red > 255:
            pixel.red = 255
        elif pixel.red < 0:
            pixel.red = 0
        if pixel.green > 255:
            pixel.green = 255
        elif pixel.green < 0:
            pixel.green = 0
        if pixel.blue > 255:
            pixel.blue = 255
        elif pixel.blue < 0:
            pixel.blue = 0
    return patch

if __name__ == '__main__':
    main()