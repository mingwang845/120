
def shape_alpha():
    """
    The function shape_alpha represents a simple reference diagram.
    Arguments:N/A
    Return Value: an array that contains all the references
    """
    print("")
    x = [10, 20]
    y = [50, 60]
    return [x, 30, 40, y]

def shape_bravo():
    """
    The function shape_bravo represents a simple reference diagram.
    Arguments:N/A
    Return Value: an array that contains all the references
    """
    x = [123, 456]
    y = [789, 1024]

    a = [x,y]
    b = [y, x]
    c = [a, b]


    return c


def shape_charlie(arg1):
    """
    The function shape_charlie represents a simple reference diagram.
    Arguments:arg1 an argument that can be any value
    Return Value: an array that contains all the references
    """
    x = [arg1, arg1]
    y = [arg1, arg1]
    w = [arg1, arg1]

    a = [x, y]
    b = [a, w]
    return b

def shape_delta(arg1, arg2):
    """
    The function shape_delta represents a simple reference diagram.
    Arguments:arg1 an argument of any value, arg2 an argument
    of any value
    Return Value: an array that contains all the references
    """

    a = [arg1]
    b = [arg2]
    v = [arg1, b]
    x = [v, a]


    return [arg1, arg2, x, [17]]


def shape_echo(arg1, arg2, arg3):
    """
    The function shape_echo represents a simple reference diagram.
    Arguments:arg1 an argument of any value, arg2 an argument
    of any value, arg3 an argument of any value
    Return Value: an array that contains all the references
    """
    array1 = [arg1, None]
    array2 = [arg2, None]
    array3 = [arg3, None]

    array1[1] = array2
    array2[1] = array3
    array3[1] = array1

    return array1


