#!/usr/bin/env python
"""Image class and related functions.
"""

# Initial colour of image
INITIAL_COLOUR = 0

class ImageError(Exception):
    """Base image error.
    """
    pass

class BadCoordinateError(ImageError):
    """Error raised when user attempts to access a co-ordinate outside the
    image's dimensions.
    """
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

class Image(object):
    """Image, represented by a grid of integers (representing colours).
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.data = make_grid(width, height, INITIAL_COLOUR)

    def set(self, x, y, colour):
        """Sets the pixel at the given x, y co-ordinate to the given colour.
        """
        try:
            self.data[x - 1][y - 1] = colour
        except IndexError:
            raise BadCoordinateError(self, x, y)

    def get(self, x, y):
        """Returns the colour of the pixel at the given x, y co-ordinate.
        """
        try:
            return self.data[x - 1][y - 1]
        except IndexError:
            raise BadCoordinateError(self, x, y)

    def clear(self):
        """Sets all of the pixels in the image to the initial colour.
        """
        for x, y in box(1, 1, self.width, self.height):
            self.set(x, y, INITIAL_COLOUR)

    def __repr__(self):
        """String representation of the image.
        """
        grid_str = ""
        for y in range(1, self.height):
            for x in range(1, self.width):
                 grid_str += ("%3d" % self.get(x, y))
            grid_str += "\n"
        return grid_str

def box(x_1, y_1, x_n, y_n):
    """All co-ordinates for x_1 <= x <= x_n, y_1 <= y <= y_n.
    """
    return ((x, y) for y in range(y_1, y_n) \
                for x in range(x_1, x_n))

def make_grid(width, height, initial_element=None):
    """Create a 2D array with given width and height, initially populated with
    the given initial element. (Warning: if this is a reference it will store
    the reference, not copies!)
    """
    def make_column():
        return [initial_element for y in range(height)]
    return [make_column() for x in range(width)]
