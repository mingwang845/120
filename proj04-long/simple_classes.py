"""
    File: simple_classes_py
    Author: Ming Wang
    Purpose: Create and use simple classes that initialize
    and create basic operation
"""

class Simplest:
    """
    This class represents a simple class that initializes and
    creates three public fields: a, b, c.

    The constructor assigns and creates three variables,
    they can have any values.
    """
    def __init__(self, a, b, c):
        """
        This function constructors the public variables in the class
        Arguments: a is a value
        b is a value
        c is a value
        Pre-condition: none

        """
        self.a = a
        self.b = b
        self.c = c


class Rotate:
    """
    This class represents will rotate three different values,
    in a round-robin fashion, when asked to rotate the values.

    The constructor assigns the three values, while also assigning
    the value in the order that it's given: first, second, and
    third.

    The class defines serveral helpful methods and fields:
        get_first():        - gets the first value
        get_second():       - gets the second value
        get_third():        - gets the third value
        rotate():           - rotates the values round-robin
    """
    def __init__(self, first, second, third):
        """
        This function constructors the public variables in the class
        Arguments: first is a value
        second is a value
        third is a value
        Pre-condition: none

        """
        self.first = first
        self.second = second
        self.third = third

    def get_first(self):
        """
        This function returns the first value
        Arguments: None
        Return Value: the first value in rotate
        """
        return self.first

    def get_second(self):
        """
        This function returns the second value
        Arguments: None
        Return Value: the second value in rotate
        """
        return self.second

    def get_third(self):
        """
        This function returns the third value
        Arguments: None
        Return Value: the third value in rotate
        """
        return self.third

    def rotate(self):
        """
        This function rotates the value in the class round-robin style
        Arguments: None
        Return Value: N/A
        """
        # a placeholder is used so that you can rotate the values and
        # so you can reassign the first value back the third place without overlapping

        placeholder = self.first
        self.first = self.second
        self.second = self.third
        self.third = placeholder


class Band:
    """
    This class represents a musical group. Where there is one singer,
    one drummer, and any number of guitar players. When first initialized you will
    only be having a singer

    The constructor assigns  the singer variable, while also
    initialize the drummer variable adn the guitar_player list

    The class defines serveral helpful methods and fields:
        get_singer():                   - gets the singer value
        set_singer(new_singer):         - sets the singer value
        get_drummer():                  - gets the drummer value
        set_drummer(new_drummer):       - sets the new_drummer value
        add_guitar_player(new_guitar_player):  - add a new guitar player to the list
        fire_all_guitar_players():             - remove and fires all guitar players
        get_guitar_players():                  - returns a list of all the guiatr players
        play_music():                          - prints out the sounds the band makes
    """

    def __init__(self,singer):
        """
        This function constructors the public variables in the class
        Arguments: singer is a value
        Pre-condition: none

        """
        self.singer = singer
        self.drummer = None
        self.guitar_players = []

    def get_singer(self):
        """
        This function returns the singer value
        Arguments: None
        Return Value: the singer value in Band
        """
        return self.singer

    def set_singer(self, new_singer):
        """
        This function sets the singer a new name
        Arguments: new_singer
        Return Value: None
        """
        self.singer = new_singer

    def get_drummer(self):
        """
        This function returns the drummer value
        Arguments: None
        Return Value: the drummer value in Band
        """
        return self.drummer

    def set_drummer(self, new_drummer):
        """
        This function sets the drummer a new name
        Arguments: new_drummer
        Return Value: None
        """
        self.drummer = new_drummer

    def add_guitar_player(self, new_guitar_player):
        """
        This function adds a new guitar player to the guitar player list
        Arguments: new_guitar_player
        Return Value: None
        """
        self.guitar_players.append(new_guitar_player)

    def fire_all_guitar_players(self):
        """
        This function removes all the guitar players in the current list
        Arguments: None
        Return Value: None
        """
        self.guitar_players = []

    def get_guitar_players(self):
        """
        This gets all the guitar players
        Arguments: None
        Return Value: list of the guitar players
        """
        return list(self.guitar_players)

    def play_music(self):
        """
        This function prints out all the music that will be played by
        the band as a whole
        Arguments: None
        Return Value: None
        """
        if self.singer == "Frank Sinatra":
            print("Do be do be do")
        elif self.singer == "Kurt Cobain":
            print("bargle nawdle zouss")
        else:
            print("La la la")
        if self.drummer:
            print("Bang bang bang!")

        for guitar in self.guitar_players:
            print("Strum!")



class Color:
    """
    This class represents RGBcolor. It stores and upates red, green, and blue
    components of the color as integers.

    The constructor assigns  the singer variable, while also
    initialize the drummer variable adn the guitar_player list

    The class defines serveral helpful methods and fields:
        setValue():                   - sets the int value of the colors
        __str__():         - returns the string values of the colors
        html_hex_color():                  - returns the converted int to hexi
        set_standard_color(name):       - sets the color of the rbg values
        remove_red():  - removes and sets the red value as r
    """

    def __init__(self, r, g, b):
        """
        This function constructors the public variables in the class
        Arguments: r the red value
        g the green value
        b the blue value
        Pre-condition: none

        """
        self.r = self.setValue(r)
        self.g = self.setValue(g)
        self.b = self.setValue(b)

    def setValue(self, value):
        """
        This function is a helper methods that sets and checks to ensure
        the values given are within a certain range.
        Arguments: value int the value of the rgb color
        Return Value: None
        Pre-condition: none
        """
        if value < 0:
            return 0
        elif value > 255:
            return 255
        else:
            return value

    def __str__(self):
        """
        This function will return a tuple of the rgb values in a string format
        Arguments: None
        Return Value: Returns a string of the values
        Pre-condition: none
        """
        return f"rgb({self.r},{self.g},{self.b})"

    def html_hex_color(self):
        """
        This function will return a tuple of the rgb values in a string format
        converting the int into hex.
        Arguments: None
        Return Value: Returns a string of the values of the hex values
        Pre-condition: none
        """
        return f"#{self.r:02X}{self.g:02X}{self.b:02X}"

    def get_rgb(self):

        """
        This function will get and return the rgb value in a tuple
        Arguments: None
        Return Value: Returns a tuple values of the rgb
        Pre-condition: none
        """
        return (self.r, self.g, self.b)

    def set_standard_color(self,name):
        """
        This function sets the colors if it's a standard color using name
        Arguments: name is a string for the color name
        Return Value: None
        Pre-condition: none
        """
        name = name.lower()
        if name == "white":
            self.r, self.g, self.b = 255, 255, 255
        if name == "black":
            self.r, self.g, self.b = 0, 0, 0
        if name == "red":
            self.r, self.g, self.b = 255, 0, 0
        if name == "yellow":
            self.r, self.g, self.b = 255, 255, 0

    def remove_red(self):
        """
        This function removes the red color by setting it to 0
        Arguments: None
        Return Value: None
        Pre-condition: none
        """
        self.r = 0