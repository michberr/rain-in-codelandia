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


def remove_rain():

    pass


def total_rain(buildings):

    rain = len(buildings) * max(buildings)
    rain -= sum(buildings)

    return rain


def rain(buildings):
    """How much rain is trapped in Codelandia?"""

    rain = total_rain(buildings)
    # Initialize the tallest building on left and right
    # to be the tallest building overall
    if len(buildings) > 2:
        left_bldg = buildings.index(max(buildings))
        right_bldg = left_bldg

        # Create list of buildings to the left of the tallest building.
        # Check if the tallest building is on the far right. If so,
        # pass in whole list of buildings to avoid an IndexError when slicing.
        if left_bldg == len(buildings) - 1:
            left_list = buildings
        else:
            left_list = buildings[:left_bldg + 1]

        # Create list of buildings to the right of the tallest building,
        # including the tallest.
        right_list = buildings[right_bldg:]

        # Loop through buildings to the left and right of the max,
        # tabulating local rain catchement as you go. Cities with two buildings
        # or less will collect no rain and return 0.

        while len(left_list) > 2:

            # Find the next tallest building on the left
            left_bldg = left_list.index(max(left_list[:-1]))

            # Add all the rain beetween the two bookend maxima
            rain += local_rain(left_list[left_bldg:])

            # Reassign left_list to everything left of left_bldg, inclusive
            left_list = left_list[:left_bldg + 1]

        while len(right_list) > 2:

            # List of all buildings to the right of the last max,
            # not including it.
            right_list_excl = right_list[1:]

            # Find the index of the next tallest building on the right
            right_bldg = right_list_excl.index(max(right_list_excl)) + 1

            # Add all the rain:
            # If the max height building is on the right-most edge,
            # pass whole list to local_rain, otherwise, add one to outer index
            # so that the slice includes right_bldg. This approach avoids
            # an IndexError.
            if right_bldg == len(right_list) - 1:
                rain += local_rain(right_list)
            else:
                rain += local_rain(right_list[:right_bldg + 1])

            # Reassign right list to everything right of right_bldg, inclusive
            right_list = right_list[right_bldg:]

    else:
        return 0
    return rain


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
