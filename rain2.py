## Alternate implementation of rain.py

"""How much rain is trapped in Codelandia?

No buildings mean no rain is captured::

    >>> rain([])
    0

All-same height buildings capture no rain::

    >>> rain([10])
    0

    >>> rain([10, 10])
    0

    >>> rain([10, 10, 10, 10])
    0

If there's nothing between taller buildings, no rain is captured::

    >>> rain([2, 3, 10])
    0

    >>> rain([10, 3, 2])
    0

If two tallest buildings are same height and on ends, it's easy::

    >>> rain([10, 5, 10])
    5

    >>> rain([10, 2, 3, 4, 10])
    21

    >>> rain([10, 4, 3, 2, 10])
    21

    >>> rain([10, 2, 4, 3, 10])
    21

If two tallest buildings are ends, but not the same height,
it will fall off the shorter of thh two::

    >>> rain([10, 2, 3, 4, 9])
    18

Rain falls off the left and right edges::

    >>> rain([2, 3, 10, 5, 5, 10, 3, 2])
    10

Trickier::

    >>> rain([2, 3, 5, 4, 3, 10, 7, 10, 5, 4, 3, 6, 2, 5, 2])
    15

Should also work with floats::

    >>> r = rain([4.5, 2.2, 2.2, 4])
    >>> round(r, 2)
    3.6
"""

def local_rain(buildings):

    # Finds the smaller of the two "bookend" maxima
    smaller_max = min(buildings[0], buildings[-1])

    rain = 0
    
    # Add difference between each building and smaller_max to rain
    for bldg in buildings[1:-1]:
        rain += smaller_max - bldg
    
    # print "The set of local buildings is: ", buildings
    # print "The measured rain is: ", rain    
    return rain


def rain(buildings):
    """How much rain is trapped in Codelandia?"""

    rain = 0
    # Initialize the tallest building on left and right
    # to be the tallest building overall
    if len(buildings) > 2:
        left_bldg = buildings.index(max(buildings))
        right_bldg = left_bldg

        left_list = buildings[:left_bldg + 1]
        right_list = buildings[right_bldg:]

        while len(left_list) > 2:

            left_bldg = left_list.index(max(left_list[:left_bldg]))
            left_list = left_list[:left_bldg + 1]
            rain += local_rain(left_list)

        while len(right_list) > 2:

            right_bldg = right_list.index(max(right_list[1:]))
            right_list = right_list[right_bldg:]
            rain += local_rain(right_list)

    return rain


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
