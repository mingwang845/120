"""
    File: animation_long.py
    Author: Ming Wang
    Purpose: Creates a animation that involves a snowflake
    where it will rotate around the origin of the screen and
    will rotate indefinetily until one destroys the graphic.
"""

import math
from graphics import graphics


def main():
    g = graphics(800, 800, "Snowflake Animation")

    def draw_branch(g, x, y, length, angle, depth):
        """
        This function will draw branches for the snowflake
        Arguments: g is the graphics, x is the x-coordinate, y is
        the y-coordinate, length is length of the branches, angle
        is teh angle at which you should offset and draw the branches,
        and depth is the total amount of branch layer you have
        Return Value: N/A
        """
        if depth == 0:
            return
        end_x = x + length * math.cos(math.radians(angle))
        end_y = y + length * math.sin(math.radians(angle))
        g.line(x, y, end_x, end_y, fill='blue', width=2)

        # Draw smaller branches
        for offset in [-30, 30]:
            draw_branch(g, end_x, end_y, length * 0.6, angle + offset, depth - 1)

    def draw_snowflake(g, x, y, size, angle, depth):
        """
        This will draw the total number of snowflakes that you want to be drawn
        Arguments:  g is the graphics, x is the x-coordinate, y is
        the y-coordinate, length is length of the branches, angle
        is teh angle at which you should offset and draw the branches,
        and depth is the total amount of branch layer you have
        Return Value: N/A
        """
        for i in range(6):
            branch_angle = angle + i * 60
            draw_branch(g, x, y, size, branch_angle, depth)

    angle = 0
    while not g.is_destroyed():
        g.clear()

        # Calcultes the new angle
        center_x = 400 + 200 * math.cos(math.radians(angle))
        center_y = 400 + 200 * math.sin(math.radians(angle))

        draw_snowflake(g, center_x, center_y, 30, angle, 5)
        draw_snowflake(g, center_x, center_y, 100, angle, 3)
        angle += 2
        g.update_frame(30)
main()
