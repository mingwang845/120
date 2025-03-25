"""
    File: pipes_static_B.py
    Author: Ming Wang
    Purpose: Random generates different sitckfigures.
    Creating stick figures of different sizes and also color.
    While also randomly creating a different amoutn of stick figures that 
    that not display of graphics will have the same stick figure.
"""

import random
from graphics import graphics

def draw_stick_figure(win, x, y, height):
    """
    This function will draw a stick figure with the given
    variable inputs
    Arguments: win the graphics layout, x is the x axis int value
    y is the y axis int value, height is the int value for the height of 
    the stick figure
    Return Value: N/A
    """
    # Choses a random color by adjusting the rgb values
    color = win.get_color_string(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    # The head
    win.ellipse(x, y, 20, 20, fill=color)
    # The body
    win.line(x, y + 10, x, y + 10 + height, fill=color, width=2)
    # The arms
    win.line(x - 15, y + 20, x + 15, y + 20, fill=color, width=2)
    # The left leg
    win.line(x, y + 10 + height, x - 15, y + 10 + height + 20, fill=color, width=2)
    # The right leg
    win.line(x, y + 10 + height, x + 15, y + 10 + height + 20, fill=color, width=2)

def main():
    win = graphics(600, 400, "Random Stick Figures")

    num_stick_figures = random.randint(1, 6)  # You can change this to any number of stick figures you want
    x = 50  # Starting x position
    y = 50  # Starting y position

    for i in range(num_stick_figures):
        # Adding randomness to the height and position
        random_height = random.randint(30, 70)
        random_x = x + random.randint(-10, 10)
        random_y = y + random.randint(-10, 10)
        draw_stick_figure(win, random_x, random_y, random_height)
        x += 100  # Move x position for the next stick figure

    win.mainloop()

if __name__ == "__main__":
    main()
