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
def get_sign(num):
    """ Returns the sign (positive, negative, zero) of a number"""
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"


def get_local_max(buildings):
    """Return list of buildings that are local maxima """

    #
    bldg_a = buildings[:-1]
    bldg_b = buildings[1:]

    # Find difference between neighboring building heights
    height_diff = [b - a for a, b in zip(bldg_a, bldg_b)]


    local_max_buildings = []

    # Adds indices of buildings that are local maxima to local_max_buildings
    sign = "positive"
    for idx, num in enumerate(height_diff):
        cur_sign = get_sign(num)

        # Add building index is sign switches from positive to negative
        if sign == "positive" and cur_sign == "negative":
            local_max_buildings.append(idx)

        # Update sign unless it is zero
        # Note: if there is a series of buildings with the same height 
        # (i.e. the sign is "zero"), this will only return the index of the 
        # last building in that series.
        if cur_sign != "zero":
            sign = cur_sign

    # Checks if last building is a local max
    if height_diff[-1] > 0:
        local_max_buildings.append(len(height_diff))

    return local_max_buildings
    

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

    if len(buildings) > 2:
        max_bldgs = get_local_max(buildings)
        for i in range(len(max_bldgs[:-1])):
            rain += local_rain(buildings[max_bldgs[i]:max_bldgs[i+1] + 1])

    return rain


if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. YAY!\n"
