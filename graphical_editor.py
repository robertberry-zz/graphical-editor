#!/usr/bin/env python
"""Graphical editor - run to start up the CLI session.
"""

from collections import deque
from cli import CLI

def new_image(client, m, n):
    """Loads a new image of the given dimensions.
    """
    client.new_image(m, n)

def terminate(client):
    """Terminates the session.
    """
    client.terminate()

def show(client):
    """Shows the image.
    """
    print client.image

def clear(client):
    """Clear currently loaded image.
    """
    client.image.clear()

def colour_pixel(client, x, y, colour):
    """Colour pixel at x, y with given colour in currently loaded image.
    """
    client.image.set(x, y, colour)

def draw_vertical_segment(client, col, y_1, y_n, colour):
    """Draw vertical segment in given column between given y values with given
    colour for currently loaded image.
    """
    for y in range(y_1, y_n + 1):
        client.image.set(col, y, colour)

def draw_horizontal_segment(client, x_1, x_n, row, colour):
    """Draw horizontal segment in given row between given x values with given
    colour for currently loaded image.
    """
    for x in range(x_1, x_n + 1):
        client.image.set(x, row, colour)

def fill_region(client, x, y, replacement_colour):
    """Fill the region beginning at the position x, y with replacement
    colour.
    """
    image = client.image
    
    to_process = deque()
    target_colour = image.get(x, y)

    if target_colour == replacement_colour:
        return

    to_process.appendleft([x, y])

    def is_target(node):
        """Is the given position the target colour?
        """
        return image.get(*node) == target_colour

    def is_valid(node):
        """Is a given node within the boundaries of the image?
        """
        x, y = node

        return x > 0 and x < image.width and y > 0 and y < image.height

    def xmost_target(last_pos, direction):
        """Given a position and a direction, continues to move in that
        direction until the colour is no longer the target colour. Returns the
        last node that shared the target colour.
        """
        pos = list(last_pos)

        while is_valid(pos) and is_target(pos):
            last_pos = list(pos)
            pos[0] += direction

        return last_pos

    while len(to_process) > 0:
        node = to_process.popleft()

        if is_target(node):
            left = xmost_target(node, -1)
            right = xmost_target(node, 1)
            draw_horizontal_segment(client, left[0], right[0], node[1], \
                                        replacement_colour)

            y = node[1]

            for x in range(left[0], right[0] + 1):
                above = [x, y - 1]
                if is_valid(above) and is_target(above):
                    to_process.appendleft(above)
                below = [x, y + 1]
                if is_valid(below) and is_target(below):
                    to_process.appendleft(below)

def main():
    interface = CLI()

    commands = (("I", new_image),
                ("C", clear),
                ("L", colour_pixel),
                ("V", draw_vertical_segment),
                ("H", draw_horizontal_segment),
                ("F", fill_region),
                ("S", show),
                ("X", terminate))

    for token, fn in commands:
        interface.register_command(token, fn)

    interface.main_loop()

if __name__ == "__main__":
    main()
