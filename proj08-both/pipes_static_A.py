"""
    File: pipes_static_A.py
    Author: Ming Wang
    Purpose: Creates a pip grid display, that will
    have a grid of 5 by 5. And each box can be a different pipe
    out of the 14 different pipe options that the code below will randomly
    generate. Creating a pipe layout that also have mutliple random colors
    to ensure no pipe layout is the same. 
"""

from graphics import graphics
import random
def main():
    win = graphics(500, 500, "Pipe Grid")
    
    def draw_corner(win, x, y, direction):
        """
        This function will draw the corner pipe for a grid
        Arguments: win the graphics layout, x is the x axis int value
        y is the y axis int value, direction is a string value
        that dictates the direction of the pipe
        Return Value: N/A
        """
        # Choses a random color by adjusting the rgb values
        color = win.get_color_string(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if direction.lower() == 'bottomright':
            win.line(x, y, x + 50, y, fill=color, width=6)
            win.line(x, y, x, y + 50, fill=color, width=6)
        elif direction.lower() == 'bottomleft':
            win.line(x, y, x - 50, y, fill=color, width=6)
            win.line(x, y, x, y + 50, fill=color, width=6)
        elif direction.lower() == 'upperright':
            win.line(x, y, x + 50, y, fill=color, width=6)
            win.line(x, y, x, y - 50, fill=color, width=6)
        elif direction.lower() == 'upperleft':
            win.line(x, y, x - 50, y, fill=color, width=6)
            win.line(x , y, x, y - 50, fill=color, width=6)


    def draw_horizontal(win, x, y, direction):
        """
        This function will draw the horizontal pipe for a grid
        Arguments: win the graphics layout, x is the x axis int value
        y is the y axis int value, direction is a string value
        that dictates the direction of the pipe
        Return Value: N/A
        """
        # Choses a random color by adjusting the rgb values
        color = win.get_color_string(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if direction.lower() == 'sideways':
            win.line(x-50, y, x + 50, y, fill=color, width=6) 
        if direction.lower() == 'updown':
            win.line(x,y+50,x,y-50, fill=color, width=6)


    def draw_dead_end(win, x, y, direction):
        """
        This function will draw the dead end pipe for a grid
        Arguments: win the graphics layout, x is the x axis int value
        y is the y axis int value, direction is a string value
        that dictates the direction of the pipe
        Return Value: N/A
        """
        # Choses a random color by adjusting the rgb values
        color = win.get_color_string(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if direction.lower() == 'east':
            win.line(x, y, x + 50, y, fill=color, width=6)  
            win.rectangle(x+50, y-10, 20, 20, fill=color)
        if direction.lower() == 'north':
            win.line(x,y,x,y-50, fill=color, width=6)
            win.rectangle(x-10,y - 70, 20, 20, fill=color)
        if direction.lower() == 'west':
            win.line(x,y,x-50,y, fill=color, width=6)
            win.rectangle(x-70, y-10, 20, 20, fill=color)
        if direction.lower() == 'south':
            win.line(x,y,x,y +50, fill=color, width=6)
            win.rectangle(x-10,y+50, 20, 20, fill=color)

    def draw_pipe(win, x, y, direction):
        """
        This function will draw the three pronge pipe for a grid
        Arguments: win the graphics layout, x is the x axis int value
        y is the y axis int value, direction is a string value
        that dictates the direction of the pipe
        Return Value: N/A
        """
        # Choses a random color by adjusting the rgb values
        color = win.get_color_string(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        if direction.lower() == 'sideways-up':
            draw_horizontal(win,x,y, 'sideways')
            win.line(x,y,x,y-50, fill=color,width=6)
        if direction.lower() == 'sideways-down':
            draw_horizontal(win,x,y, 'sideways')
            win.line(x,y,x,y+50, fill=color,width=6)
        if direction.lower() == 'updown-left':
            draw_horizontal(win,x,y, 'sideways')
            win.line(x,y,x-50,y, fill=color,width=6)
        if direction.lower() == 'updown-right':
            draw_horizontal(win,x,y, 'sideways')
            win.line(x,y,x+50,y, fill=color,width=6)

    # Creates the values direction of drawlings into lists
    corner = ['bottomright','bottomleft','upperright','upperleft']
    horizontal = ['sideways', 'updown', 'sideways', 'updown']
    dead_end = ['north', 'south', 'east', 'west']
    pipe = ['sideways-up', 'sideways-down', 'updown-left', 'updown-right']

    # Inital base case values
    x = 50
    y = 50
    i = 0

    # Iterates to fill a grid that is 5x5
    while i < 25:
        # Generate random number to create the grid
        draw_choice = random.randint(0,3)
        pipe_choice = random.randint(1,4)

        if pipe_choice == 1:
            draw_corner(win, x, y, corner[draw_choice])
        if pipe_choice == 2:
            draw_horizontal(win, x, y, horizontal[draw_choice])
        if pipe_choice == 3:
            draw_dead_end(win, x, y, dead_end[draw_choice])
        if pipe_choice == 4:
            draw_pipe(win,x,y, pipe[draw_choice])

        if (i+1) % 5 == 0:
            y += 100
            x = 50
        else:
            x += 100
        i += 1
    
    
    win.mainloop()

if __name__ == "__main__":
    main()
