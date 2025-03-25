#! /usr/bin/python3

import shapes



# The tests will use this set to detect unexpected aliasing.  Some aliasing is
# expected and required, of course - but spurious aliasing is always an error!

ids = set()



def test_alpha():
    print("Testing shape_alpha()")

    val = shapes.shape_alpha()

    print(f"shape_alpha() returned: {val}")

    if len(val) != 4:
        print("ERROR: Invalid contents")
        return

    if val[0] != [10,20]:
        print("ERROR: Invalid contents")
        return

    if val[1] != 30:
        print("ERROR: Invalid contents")
        return

    if val[2] != 40:
        print("ERROR: Invalid contents")
        return

    if val[3] != [50,60]:
        print("ERROR: Invalid contents")
        return

    print("OK - the shape appears to be correct")


def test_bravo():
    print("Testing shape_bravo()")

    val = shapes.shape_bravo()

    print(f"shape_bravo() returned: {val}")

    if len(val) != 2:
        print("ERROR: Invalid contents")
        return

    if val[0] != 123:
        print("ERROR: Invalid contents")
        return

    if val[1] != 1024:
        print("ERROR: Invalid contents")
        return

    else:
        print("bravo is correct")
        return



def test_charlie():
    print("Testing shape_charlie()")

    val = shapes.shape_charlie(10)

    print(f"shape_charlie() returned: {val}")

    print(len(val))

    return

def test_delta():
    print("Testing shape_delta()")

    val = shapes.shape_delta(10,20)

    print(f"shape_delta() returned: {val}")

    print(len(val))

    return

def test_echo():
    print("Testing shape_echo()")

    val = shapes.shape_echo(10,20, 30)

    print(f"shape_echo() returned: {val}")

    print(len(val))

    return
test_alpha()

test_bravo()

test_charlie()

test_delta()

test_echo()
