def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    res = True
    for item in lst:
        if type(item) != list:
            res = False

    return res